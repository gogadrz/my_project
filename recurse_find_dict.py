def seek_key(struct, key):
    if key in struct:
        return struct[key]

    for substruct in struct.values():
        if isinstance(substruct, dict):
            result = seek_key(substruct, key)
            if result:
                break
        else:
            result = substruct
            break
    else:
        result = None

    return result


site = {
    'html': {
        'hevj': '123',
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input('Введите ключ для поиска: ')

result = seek_key(site, key)
if result:
    print(result)
else:
    print('Ключ в структуре не найден')

