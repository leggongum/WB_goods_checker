from wb_request import get_good_info_from_wb
from utils import parse_json, form_response_text
from app import bot

import asyncio


user_coroutine_map = {}

async def validate_response_and_send_good_info(chat_id, articul, markup):
    try:
        info = parse_json(await get_good_info_from_wb(articul))
    except ValueError:
        await bot.send_message(chat_id, 'Принимается только артикул в виде числа.')
        raise ValueError
    except IndexError:
        await bot.send_message(chat_id, f'Товара с артикулом {articul} не существует.')
        raise IndexError
    else:
        await bot.send_message(chat_id, form_response_text(info), reply_markup=markup)


async def send_notifications(chat_id, articul):
    while True:
        await asyncio.sleep(5*60)
        await validate_response_and_send_good_info(chat_id, articul, None)
        