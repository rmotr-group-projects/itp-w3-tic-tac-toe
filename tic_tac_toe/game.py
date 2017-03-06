from exceptions import InvalidMovementException 
class Game(object):
    def __init__(self, board, player_1="X", player_2="O"):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2 
        self.count = 1
        self.winner = None

    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True
        

    def has_winner(self):
        if self.get_winner() is not None:
            return True

    def is_tied(self):
        for i in self.board.board:
            for x in i:
               if x == None:
                   return False
        if not self.has_winner() :
            return True
        

    def get_winner(self):
        for i in range(3):
            if self.board.get_column(i) == ['X' , 'X' , 'X']:
                 self.winner = 'X'
            elif self.board.get_column(i) == ['O' , 'O' , 'O']:
                 self.winner = 'O'
            if self.board.get_row(i) == ['X' , 'X' , 'X']:
                 self.winner = 'X'
            elif self.board.get_row(i) == ['O' , 'O' , 'O']:
                 self.winner = 'O'
            if self.board.get_diagonal(0) == ['X' , 'X' , 'X']:
             self.winner = 'X'
            elif self.board.get_diagonal(0) == ['O' , 'O' , 'O']:
             self.winner = 'O'
            if self.board.get_diagonal(1) == ['X' , 'X' , 'X']:
             self.winner = 'X'
            elif self.board.get_diagonal(1) == ['O' , 'O' , 'O']:
             self.winner = 'O'
        return self.winner

    def next_turn(self):
        if self.count % 2 == 0:
            return self.player_2
        else:
            return self.player_1

    def move(self, player, row, col):
        if row > 2 or col >2 or row <0 or col <0:
            raise InvalidMovementException()
        elif player != self.next_turn():
            raise InvalidMovementException()
        elif self.is_finished():
            raise InvalidMovementException()
        elif player != 'X' and player != 'O':
            raise InvalidMovementException
        elif self.board.board[row][col] != None:
            raise InvalidMovementException
        #elif self.is_finished():
           # raise InvalidMovementException
        elif self.board.board[row][col] is None:
            self.board.board[row][col] = player
            self.count += 1

BOARD_TEMPLATE = """
     |     |
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
     |     |
"""


class Board(object):
    def __init__(self, initial_board=None):
        if initial_board is not None:
            self.board = initial_board
        else:
            self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
            ]
            
    def move(self, figure, row, col):
        self.board[row][col] = figure

    def __str__(self):
        return BOARD_TEMPLATE.format(
            self.board[0][0] or "-",
            self.board[0][1] or "-",
            self.board[0][2] or "-",
            
            self.board[1][0] or "-",
            self.board[1][1] or "-",
            self.board[1][2] or "-",
            
            self.board[2][0] or "-",
            self.board[2][1] or "-",
            self.board[2][2] or "-")  # .format()

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        return [self.board[0][col_number], self.board[1][col_number], self.board[2][col_number]]

    def get_diagonal(self, row_number):
        if row_number == 0:
            return [self.board[0][0], self.board[1][1], self.board[2][2]]
        elif row_number == 1:
                return [self.board[0][2], self.board[1][1], self.board[2][0]]
