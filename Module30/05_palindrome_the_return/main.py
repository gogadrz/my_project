import collections


def can_be_poly(in_string: str) -> bool:
    counter = 0
    sym = collections.Counter(list(in_string))

    for _, value in sym.items():
        if value % 2 != 0:
            counter += 1

        if counter > 1:
            return False

    return True


def main() -> None:
    print(can_be_poly('ababc'))
    print(can_be_poly('abbbc'))


if __name__ == '__main__':
    main()
