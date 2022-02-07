from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    """
    Надоедливый декоратор.

    При вызове декорируемой функции спрашивает у пользователя
    'Как дела?' и вне зависимости от его ответа,
    'держит в курсе' и отвечает что-то вроде 'А у меня не очень!'
    и только потом запускает саму функцию.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print('Как дела?', end=' ')
        input()
        print('А у меня не очень! Ладно, держи свою функцию.')

        value = func(*args, **kwargs)

        return value

    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


def main():
    test()


main()
