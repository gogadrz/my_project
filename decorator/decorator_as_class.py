from typing import Callable
import functools


class CountCalls:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs) -> Callable:
        self.num_calls += 1
        print('Вызов номер {num} функции {fun}'.format(
            num=self.num_calls,
            fun=self.func.__name__
        ))

        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')


say_hello()
say_hello()
say_hello()
print(say_hello.num_calls)

