from typing import Callable, ClassVar
import functools
from datetime import datetime
import time


def get_date_string(format_string):
    dt, tm = format_string.split(' - ')

    month, day, year = map(str, dt.split())
    hours, minutes, secs = map(str, tm.split(':'))
    now = datetime.now()

    str_format = '%{month} %{day} %{year} - %{hours}:%{minutes}:%{secs}'.format(
        month=month,
        day=day,
        year=year,
        hours=hours,
        minutes=minutes,
        secs=secs
    )

    return now.strftime(str_format)


def timer(cls: ClassVar, func: Callable, date_format: str) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        cls_name = cls.__name__
        func_name = func.__name__

        date_time_str = get_date_string(date_format)
        print('- Запускается \'{cls}.{func}\'. '
              'Дата и время запуска: {date_time}'.format(
            cls=cls_name,
            func=func_name,
            date_time=date_time_str
        ))

        start = time.time()
        result = func(*args, **kwargs)
        total = round(time.time() - start, 3)

        print('- Завершение \'{cls}.{func}\','
              ' время работы = {total}s'.format(
            cls=cls_name,
            func=func_name,
            total=total
        ))
        return result

    return wrapped


def log_methods(date_format: str) -> Callable:
    def decorate(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                cur_method = getattr(cls, i_method)
                decorated_method = timer(cls, cur_method, date_format)
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

# Здравствуйте Александр.
# У меня так и не получилось добиться вывода: "Тут метод" перед именем метода и
# "у наследника" после. А если присмотреться, в примере выводится с символом
# подчеркивания, тогда как в самих функциях написано через пробел... я так и не понял что
# с этим поделать. Хотелось бы разобраться. Видео смотрел 2 раза, не помогло.
# Али с ухом приключился у меня какой изъян (как говорил Федот-стрелец)

# Спасибо.
