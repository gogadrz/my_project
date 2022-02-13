from typing import Callable, Any
import functools


class app:
    """
    Класс app.
    Пришлось написать имя с маленькой буквы,
    что бы работал код из примера.
    В классе всего один странный метод get, принимающий параметр,
    который он никак не использует
    """

    @classmethod
    def get(cls, param: str) -> Callable:
        return example


def callback(param: str) -> Callable:
    """ Декоратор с параметром, ничего не делает """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            value = func(*args, **kwargs)
            # print('Inside callback. Param: {}'.format(param))
            return value

        return wrapped_func

    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


def main():
    route = app.get('//')
    if route:
        response = route()
        print('Ответ:', response)
    else:
        print('Такого пути нет')


main()
