def calc_qty_amt(store_dict, code_num):
    pcs = cost = 0
    for index in range(len(store_dict[code_num])):
        pcs += store_dict[code_num][index]['quantity']
        cost += store_dict[code_num][index]['quantity'] * \
                store_dict[code_num][index]['price']

    return pcs, cost


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key_g in goods:
    cnt, price = calc_qty_amt(store, goods[key_g])
    print('{0} - {1} шт, стоимость {2} руб'.format(key_g, cnt, price))
