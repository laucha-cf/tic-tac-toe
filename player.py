import random
import math

class Player:
    def __init__(self, p_letter):
        #letter is x or o
        self.letter = p_letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, p_letter):
        super().__init__(p_letter)
    
    def get_move(self, game):
        square = random.choice( game.available_moves() )
        return square


class HumanPlayer(Player):
    def __init__(self, p_letter):
        super().__init__(p_letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'{self.letter}´s turn. Input move (0-9): ')
            try:
                #trying to cast de answer to a integer
                #checking if the value is an valid move
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
