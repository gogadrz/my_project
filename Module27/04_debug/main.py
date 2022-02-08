from typing import Callable, Any, Optional
import functools


def debug(func: Callable) -> Callable:
    """
    Декоратор debug.

    При каждом вызове декорируемой функции выводит её имя
    (вместе со всеми передаваемыми аргументами)
    и затем какое значение она возвращает.
    И после этого выводится результат её выполнения.
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:

        grown = False
        ages = 0

        result_str = 'Вызывается {name}('.format(
            name=func.__name__,
            args=args
        )

        if args and kwargs:
            for arg in args:
                result_str += '"{arg}'.format(arg=arg)
            result_str += '", '

            for key, value in kwargs.items():
                if key == 'age' and value > 25:
                    grown = True
                    ages = value
                result_str += '{key}={value}'.format(key=key, value=value)

        elif args:
            for arg in args:
                result_str += '"{arg}'.format(arg=arg)

            result_str += '"'

        else:
            for key, value in kwargs.items():
                if key == 'age' and value > 25:
                    grown = True
                    ages = value

                if isinstance(value, str):
                    result_str += '{key}="{value}", '.format(key=key, value=value)

                else:
                    result_str += '{key}={value}, '.format(key=key, value=value)

            result_str = result_str[:-2]

        result_str += ')'

        print(result_str)

        value = func(*args, **kwargs)

        print('\'{name}\' вернула значение \'{value}\''.format(
            name=func.__name__,
            value=value
        ))

        if grown:
            print('Ого, Миша! Тебе уже {ages} лет, ты вырос!\n'.format(ages=ages))
        else:
            print(value, '\n')

        return value

    return wrapped_func


@debug
def greeting(name: str, age: Optional[int]=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


def main():

    greeting("Том")
    greeting("Миша", age=100)
    greeting(name="Катя", age=16)


main()
