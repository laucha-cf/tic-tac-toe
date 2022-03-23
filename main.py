from game import TicTacToe
from player import *

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print('')

            letter = 'O' if letter == 'X' else 'X'
            #if letter == 'X':
            #    letter = 'O'
            #else:
            #    letter = 'X'