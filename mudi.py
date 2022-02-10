from typing import Callable, Any, Optional
import functools
import time


def decorator_timer(_func: Optional[Callable] = None, *, wait: int = 1) -> Callable:
    def timer(func: Callable) -> Callable:
        """
        Декоратор. Таймер
        Выжидает паузу wait секунд
        :param func: функция
        :return: функция
        """
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            time.sleep(wait)
            result = func(*args, **kwargs)
            return result
        return wrapped_func
    if _func is None:
        return timer

    return timer(_func)


@decorator_timer(wait=3)
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
