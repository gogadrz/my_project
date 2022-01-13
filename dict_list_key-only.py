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


print()

# цикл по ключам верхнего уровня
for d_key in data.keys():

    # печатаем ключ верхнего уровня
    print(d_key)

    # словарь - напечатать ключи
    if type(data[d_key]) is dict:
        print('{')
        for i in data[d_key]:
            print('\t', i)
        print('}')

    # список
    if type(data[d_key]) is list:
        for j in range(len(data[d_key])):
            print('[]')
            for x in data[d_key][j]:
                print('{}', x)
                if type(data[d_key][j][x]) is dict:
                    for z in data[d_key][j][x]:
                        print('--{}', z)


