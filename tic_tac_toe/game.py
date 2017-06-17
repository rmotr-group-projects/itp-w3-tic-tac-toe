from .exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.next_player = self.player_1
                                            
    def is_finished(self):
        if self.has_winner() == True or self.is_tied() == True:
            return True
        else:
            return False

    def has_winner(self):
        if self.get_winner():
            return True
        else:
            return False

    def is_tied(self):
        for space in range(0,3):
            if None in self.board.initial_board[space]:
                return False
        return True 
                
    def get_winner(self):
        winner_X = ['X', 'X', 'X']
        winner_O = ['O', 'O' , 'O']
        
        for space in range(0, 3):
            if self.board.get_row(space) == winner_X or self.board.get_column(space) == winner_X or self.board.get_diagonal(space) == winner_X:
                return 'X'
        for space in range(0, 3):
             if self.board.get_row(space) == winner_O or self.board.get_column(space) == winner_O or self.board.get_diagonal(space) == winner_O:
                return 'O'
        return None
   
    def next_turn(self):
        return self.next_player

    def move(self, player, row, col):
        if (player != self.next_player or row not in range(0,3)
                                        or col not in range(0,3) 
                                        or self.board.initial_board[row][col] 
                                         or self.is_finished() == True):
            raise InvalidMovementException()
        
        self.board.initial_board[row][col] = player
        
        if player == 'X':
            self.next_player = 'O'
        else:
            self.next_player = 'X'

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

    def __str__(self):
        return BOARD_TEMPLATE.format(self.initial_board[0][0] or '-', self.initial_board[0][1] or '-', self.initial_board[0][2] or '-',
                                     self.initial_board[1][0] or '-', self.initial_board[1][1] or '-', self.initial_board[1][2] or '-',
                                     self.initial_board[2][0] or '-', self.initial_board[2][1] or '-', self.initial_board[2][2] or '-'
                                    )
                                     

    def get_row(self, row_number):
        return self.initial_board[row_number]

    def get_column(self, col_number):
        column = []
        for space in range(0,3):
            column.append(self.initial_board[space][col_number])
        return column

    def get_diagonal(self, row_number):
        diagonal = []
        for space in range(0,3):
            if row_number == 0:
                diagonal.append(self.initial_board[row_number+space][space])
        if row_number == 1:
            diagonal.append(self.initial_board[0][2])
            diagonal.append(self.initial_board[1][1])
            diagonal.append(self.initial_board[2][0])
        return diagonal
