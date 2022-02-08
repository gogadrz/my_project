import time


class Timer:
    def __init__(self) -> None:
        print('Время работы кода')
        self.__start = 0

    def __enter__(self) -> 'Timer':
        self.__start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.__start)
        print()

        # что бы не вылетела по ошибке TypeError
        if exc_type is TypeError:
            return True
        # или просто
        return True


with Timer() as t1:
    print('Part first')
    val_1 = 100 * 100 ** 1000000

with Timer() as t2:
    print('Part second')
    val_2 = 100 * 200 ** 1000000

with Timer() as t3:
    print('Part third')
    val_3 = 100 * 300 ** 1000000
