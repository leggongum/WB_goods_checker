from aiohttp import ClientSession


URL = 'https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={}'


async def get_good_info_from_wb(articul: int):
    async with ClientSession() as session:
        async with session.get(URL.format(articul)) as response:
            return await response.json()