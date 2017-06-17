from .exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.next_player = player_1

    def is_finished(self):
        if self.has_winner() == True:
            return True
        elif self.is_tied() == True:
            return True
        else: 
            return False
            
    def has_winner(self):
        if self.get_winner() == 'X':
            return True
        elif self.get_winner() == 'O':
            return True
        else:
            return False
            
    def is_tied(self):
        for turkey in self.board.initial_board:
            for jason in turkey:
                if jason is None:                   # very good variable names
                    return False
        return True

    def get_winner(self):
        winner_X = ['X', 'X', 'X']
        winner_O = ['O', 'O', 'O']
        
        for i in range(3):
            if self.board.get_row(i) == winner_X or self.board.get_column(i) == winner_X:
                return 'X'
        for i in range(2):
            if self.board.get_diagonal(i) == winner_X:
                return 'X'
        for i in range(3):
            if self.board.get_row(i) == winner_O or self.board.get_column(i) == winner_O:
                return 'O'
        for i in range(2):        
            if self.board.get_diagonal(i) == winner_O:
                return 'O'
        return None
            
    def next_turn(self):
        return self.next_player

    def move(self, player, row, col):
        if (row < 0 or row > 2) or (col < 0 or col > 2):
            raise InvalidMovementException()
        elif player != self.next_player:
            raise InvalidMovementException()
        elif self.is_finished():
            raise InvalidMovementException()
        elif self.board.initial_board[row][col] != None:
            raise InvalidMovementException()
        self.board.move(player, row, col)
        if player == 'O': 
            self.next_player = 'X'
        else:
            self.next_player = 'O'


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
        if initial_board == None:
            self.initial_board = [[None, None, None],
                                  [None, None, None],
                                  [None, None, None]]
        else: 
            self.initial_board = initial_board

    def move(self, figure, row, col):
        self.initial_board[row][col] = figure
        #rows and col are 0, 1, 2 and figures are 'x' and 'o'

    def __str__(self):
        #return BOARD_TEMPLATE  # .format()
        return BOARD_TEMPLATE.format(self.initial_board[0][0] or '-', self.initial_board[0][1] or '-', self.initial_board[0][2] or '-',
                                     self.initial_board[1][0] or '-', self.initial_board[1][1] or '-', self.initial_board[1][2] or '-',
                                     self.initial_board[2][0] or '-', self.initial_board[2][1] or '-', self.initial_board[2][2] or '-')
        
    def get_row(self, row_number):
        return self.initial_board[row_number]

    def get_column(self, col_number):
        # return self.initial_board[col_number]
        if col_number == 0:
            col_0 = [self.initial_board[0][0], self.initial_board[1][0], self.initial_board[2][0]]
            return col_0
        elif col_number == 1:
            col_1 = [self.initial_board[0][1], self.initial_board[1][1], self.initial_board[2][1]]
            return col_1
        elif col_number == 2:
            col_2 = [self.initial_board[0][2], self.initial_board[1][2], self.initial_board[2][2]]
            return col_2    
        
    def get_diagonal(self, row_number):
        if row_number == 0:
            diagonal_0 = [self.initial_board[0][0], self.initial_board[1][1], self.initial_board[2][2]]
            return diagonal_0
        elif row_number == 1:
            diagonal_1 = [self.initial_board[0][2], self.initial_board[1][1], self.initial_board[2][0]]
            return diagonal_1
                
            # AssertionError: Lists differ: [None, 'X', 'X'] != ['X', 'X', None]