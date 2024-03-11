from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class main(CallbackData, prefix='main'):
    action: str


start_buttons = [
    [InlineKeyboardButton(text='Получить информацию по товару', callback_data='main:get_good_info')],
    [InlineKeyboardButton(text='Остановить уведомления', callback_data='main:stop_notifications')],
    [InlineKeyboardButton(text='Получить информацию из БД', callback_data='main:get_db_info')],
]

main_menu = InlineKeyboardMarkup(inline_keyboard=start_buttons)


def get_context_sub_menu(articul: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Подписаться', callback_data=f'sub:{articul}')]
    ])
