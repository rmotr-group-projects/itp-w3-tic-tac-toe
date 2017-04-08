from .exceptions import InvalidMovementException
import pdb
 
class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.current_player = player_1
        self.winner = None
        #....

    def is_finished(self):
        if self.has_winner() is True or self.is_tied() is True:
            return True
        return False

    def has_winner(self):
        if self.get_winner():
            return True
        else:
            return False

    def is_tied(self):
        if self.get_winner() is True:
           return False
        else:
            for x in self.board.board:
                for j in x:
                    if j is None:
                        return False
            return True
    

    def get_winner(self):
        #pdb.set_trace()
        for rows in range(3):
            X = 0
            O = 0
            for j in self.board.get_row(rows):
                if j == self.player_1:
                    X += 1
                if j == self.player_2:
                    O += 1
            if X == 3:
                return self.player_1
            elif O == 3:
                return self.player_2
        for columns in range(3):
            X = 0
            O = 0
            for j in self.board.get_column(columns):
                if j == self.player_1:
                    X += 1
                if j == self.player_2:
                    O += 1
            if X == 3:
                return self.player_1
            elif O == 3:
                return self.player_2
        for diagonal in range(2):    
            X = 0
            O = 0
            for j in self.board.get_diagonal(diagonal):
                if j == self.player_1:
                    X += 1
                if j == self.player_2:
                    O += 1
            if X == 3:
                return self.player_1
            elif O == 3:
                return self.player_2

# loop to see who the winner is
    def next_turn(self):
        return self.current_player

    def move(self, player, row, col):
    # start with player_1 then go to player_2
        # invalid = (
        #     row not in range(3) or
        #     col not in range(3) or
        #     player != self.current_player or
        #     self.is_finished is True or
        #     self.board[row][col] is not None
        #     )
        
        if row not in range(3):
            raise InvalidMovementException
        elif col not in range(3):
            raise InvalidMovementException
        elif player != self.current_player:
            raise InvalidMovementException
        elif self.board.board[row][col] is not None:
            raise InvalidMovementException
        elif player != self.next_turn():
            raise InvalidMovementException
        elif self.is_finished() is True:
            raise InvalidMovementException
        
        
        
        self.board.move(player, row, col)
        
        
        if player == self.player_1:
            self.current_player = self.player_2
        elif player == self.player_2:
            self.current_player = self.player_1
        


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
# l = [1, 2, 3, 4, 5]
# my_func(l[0], l[1], l[2], l[3], l[4])
# my_func(*l)
# PYTHONPATH=. py.test tests/testfile::TestCase::test_function_name

class Board(object):
    
    def __init__(self, initial_board=None):
        if initial_board is None:
            self.board = [
                [None, None, None],
                [None, None, None],
                [None, None, None]
            ]
        else:
            self.board = initial_board
# if the initial board equals none, create the board
#self.board[0][1]
#initial_board[0] = [ 'X', 'O', None]
    def move(self, figure, row, col):
        self.board[row][col] = figure
        

    def __str__(self):
        
        result = []
        for pos in self.board:
            for mark in pos:
                if mark is None:
                    result.append('-')
                else:
                    result.append(mark)
        return BOARD_TEMPLATE.format(*result)# .format()
        
        

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        column = []
        for row in self.board:#board_data_as_lists:
            column.append(row[col_number])
        return column


    def get_diagonal(self, row_number):
        diagonal = []
        row_increase = 0
        row_decrease = 2
        if row_number == 0:
            for row in self.board:
                diagonal.append(row[row_increase])
                row_increase += 1
        if row_number == 1:
            for row in self.board:
                diagonal.append(row[row_decrease])
                row_decrease -= 1
        return diagonal