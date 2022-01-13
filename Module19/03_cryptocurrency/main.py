data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}


for d_key in data.keys():
    # печатаем ключ верхнего уровня, если это словарь то и значение
    print(d_key, ': ', sep='', end='')
    if (not type(data[d_key]) is list) and (not type(data[d_key]) is dict):
        print(data[d_key], sep='', end='')
    print()

    # словарь - напечатать ключи
    # верхний уровень
    if type(data[d_key]) is dict:
        print('\t{')
        for key_dict1 in data[d_key]:
            print('\t\t', key_dict1, ': ', data[d_key][key_dict1], sep='')
        print('\t}')

    # список в словаре
    elif type(data[d_key]) is list:
        print('\t[')
        for dict_in_list in range(len(data[d_key])):
            print('\t\t{')
            for ddl in data[d_key][dict_in_list]:
                if type(data[d_key][dict_in_list][ddl]) is dict:
                    print('\t\t', ddl)
                    print('\t\t\t{')
                else:
                    print('\t\t', ddl, data[d_key][dict_in_list][ddl])
                if type(data[d_key][dict_in_list][ddl]) is dict:
                    for dld in data[d_key][dict_in_list][ddl]:
                        print('\t\t\t', dld, ': ', data[d_key][dict_in_list][ddl][dld], sep='')
                    print('\t\t\t}')
            print('\t\t}')
        print('\t]')

# В “ETH” добавить ключ “total_diff” со значением 100
data['ETH']['total_diff'] = 100

# Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”
data['tokens'][0]['fst_token_info']['name'] = 'doge'

# Удалить “total_out” из tokens и присвоить
# его значение в “total_out” внутри “ETH”.
# Так как в 'tokens' 2 ключа 'total_out, удалим их
# разными способами
data['ETH']['total_out'] = data['tokens'][0].pop('total_out')
del data['tokens'][1]['total_out']

# Внутри "sec_token_info" изменить название ключа “price” на “total_price”
data['tokens'][1]['sec_token_info']['total_price'] =\
    data['tokens'][1]['sec_token_info'].pop('price')
