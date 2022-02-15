from typing import List
from functools import reduce


def main() -> None:

    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

    print('Первый список:', list(map(lambda x: round(x ** 3, 3), floats)))

    print('Второй список:', list(filter(lambda y: len(y) >= 5, names)))

    print('Третий список:', [reduce(lambda a, b: a * b, [i for i in numbers])])


if __name__ == '__main__':
    main()
