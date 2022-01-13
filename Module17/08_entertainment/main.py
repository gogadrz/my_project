import random


def generate_range(stick_cnt):
    left = random.randint(0, stick_cnt - 1)
    right = random.randint(0, stick_cnt - 1)
    while left == right:
        right = random.randint(0, stick_cnt - 1)

    if left > right:
        left, right = right, left
    return left, right


def print_result(result_list):
    print('\nРезультат: ', end='')
    for i_result in result_list:
        if i_result == 1:
            print('I', end='')
        else:
            print('.', end='')
    return


def make_throws(throw_total, stick_total, throw_list):
    for i_throw in range(throw_total):
        l_index, r_index = generate_range(stick_total)
        throw_list.append(list([l_index, r_index]))
    return


def change_stick_list(stick_list, throw_list, throw_total):
    for i_throw in range(throw_total):
        for i_points in range(throw_list[i_throw][0], throw_list[i_throw][1] + 1):
            stick_list[i_points] = '.'
    return


def print_throws(throw_total, throw_list, stick_list):
    for i_throw in range(throw_total):
        print('Бросок ', i_throw + 1, '. Сбиты палки с номера ', throw_list[i_throw][0] + 1, sep='')
        print('по номер', throw_list[i_throw][1] + 1)
        change_stick_list(stick_list, throw_list, throw_total)
    return


def main():
    debug = False
    stick_total = int(input('Кол-во палок: '))
    throw_total = int(input('Кол-во бросков: '))

    stick_list = [1 for _ in range(stick_total)]
    throw_list = []

    make_throws(throw_total, stick_total, throw_list)

    if debug:
        print(stick_list)
        print(throw_list)

    print_throws(throw_total, throw_list, stick_list)
    print_result(stick_list)


if __name__ == '__main__':
    main()
