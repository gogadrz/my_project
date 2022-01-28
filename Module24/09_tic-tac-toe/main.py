import random

from ttt import TicTacToe


def input_validate(figure):
    figure = figure.strip()
    try:
        figure = int(figure)
    except ValueError:
        return False
    else:
        if figure in (1, 2):
            return True
        else:
            return False


def initialize(gamers):

    figure_interpreter = {1: 'X', 2: 'O'}

    for i_gamer in range(1, 3):

        print(i_gamer, 'игрок. ', end='')
        name = input('Введите имя: ')

        if name == '':
            name = 'Player' + str(i_gamer)

        if i_gamer == 1:
            print('Чем будете играть?')

            while True:
                print('1: X, 2: O')
                figure = input()
                if input_validate(figure):
                    break
                print('Ошибка ввода, попробуйте еще раз (1 или 2).')
        else:
            figure = (3 - int(figure))

        gamers[0][i_gamer] = [name, int(figure)]

    for i_gamer in range(1, 3):
        print('{} играет {}'.format(
            gamers[0][i_gamer][0],
            figure_interpreter[gamers[0][int(i_gamer)][1]]
        ))
    return


def main():
    gamers = [dict()]
    initialize(gamers)

    game = TicTacToe()
    game.print_field()

    current_gamer = random.randint(1, 2)
    print('Первым выпало ходить {}'.format(gamers[0][current_gamer][0]))

    for _ in range(2):
        print('Введите координаты через пробел (горизонталь вертикаль)')
        x, y = input().split()

        game.set_figure(1 ,int(x) - 1, int(y) - 1)
        game.print_field()




    # print(gamers)

    # game = TicTacToe()
    # game.print_field()
    #
    # game.set_figure('x', 0, 2)
    # game.print_field()
    #
    # game.set_figure('o', 0, 2)
    # game.print_field()


main()
