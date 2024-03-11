from datetime import datetime


def parse_json(json: dict) -> dict:
    name = json['data']['products'][0]['name']
    articul = json['data']['products'][0]['id']
    price = json['data']['products'][0]['priceU']
    sale_price = json['data']['products'][0]['salePriceU']
    all_amount = 0
    for size in json['data']['products'][0]['sizes']:
        for stock in size['stocks']:
            all_amount += stock['qty']
    return {'name': name, 'articul': articul, 'price': price, 'sale_price': sale_price, 'all_amount': all_amount}


def form_response_text(info):
    return f'''<b>Товар:</b> {info['name']}
<b>Артикул:</b> {info['articul']}
<b>Цена со скидкой:</b> {round(info['sale_price'] / 100, 2)}₽
<b>Цена без скидки:</b> <del>{round(info['price'] / 100, 2)}₽</del>
<b>Общее количество на складах:</b> {info['all_amount']}'''


def form_db_response(data: list[dict]):
    return ''.join(
        f'''<b>id:</b> {action['id']}
<b>id пользователя:</b> {action['user_id']}
<b>Артикул:</b> {action['articul']}
<b>Дата:</b> {datetime.strftime(action['timestamp'], '%d-%m-%Y %H:%M:%S')}\n\n''' for action in data
    )
