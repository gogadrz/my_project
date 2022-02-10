from contextlib import contextmanager
from typing import Iterable


@contextmanager
def next_num(num: int) -> Iterable[int]:
    # до yield - как в методе __enter__
    print('Входим в функцию')
    try:
        yield num + 1

    except ZeroDivisionError as exc:
        print('Ошибка: {exc}'.format(exc = exc))
    finally:
        print('Это выполнится в любом случае')
    print('Выход из функции')  # после yield - как в методе __exit__


# в next попадает то, что сгенерировалось в yield
with next_num(-1) as next:
    print('Следующее число = {next}'.format(next = next))
    print(10 / next)
