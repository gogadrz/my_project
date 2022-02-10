from typing import Callable, Any
import functools


def decorator(func: Callable) -> Callable:

    # Что бы можно было получать информацию о декорируемой функции, используем @functools.wraps(имя функции)
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:

        # Код до вызова функции

        value = func(*args, **kwargs)

        # Код после вызова функции

        return value
    return wrapped_func


@decorator
def some_function(*args):
    pass
