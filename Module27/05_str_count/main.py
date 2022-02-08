from typing import Callable, Any
import functools


def counter(func: Callable) -> Callable:
    """
    Декоратор-счетчик.

    Показывает сколько раз была вызвана функция.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:

        wrapped_func.count += 1
        result = func(*args, **kwargs)

        print('Функция {func} вызвана {count} раз.'.format(
            func=func.__name__,
            count=wrapped_func.count
        ))

        return result

    wrapped_func.count = 0
    return wrapped_func


@counter
def my_func() -> None:
    print('Inside my_func()')


def main():
    my_func()
    my_func()
    my_func()
    my_func()


main()
