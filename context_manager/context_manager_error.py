class Example:
    def __init__(self) -> None:
        print('Вызов __init__')

    def __enter__(self) -> 'Example':
        print('Вызов __enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Вызов __exit__')
        if exc_type == Exception:
            print('Тип ошибки: {}'.format(exc_type))
            print('Значение ошибки: {}'.format(exc_val))
            print('"След ошибки: "{}'.format(exc_tb))
            return True


my_obj = Example()

with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')
    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

    print('Я обязательно выведусь...')
