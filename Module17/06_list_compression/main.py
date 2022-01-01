import random


def main():
    total_digits = int(input('Кол-во чисел в списке: '))

    digits_list = [random.randint(0, 2) for _ in range(total_digits)]
    print('Список до сжатия:', digits_list)

    count = digits_list.count(0)
    while count > 0:
        digits_list.remove(0)
        count -= 1

    print('Список после сжатия:', digits_list)


if __name__ == '__main__':
    main()
