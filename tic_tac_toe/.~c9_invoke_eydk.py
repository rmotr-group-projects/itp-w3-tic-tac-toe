from .exceptions import InvalidMovementException

class Game(object):
    
    def __init__(self, board, player_1, player_2):
        self.board = board  # <-- self.board is an instance of your board class. Not the list of lists from your board class. Refer to lines 22-33 in test-game.py
        self.player_1 = player_1
        self.player_2 = player_2
        self.next_player = player_1

    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True
        return False

    def has_winner(self):
        if self.get_winner() is not None:
            return True

    def is_tied(self):
        for row in self.board.board:
            if None in row:
                return False
        return True

    def get_winner(self):
        for row in self.board.board:
            if row == ['X', 'X', 'X']:
                return self.player_1
            if row == ['O', 'O', 'O']:
                return self.player_2
            
        if self.board.get_column():
            
     
            
        if self.board.get_diagonal():
            

    def next_turn(self):


    def move(self, player, row, col):
        if player != self.player_1 or player != self.player_2:
            raise InvalidMovementException()
        if row > 2 or row < 0:
            raise InvalidMovementException()
        if col > 2 or col < 0:
            raise InvalidMovementException()
        if self.board[row][col] is not None:
            raise InvalidMovementException()
        if self.is_finished():
            raise InvalidMovementException()
        else:
            self.board.move(player, row, col)
            player =self.next_player


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
        if initial_board is None:
            self.board =    [[None, None, None], 
                             [None, None, None], 
                             [None, None, None]
                            ]
            #self.board: [row_0], [row_1], [row_2]
        else:
            self.board = initial_board


    def move(self, figure, row, col):
        self.board[row][col] = figure
        

    def __str__(self):
        return BOARD_TEMPLATE.format(self.board[0][0] or '-', self.board[0][1] or '-', self.board[0][2] or '-', 
                self.board[1][0] or '-', self.board[1][1] or '-', self.board[1][2] or '-', 
                self.board[2][0] or '-', self.board[2][1] or '-', self.board[2][2] or '-')


    def get_row(self, row_number):
        return self.board[row_number]


    def get_column(self, col_number):
        col_list = []
        for list in self.board:
            col_list.append(list[col_number])
        return col_list


    def get_diagonal(self, row_number):
        diag_list = []
        if row_number == 0:
            column_position = 0
            for list in self.board:
                diag_list.append(list[column_position])
                column_position += 1
            return diag_list
        elif row_number == 1:
            column_position = 2
            for list in self.board:
                diag_list.append(list[column_position])
                column_position -= 1
            return diag_list