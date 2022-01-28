from functions import get_x_y, choice


class TicTacToe:
    figures = {0: '.', 1: 'x', 2: 'o', 'x': 1, 'o': 2}
    gamers = [dict()]

    def __init__(self):
        self.game_field = [[0 for _ in range(3)] for _ in range(3)]
        self.get_user_name()
        return

    def print_field(self, current_gamer, print_footer):

        print('\n\n')
        print('    1 2 3')
        print('   ', '_' * 7, sep = '')

        for j in range(3):
            print(j + 1, '| ', end = '')
            for i in range(3):
                print(self.figures[self.game_field[i][j]], end = ' ')
            print('|')

        print('   ', '-' * 7, ' ', sep = '')

        if print_footer:
            print('{}, Ваш ход. ({})'.format(
                self.gamers[0][current_gamer][0],
                self.figures[self.gamers[0][current_gamer][1]]
            ))
            print('Введите координаты через пробел (горизонталь, вертикаль)')

        return

    def set_figure(self, figure, x, y):

        if self.check_cell(x, y):
            # self.game_field[x][y] = self.figures[figure]
            self.game_field[x][y] = figure
            return True

        else:
            return False

    def check_cell(self, x, y):
        if self.game_field[x][y] == 0:
            return True

        else:
            return False

    def get_user_name(self):
        last_user_name = ''

        for i_gamer in range(1, 3):

            print('\nИгрок №{} '.format(i_gamer))
            name = input('Введите имя: ').title()

            if name == '':
                name = 'Player ' + str(i_gamer)

            elif name == last_user_name:
                name += '2'

            if i_gamer == 1:
                figure = choice()

            else:
                figure = 3 - self.gamers[0][i_gamer - 1][1]

            self.gamers[0][i_gamer] = [name, figure]
            last_user_name = name

    def put_figure(self, figure, x, y):
        while True:
            if self.set_figure(figure, x, y):
                return True

            print('Эта ячейка занята')
            x, y = get_x_y()

    def print_header(self, first_player):
        for i_gamer in range(1, 3):
            print('Игрок: {} играет - \'{}\''.format(self.gamers[0][i_gamer][0],
                                                     self.figures[self.gamers[0][int(i_gamer)][1]]))

        print('\nЖребий брошен')
        print('Начнет игру - {}'.format(self.gamers[0][first_player][0]))
        print()

        print('-' * 30)
        return

    def check_x_y(self, figure, x, y):
        if self.game_field[x][y] == figure:
            return True
        else:
            return False

    def check_win(self, figure):
        if all([self.check_x_y(figure, index, index) for index in range(3)]):
            # print('\nBack diagonal Win!')
            return True

        if all([self.check_x_y(figure, 2 - index, index) for index in range(3)]):
            # print('\nDiagonal Win!')
            return True

        for i in range(3):
            if all([self.check_x_y(figure, index, i) for index in range(3)]):
                # print('\nHorizontal line {} Win!'.format(i))
                return True

        for i in range(3):
            if all([self.check_x_y(figure, i, index) for index in range(3)]):
                # print('\nVertical line {} Win!'.format(i))
                return True

        return False
