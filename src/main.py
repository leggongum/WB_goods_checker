import asyncio

from handler import router
from app import bot, dp, app



if __name__ == '__main__':
    # To start webhook run command `uvicorn main:app`
    # To start polling run command `python main.py`
    dp.include_router(router)
    asyncio.run(dp.start_polling(bot))
