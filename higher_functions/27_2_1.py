from typing import Callable


def func_1(x: int) -> int:
    return x + 10


def func_2(func: Callable, *args, **kwargs) -> int:
    result = func(*args, **kwargs) * func(*args, **kwargs)
    return result


# print(func_1(4))

print(func_2(func_1, 9))
