from typing import Callable, Any
import functools
import time


def timer_decorator(func: Callable) -> Callable:
    """
    Декоратор.

    Перед вызовом декорируемой функции ждет 3 секунды.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:

        print('Wait 3 seconds')
        for _ in range(3):
            time.sleep(1)
            print('.', end='')
        print('\nDone.')

        value = func(*args, **kwargs)

        return value

    return wrapped_func


@timer_decorator
def my_function():
    print('Inside my_function()')


def main():

    my_function()


main()
