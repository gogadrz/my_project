from typing import Callable, Any, Optional
import functools
import time


def timer_with_precision(_func: Optional[Callable] = None, *, precision: int = 1) -> Callable:
    def timer_decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            started = time.time()
            value = func(*args, **kwargs)
            ended = time.time() - started

            print('Время работы функции {} секунд'.format(round(ended, precision)))

            return value
        return wrapped_func
    if _func is None:
        return timer_decorator
    return timer_decorator(_func)


@timer_with_precision()
def squares_sum() -> None:
    var = [x ** 2 for x in range(100000)]


@timer_with_precision(precision=4)
def cubes_sum(num: int) -> None:
    var = [x ** 3 for x in range(100000)]
    print('num =', num)


def main():
    squares_sum()
    cubes_sum(3)


main()
