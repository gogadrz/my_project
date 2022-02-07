from typing import Callable, Any


def dec_fun(func: Callable) -> Callable:
    """
    Декоратор.
    Вызывает декорированную функцию 2 раза.
    :param func: функция
    :return: функция
    """

    def wrapped_func(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        func(*args, **kwargs)

        return result

    return wrapped_func


@dec_fun
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
