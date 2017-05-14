from exceptions import InvalidMovementException


class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.next_player = self.player_1 #needs another option for 'next player'

    def is_finished(self):
        
        if (self.has_winner() == False and 
        self.is_tied() == False):
            return False
        else:
            return True
            

    def has_winner(self):
        
        if self.get_winner() is None:
            return False
        else:
            return True
        
        

    def is_tied(self):
       
        for x in range(3):
            for o in range(3):
                if self.board.initial_board[x][o] is None:
                    return False
        return True

    def get_winner(self):
        x_win = ['X', 'X', 'X']
        o_win = ['O', 'O', 'O']
        
        for x in range(3):
            if (self.board.get_row(x) == x_win or
            self.board.get_column(x) == x_win or
            self.board.get_diagonal(x) == x_win):
                return 'X'
                
        for o in range(3):
            if (self.board.get_row(o) == o_win or
            self.board.get_column(o) == o_win or
            self.board.get_diagonal(o) == o_win):
                return 'O'
        
        return None


    def next_turn(self):
        
        return self.next_player #line 17 test_game.py
        

    def move(self, player, row, col):
        
        if player != self.next_player:
            raise InvalidMovementException()
            
        elif row not in range(3) or col not in range(3):
            raise InvalidMovementException()
        
        elif self.board.initial_board[row][col] != None:
            raise InvalidMovementException()
        
        elif self.is_finished() is True:
            raise InvalidMovementException()
            
        elif self.next_player == self.player_1:
            self.board.move(player, row, col)
            self.next_player = self.player_2
        elif self.next_player == self.player_2:
            self.board.move(player, row, col)
            self.next_player = self.player_1
        
        else:
            self.board.move(player, row, col)
        
        if player == "X":
            self.next_player = "O"
        elif player == "O":
            self.next_player = "X"
            


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
        
        #need to self.initial_board = initial_board ??
        
        if initial_board is None:
            self.initial_board = [[None, None, None], 
                                [None, None, None], 
                                [None, None, None]]
        else:
            self.initial_board = initial_board
                                

    def move(self, figure, row, col):
        
        self.initial_board[row][col] = figure
        

    def __str__(self):
        return BOARD_TEMPLATE.format(
        self.initial_board[0][0] or '-', 
        self.initial_board[0][1] or '-', 
        self.initial_board[0][2] or '-', 
        self.initial_board[1][0] or '-', 
        self.initial_board[1][1] or '-', 
        self.initial_board[1][2] or '-', 
        self.initial_board[2][0] or '-', 
        self.initial_board[2][1] or '-', 
        self.initial_board[2][2] or '-')
        

    def get_row(self, row_number):
        
        return self.initial_board[row_number] 


    def get_column(self, col_number):
        
        return [self.initial_board[i][col_number] 
        for i, item in enumerate(self.initial_board)]


    def get_diagonal(self, row_number):
        
        diag = []
        
        if row_number == 0:
            for spot, item in enumerate(self.initial_board):
                diag.append(self.initial_board[spot][spot])
                
        elif row_number == 1:
            diag.append(self.initial_board[0][2])
            diag.append(self.initial_board[1][1]) 
            diag.append(self.initial_board[2][0])
        
        return diag
            
