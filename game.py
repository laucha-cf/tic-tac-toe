class TicTacToe:
    def __init__(self):
        self.board = [' ' for n in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+ ' |')


    @staticmethod
    def print_board_nums():
        number_board = [ [str(i) for i in range(j*3, (j+1)*3)] for j in range(3) ]
        for row in number_board:
            print('| '+' | '.join(row)+ ' |')

    def available_moves(self):
        #for i, spot in enumerate(self.board):
        #    if spot == ' ':
        #        moves.append(i)
        moves = [i for i,spot in enumerate(self.board) if spot == ' ']

        return moves
    
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[ row_ind*3 : (row_ind+1)*3 ]
        if all( [spot == letter for spot in row] ):
            return True

        #check column
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3) ]
        if all( [spot == letter for spot in col] ):
            return True

        #check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right
            if all( [spot == letter for spot in diagonal1] ):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] #right to left
            if all( [spot == letter for spot in diagonal2] ):
                return True

        return False

    

