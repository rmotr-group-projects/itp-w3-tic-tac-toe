from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.winning_player = None
        self.turn_count = 2

    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True
        else:
            return False

    def has_winner(self):
        for row in self.board.board:
            if row[0] == row[1] == row[2] != None:
                self.winning_player = row[0]
                return True
        for num in range(3):
            col = self.board.get_column(num)
            if col[0] == col[1] == col[2] != None:
                self.winning_player = col[0]
                return True
        for num in range(2):
            diag = self.board.get_diagonal(num)
            if diag[0] == diag[1] == diag[2] != None:
                self.winning_player = diag[0]
                return True
        return False        
                
    def is_tied(self):
        if self.has_winner() == True:
            return False
        for row in self.board.board:
            for col in row:
                if row[row.index(col)] == None:
                    return False
        return True            

    def get_winner(self):
        return self.winning_player

    def next_turn(self):
        if self.turn_count % 2 == 0:
            return self.player_1
        else:
            return self.player_2

    def move(self, player, row, col):
        if player != 'X' and player != 'O':
            raise InvalidMovementException
        elif self.is_finished() == True:
            raise InvalidMovementException
        elif self.next_turn() != player:
            raise InvalidMovementException
        elif (row > 2 or row < 0) or (col > 2 or col < 0):
            raise InvalidMovementException
        elif self.board.get_row(row)[col] != None:
            raise InvalidMovementException
        else:
            self.turn_count += 1
            return self.board.move(player,row,col)

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
        self.board = initial_board
        if initial_board == None:
            self.board = [[None,None,None],[None,None,None],[None,None,None]]

    def move(self, figure, row, col):
        self.board[row][col] = figure

    def __str__(self):
        for row in self.board:
            for col in row:
                if col == None:
                    row[row.index(col)] = "-"
        return BOARD_TEMPLATE.format(
            self.board[0][0],
            self.board[0][1],
            self.board[0][2],
            self.board[1][0],
            self.board[1][1],
            self.board[1][2],
            self.board[2][0],
            self.board[2][1],
            self.board[2][2])
            
    def get_row(self, row_number):
        return self.board[row_number]
            
    def get_column(self, col_number):
        column_result = []
        for index in self.board:
            column_result.append(index[col_number])
        return column_result    

    def get_diagonal(self, row_number):
        diagonal_result = []
        if row_number == 0:
            col_counter = 0
            for index in self.board:
                diagonal_result.append(index[col_counter])
                col_counter += 1
        if row_number == 1:
            col_counter = 2
            for index in self.board:
                diagonal_result.append(index[col_counter])
                col_counter -= 1
        return diagonal_result        
