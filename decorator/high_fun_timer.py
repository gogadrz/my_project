import time
from typing import Callable, Any
import functools


def timer(func: Callable) -> Callable:
    """
    Декоратор выводящий время,
    которое заняло выполнение декорируемой функции.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)

        print('Время выполнения функции {} сек.'.format(run_time))

        return result

    return wrapped_func


def logging(func: Callable) -> Callable:
    """
    Декоратор логирующий работу кода
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:

        print('Вызывается функция {func}\n'
              'позиционные аргументы {args}\n'
              'именованные аргументы {kwargs}'.format(
            func=func.__name__,
            args=args,
            kwargs=kwargs
        ))

        result = func(*args, **kwargs)
        print('Функция успешно завершила работу.')
        return result

    return wrapped_func


@logging
@timer
def squares_sum() -> int:
    number = 100
    result = 0

    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])

    return result


@timer
@logging
def cubes_sum(number: int) -> int:
    result = 0

    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])

    return result


# my_result = timer(squares_sum)
# print(my_result)
# print()
# my_cubes_sum = timer(cubes_sum, 200)
# print(my_cubes_sum)

my_sum = squares_sum()
print(my_sum)

my_cubes_sum = cubes_sum(200)
print(my_sum)

print(logging.__doc__)
print(squares_sum.__name__)

