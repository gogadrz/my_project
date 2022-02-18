import itertools


def main() -> None:
    # for code in range(10000):
    #     print('{:04d}'.format(code))

    # лучше так
    digits = range(10)
    pincode_vars = itertools.product(digits, repeat = 4)

    for var in pincode_vars:
        print(var)


if __name__ == '__main__':
    main()
