from typing import Callable, Any
import functools
from datetime import datetime


def write_to_log_file(func: Callable, er: Exception) -> None:
    """
    Функция пишет в файл 'function_errors.log'
    дату и время, имя функции в которой возникла ошибка
    и описание ошибки.
    """
    now = datetime.now()
    dt_tm = now.strftime("%d.%b.%Y %H:%M:%S")

    err_str = '{date_time}    Function: {func:20}Error: {error}\n'.format(
        date_time=dt_tm,
        func=func.__name__,
        error=er
    )

    with open('function_errors.log', 'a') as out_file:
        out_file.write(err_str)


def logging(func: Callable) -> Callable:
    """
    Декоратор.
    Выводит на экран название функции и её документацию.
    Если возникают ошибки - пишет их в 'function_errors.log'
    (через вызов write_to_log_file())
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print('-' * 30)
        print('Название функции: {}()'.format(func.__name__))
        print('Документация:')
        print(func.__doc__)

        try:
            value = func(*args, **kwargs)

        except (IndexError, ZeroDivisionError) as er:
            write_to_log_file(func, er)
            return False

        return value

    return wrapped_func


@logging
def my_func() -> None:
    """
    Функция, которая просто выводит на экран фразу 'Какой-то текст'
    и значение счетчика index с 0 до 4.
    """
    print('Какой-то текст')

    for index in range(5):
        print('index = {index}'.format(index=index))


@logging
def fun_err_zero_div() -> None:
    """
    Функция выбрасывает исключение 'ZeroDivisionError:'
    """
    x = 5 / 0


@logging
def fun_err_index() -> None:
    """
    Функция выбрасывает исключение 'IndexError'
    """
    y = (1, 2, 3)
    x = y[3]


def main():
    my_func()
    fun_err_zero_div()
    fun_err_index()


main()
