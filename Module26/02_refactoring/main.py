from collections.abc import Iterable


def seek(looking_number: int) -> Iterable[int, int, int]:
    list_1 = [2, 5, 7, 10]
    list_2 = [3, 8, 4, 9]

    for x in list_1:
        for y in list_2:
            result = x * y
            yield x, y, result
            if result == looking_number:
                print('Found!!!')
                return


def main():
    value = seek(looking_number=56)
    for x, y, result in value:
        print(x, y, result)


main()
