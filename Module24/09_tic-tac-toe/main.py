from tictactoe import TicTacToe
from functions import get_x_y, get_first_player_index, change_gamer


def main():

    game = TicTacToe()
    current_gamer = get_first_player_index()
    game.print_header(current_gamer)

    for _ in range(9):

        game.print_field(current_gamer, True)
        x, y = get_x_y()
        game.put_figure(game.gamers[0][current_gamer][1], x, y)

        if game.check_win(game.gamers[0][current_gamer][1]):
            game.print_field(current_gamer, False)

            print('\nПобеда!\n{} выиграл!!! ({})'.format(
                game.gamers[0][current_gamer][0],
                game.figures[game.gamers[0][current_gamer][1]]
            ))

            return

        current_gamer = change_gamer(current_gamer)

    game.print_field(current_gamer, False)
    print('Боевая ничья.')


main()
