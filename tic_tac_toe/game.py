from .exceptions import InvalidMovementException 


class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = 'X'
        self.player_2 = 'O'
        self.next_player = self.player_1

    def is_finished(self):
        if self.get_winner() is not None:
            return True
        if self.is_tied() is not False:
            return True

    def has_winner(self):
        if self.get_winner() is not None:
            return True
    

    def is_tied(self):
        for i in range (3):
            for j in range(3):
                if self.board.board[i][j] == None:
                    return False
        return True
        

    def get_winner(self):
        for i in range (3):
            if self.board.board[i][0] == self.board.board[i][1] == self.board.board[i][2] != None:
                return self.board.board[i][0]
        for i in range (3):
            if self.board.board[0][i] == self.board.board[1][i] == self.board.board[2][i] != None:
                return self.board.board[0][i]
        if self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2] != None:
            return self.board.board[0][0]
        elif self.board.board[0][2] == self.board.board[1][1] == self.board.board[2][0] != None:
            return self.board.board[0][2]

    def next_turn(self):
        return self.next_player
        

    def move(self, player, row, col):
        if row > 2 or row < 0:
            raise InvalidMovementException
        if col > 2 or col < 0:
            raise InvalidMovementException
        if self.get_winner():
            raise InvalidMovementException
        if self.next_turn() != player:
            raise InvalidMovementException
        if player != 'X' and player != 'O':
            raise InvalidMovementException
        if self.board.board[row][col] == None:
            self.board.board[row][col] = player
        else:
            raise InvalidMovementException
        
        if player == self.player_1:
            self.next_player = self.player_2
        else:
            self.next_player = self.player_1
        
        
        



    BOARD_TEMPLATE = """
     |     |
  {}  | {}  |  {}
_____|_____|_____
     |     |
  {}  |  {} |  {}
_____|_____|_____
     |     |
  {}  |  {} |  {}
     |     |
"""


class Board(object):
    def __init__(self, initial_board=None):
        if initial_board is not None:
            self.board = [initial_board[0], initial_board[1], initial_board[2]]
        else:
            self.board = [[initial_board, initial_board, initial_board], 
                    [initial_board, initial_board, initial_board], 
                    [initial_board, initial_board, initial_board]]




    def move(self, figure, row, col):
        self.board[row][col] = figure
         
    #placing the figure in whatever row and column we give it
    

    def __str__(self):
       return BOARD_TEMPLATE.format(
	    self.board[0][0] or '-',
	    self.board[0][1] or '-',
    	self.board[0][2] or '-',
	
    	self.board[1][0] or '-',
    	self.board[1][1] or '-',
    	self.board[1][2] or '-',
	
    	self.board[2][0] or '-',
    	self.board[2][1] or '-',
    	self.board[2][2] or '-',
	
        )

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        return [self.board[0][col_number], self.board[1][col_number], self.board[2][col_number]]

    def get_diagonal(self, row_number):
        if row_number == 0: 
            return [self.board[0][0], self.board[1][1], self.board[2][2]]
        elif row_number == 1:
            return [self.board[0][2], self.board[1][1], self.board[2][0]]
