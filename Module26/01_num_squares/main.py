from collections.abc import Iterable


class ClassIterator:

    def __init__(self, limit: int):
        self.__limit = limit
        self.__current = 0

    def __iter__(self):
        return self

    def __next__(self) -> Iterable[int]:
        self.__current += 1
        if self.__current <= self.__limit:
            return self.__current ** 2
        else:
            raise StopIteration()


def fun_square(limit: int) -> Iterable[int]:
    for index in range(1, limit + 1):
        yield index ** 2


def main():
    n_number = int(input('Введите число N: '))

    gen_exp_square = (num ** 2 for num in range(1, n_number + 1))

    print('\nГенераторное выражение:')
    for item in gen_exp_square:
        print(item, end=' ')
    print()

    print('\nФункция генератор:')
    square_gen = fun_square(limit=n_number)

    for item in square_gen:
        print(item, end=' ')
    print()

    print('\nКласс-итератор:')
    square_iter = ClassIterator(limit=n_number)
    for item in square_iter:
        print(item, end=' ')
    print()


main()
