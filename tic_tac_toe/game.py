from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.turns = 0
    
    
    def is_finished(self):
        if self.is_tied() or self.has_winner():
            return True
        else:
            return False

    def has_winner(self):
        if self.get_winner() != None:
            return True
        else:
            return False

    def is_tied(self):
        for i in self.board.board:
            for j in i:
                if j == None:
                    return False
        if self.has_winner():
            return False
        else:
            return True
                
            
    def get_winner(self):
        for rows in range(3):
            x = 0
            o = 0
            for i in self.board.get_row(rows):
                if i == self.player_1:
                    x +=1
                elif i  == self.player_2:
                    o += 1
                    
                if x == 3:
                    return self.player_1
                elif o == 3:
                    return self.player_2
                    
        for columns in range(3):
            x = 0
            o = 0
            for i in self.board.get_column(columns):
                if i == self.player_1:
                    x +=1
                elif i  == self.player_2:
                    o += 1
                if x == 3:
                    return self.player_1
                elif o == 3:
                    return self.player_2
                    
        for diag in range(2):
            x = 0
            o = 0
            for i in self.board.get_diagonal(diag):
                if i == self.player_1:
                    x +=1
                elif i  == self.player_2:
                    o += 1
                if x == 3:
                    return self.player_1
                elif o == 3:
                    return self.player_2
                    
    def next_turn(self):
        if self.turns % 2 == 0:
            return self.player_1
        else:
            return self.player_2

    def move(self, player, row, col):
        if row > 2 or col > 2  or row  < 0 or col < 0:
            raise InvalidMovementException()
            
        elif player != 'X' and player != 'O':
            raise InvalidMovementException()
            
        elif self.board.board[row][col] != None:
            raise InvalidMovementException()
            
        elif player != self.next_turn():
            raise InvalidMovementException()
            
        elif self.is_finished():
            raise InvalidMovementException()
            
        elif self.is_tied():
            raise InvalidMovementException()
            
        else:
            self.board.board[row][col] = player
            self.turns += 1


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
            initial_board = [[None, None, None], [None, None, None], [None, None, None]]
        self.board = initial_board
        self.string_represent = [self.board[0][0] if self.board[0][0] is not None else '-', 
                            self.board[0][1] if self.board[0][1] is not None else '-',
                            self.board[0][2] if self.board[0][2] is not None else '-',
                            self.board[1][0] if self.board[1][0] is not None else '-',
                            self.board[1][1] if self.board[1][1] is not None else '-',
                            self.board[1][2] if self.board[1][2] is not None else '-',
                            self.board[2][0] if self.board[2][0] is not None else '-',
                            self.board[2][1] if self.board[2][1] is not None else '-',
                            self.board[2][2] if self.board[2][2] is not None else '-',
                            ]
        self.BOARD_TEMPLATE = BOARD_TEMPLATE.format(*self.string_represent)
    def __str__(self):
            return self.BOARD_TEMPLATE
            
    def move(self, figure, row, col):
        self.board[row][col] = figure
        
    
    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        return [self.board[0][col_number], self.board[1][col_number], self.board[2][col_number]]
        
    def get_diagonal(self, diagonal):
        if diagonal == 0:
            return [self.board[0][0], self.board[1][1], self.board[2][2]]
        else:
            return [self.board[0][2], self.board[1][1], self.board[2][0]]

