import random


def choice():
    print('Чем будете играть?')

    while True:
        print('(1: X, 2: O)')

        str_figure = input()
        if input_validate(str_figure):
            break

        print('Ошибка ввода, попробуйте еще раз (1 или 2).')

    return int(str_figure)


def in_range(num, min_value, max_value):
    if num in range(min_value, max_value + 1):
        return True

    else:
        return False


def is_digit(figure):
    try:
        int(figure)

    except ValueError:
        return False

    else:
        return True


def input_validate(figure):
    figure = figure.strip()

    if is_digit(figure) and in_range(int(figure), 1, 2):
        return True

    else:
        return False


def change_gamer(gamer):
    return 3 - gamer


def get_x_y():
    while True:
        str_coordinates = input()
        str_coordinates = str_coordinates.strip()

        if len(str_coordinates) == 3 and str_coordinates[1] == ' ':
            x, y = str_coordinates.split()

            if is_digit(x) and is_digit(y):
                if in_range(int(x), 1, 3) and in_range(int(y), 1, 3):
                    return int(x) - 1, int(y) - 1

        print('Нужно ввести 2 цифры (от 1 до 3) через пробел.')


def get_first_player_index():
    return random.randint(1, 2)
