from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.current_player = "X"

    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True
        return False

    def has_winner(self):
        if self.get_winner():
            return True
        return False

    def is_tied(self):
        if self.get_winner():
            return False
        else: 
            for i in self.board.board_data_as_lists:
                for j in i:
                    if not j: 
                        return False
            return True

    def get_winner(self):
        things_to_check = []
        row_and_column = [0,1,2]
        diagonals = [0,1]
        
        for i in row_and_column:
            things_to_check.append(self.board.get_row(i))
            things_to_check.append(self.board.get_column(i))
            
        for e in diagonals:
            things_to_check.append(self.board.get_diagonal(e))
            
        for u in things_to_check: 
            for w in ("X", "O"):
                if u[0] == u[1] == u[2] == w:
                    return w
        return None
            
                    
    def next_turn(self):
        return self.current_player

    def move(self, player, row, col):
        if player != self.next_turn():
            raise InvalidMovementException
        elif row not in [0,1,2]:  
            raise InvalidMovementException
        elif col not in [0,1,2]:
            raise InvalidMovementException
        elif self.board.board_data_as_lists[row][col] != None:
            raise InvalidMovementException
        elif self.is_finished():
            raise InvalidMovementException

        self.board.move(player, row, col)
        if player == 'O':
            self.current_player = 'X' 
        else: 
            self.current_player = 'O'
       


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
        if not initial_board:
            self.board_data_as_lists = [ [initial_board]*3, [initial_board]*3, [initial_board]*3 ]
            
        else:
            self.board_data_as_lists = initial_board

    def move(self, figure, row, col):
        self.board_data_as_lists[row][col] = figure

    def __str__(self):
        finalList = []
        for i in self.board_data_as_lists:
            for j in i:
                if j == None:
                    finalList.append("-")
                else:
                    finalList.append(j)
                        
        return BOARD_TEMPLATE.format(*finalList)
            
            
    def get_row(self, row_number):
        return self.board_data_as_lists[row_number]

    def get_column(self, col_number):
        column = []
        for row in self.board_data_as_lists:
            column.append(row[col_number])
        return column

    def get_diagonal(self, row_number):
        if row_number == 0:
            positions = [ (0, 0), (1, 1), (2, 2) ]
            
        elif row_number == 1:
            positions = [ (0, 2), (1, 1), (2, 0) ]
        
        diagonal = []
        for position in positions:
            row = position[0]
            col = position[1]
            diagonal.append(self.board_data_as_lists[row][col])
        return diagonal
