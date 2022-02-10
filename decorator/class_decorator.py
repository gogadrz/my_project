from datetime import datetime
import functools
import time
from typing import Callable


def create_time(cls):
    """ Декоратор класса, выдает время создания инстанса класса """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print('Время создания инстанса класса {}'.format(datetime.utcnow()))
        return instance
    return wrapper


def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        total = time.time() - start
        print('Время выполнения функции {total}'.format(total=total))
        return result
    return wrapped


def for_all_method(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                cur_method = getattr(cls, i_method)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method, decorated_method)

        return cls

    return decorate



@create_time
@for_all_method(timer)
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0

        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(self.max_num)])

        return result

    def cubes_sum(self, number: int) -> int:
        result = 0

        for _ in range(number):
            result += sum([i_num ** 3 for i_num in range(self.max_num)])

        return result


my_funcs_1 = Functions(max_num=1000)
# time.sleep(2)
# my_funcs_2 = Functions(max_num=2000)
# time.sleep(3)
# my_funcs_3 = Functions(max_num=3000)
my_funcs_1.squares_sum()
my_funcs_1.cubes_sum(number=2000)
