def find_key(struct, key):
    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key)
            if result:
                break
    else:
        result = None

    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        },
        'nobody': {
            'nobody2': {
                'text': {
                    'inside': 'внутри текста'
                }
            }

        }
    }
}

seek_key = 'text'

x = find_key(site, seek_key)
if x:
    print(x)
else:
    print('ключ {0} отсутствует'.format(seek_key))
