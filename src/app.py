from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, Update

from fastapi import FastAPI, Request

from config import settings


bot = Bot(settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


app = FastAPI('WB_goods_checker')

@app.post('/')
async def webhook(request: Request):
    update = Update.model_validate(await request.json(), context={'bot': bot})
    await dp.feed_update(bot, update)