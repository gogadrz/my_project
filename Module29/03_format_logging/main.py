from typing import Callable
import functools
import time


def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        total = time.time() - start
        print('Время выполнения функции {total}'.format(total=total))
        return result

    return wrapped


def log_methods(date_format: str) -> Callable:
    def decorate(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                print('- Запускается {name}.{method}. '
                      'Дата и время запуска:'.format(
                    name=cls.__name__,
                    method=i_method
                ))
                cur_method = getattr(cls, i_method)
                decorated_method = timer(cur_method)
                setattr(cls, i_method, decorated_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
