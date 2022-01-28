class TicTacToe:

    figures = {0: '.', 1: 'x', 2: 'o', 3: 'X', 4: 'O',
               '.': 0, 'x': 1, 'o': 2, 'X': 3, 'O': 4}

    def __init__(self):
        self.game_field = [[0 for _ in range(3)] for _ in range(3)]
        return

    def print_field(self):

        print('\n\n')
        print('    1 2 3')
        print('   ', '_' * 7, sep='')

        for j in range(3):
            print(j + 1, '| ', end='')
            for i in range(3):
                print(self.figures[self.game_field[i][j]], end=' ')
            print('|')

        print('   ', '-' * 7, ' ', sep='')
        return

    def set_figure(self, figure, x, y):

        if self.check_cell(x, y):
            self.game_field[x][y] = self.figures[figure]
            return True

        else:
            return False

    def check_cell(self, x, y):
        if self.game_field[x][y] == 0:
            return True

        else:
            return False
