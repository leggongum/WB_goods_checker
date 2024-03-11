from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove


router = Router()

@router.message(Command("start"))
async def get_start(message: Message):
    await message.answer(message.text)



@router.message(Command("menu"))
async def get_menu(message: Message):
    await message.answer(message.text)