class TicTacToe:

    figures = {0: 'empty', 1: 'x', 2: 'o', 3: 'x_win', 4: 'o_win',
               'empty': 0, 'x': 1, 'o': 2, 'x_win': 3, 'o_win': 4}

    def __init__(self):
        self.game_field = [[0 for _ in range(3)] for _ in range(3)]

    def print_field(self):
        for j in range(3):
            for i in range(3):
                print(self.game_field[i][j], end = ' ')
            print()

    def set_figure(self, figure, x, y):
        if self.check_cell(int(x), int(y)):
            self.game_field[int(x)][int(y)] = self.figures[figure]
        else:
            print('Ячейка занята!')

    def check_cell(self, x, y):
        if self.print_field[x][y] == 0:
            return True
        else:
            return False


game = TicTacToe()
game.print_field()
game.set_figure('x', 0, 2)
game.print_field()
