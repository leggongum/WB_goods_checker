from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from db.db_methods import insert_action, select_five_last_actions
from callback import main, main_menu, get_context_sub_menu
from notifications import send_notifications, validate_response_and_send_good_info, user_coroutine_map
from utils import form_db_response

import asyncio

router = Router()


@router.message(Command("start"))
async def get_start(message: Message):
    await message.answer('Привет! \nДля получения информации по товару Wildberries, введи его артикул.')


@router.message(Command("menu"))
async def get_menu(message: Message):
    await message.answer('Доступные команды:', reply_markup=main_menu)


@router.callback_query(main.filter(F.action=='get_good_info'))
async def get_good_info(call: CallbackQuery):
    await call.answer('Для получения информации по товару, введите его артикул.')


@router.callback_query(main.filter(F.action=='stop_notifications'))
async def stop_notifications(call: CallbackQuery):
    try:
        user_coroutine_map[call.from_user.id].close()
        del user_coroutine_map[call.from_user.id]
    except KeyError:
        await call.answer('Вы не подписаны на уведомления')
    else:
        await call.answer('Вы отписаны')


@router.callback_query(main.filter(F.action=='get_db_info'))
async def get_db_info(call: CallbackQuery):
    actions = await select_five_last_actions()
    await call.message.answer(form_db_response(actions))


@router.callback_query(F.data.startswith('sub'))
async def subscribe(call: CallbackQuery):
    if user_coroutine_map.get(call.from_user.id, False):
        user_coroutine_map[call.from_user.id].close()
    coroutine = send_notifications(call.from_user.id, call.data.split(':')[1])
    user_coroutine_map[call.from_user.id] = coroutine
    asyncio.create_task(coroutine)
    await call.answer('Вы успешно подписаны!')


@router.message()
async def get_good_info_by_articul(message: Message):
    await validate_response_and_send_good_info(message.from_user.id, message.text, get_context_sub_menu(message.text))
    await insert_action(message.from_user.id, int(message.text))
