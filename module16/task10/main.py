def check_palindrom(num_list):
    for index in range(len(num_list) // 2):
        back_index = -index - 1
        if num_list[index] != num_list[back_index]:
            return False

    return True


def print_list(message, prt_list):
    print(message, end='')
    for i_prt in prt_list:
        print(i_prt, end=' ')
    print()


def main():
    num_cnt = int(input('Кол-во чисел: '))
    num_list = []
    buffer = []
    done = False

    for _ in range(num_cnt):
        num = int(input('Число: '))
        num_list.append(num)

    print_list('\nПоследовательность: ', num_list)

    done = check_palindrom(num_list)
    while not done:
        buffer.append(num_list[0])
        num_list.pop(0)
        done = check_palindrom(num_list)

    print('Нужно приписать чисел:', len(buffer))

    buffer.reverse()
    print_list('Сами числа: ', buffer)


if __name__ == '__main__':
    main()
