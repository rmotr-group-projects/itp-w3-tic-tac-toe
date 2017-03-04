from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.turns = 0
        self.winner = None
        

    def is_finished(self):
        self.has_winner()
        if self.winner != None or self.is_tied():
          
            return True
        else:
            return False
            
    def has_winner(self):
        
        for rows in range(3):
        
            x = 0
            o = 0
            
            for i in self.board.get_row(rows):
                if i == self.player_1: # X
                    x += 1
                elif i == self.player_2: # O
                    o += 1
                
                if x == 3:
                    self.winner = self.player_1
                elif o == 3:
                    self.winner = self.player_2
                    
        for columns in range(3):
        
            x = 0
            o = 0
            
            for i in self.board.get_column(columns):
                if i == self.player_1: # X
                    x += 1
                elif i == self.player_2: # O
                    o += 1
                
                if x == 3:
                    self.winner = self.player_1
                elif o == 3:
                    self.winner = self.player_2
                    
        for diag in range(2):
        
            x = 0
            o = 0
            
            for i in self.board.get_diagonal(diag):
                if i == self.player_1: # X
                    x += 1
                elif i == self.player_2: # O
                    o += 1
                
                if x == 3:
                    self.winner = self.player_1
                elif o == 3:
                    self.winner = self.player_2
                    
        if self.winner != None:
            return True

          

    def is_tied(self):
        for i in self.board.board:
            for x in i:
                if x == None:
                    return False
        
        if self.has_winner():
            return False
        else:
            return True
      

    def get_winner(self):
        return self.winner

    def next_turn(self):
        if self.turns % 2 == 0:
            return self.player_1
        else:
            return self.player_2

    def move(self, player, row, col):
        if row > 2 or row < 0 or col > 2 or col < 0:
            raise InvalidMovementException()
        elif self.board.board[row][col] != None:
            raise InvalidMovementException()
        elif self.is_finished():
            raise InvalidMovementException()
        elif self.is_tied():
            raise InvalidMovementException()
        elif self.has_winner():
            raise InvalidMovementException()
        elif self.next_turn() != player:
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
        
        if initial_board:
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
        results = []
        for i in self.board:
            for x in i:
                if x is None:
                    results.append('-')
                else:
                    results.append(x)
        return BOARD_TEMPLATE.format(*results)

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        return [
        self.board[0][col_number],
        self.board[1][col_number],
        self.board[2][col_number]
        ]

    def get_diagonal(self, diagonal_num):
        if diagonal_num == 0:
            return [self.board[0][0],self.board[1][1],self.board[2][2]]
        elif diagonal_num == 1:
        
            return [self.board[0][2],self.board[1][1],self.board[2][0]]

    
