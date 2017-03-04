from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.turns = 0
        

    def get_winner(self):
        for rows in range(3):
            x = 0
            o = 0
            for i in self.board.get_row(rows):
                if i == self.player_1:
                    x +=1
                elif i == self.player_2:
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
                    x += 1
                elif i == self.player_2:
                    o += 1
                    
            if x == 3:
                return self.player_1
            elif o == 3:
                return self.player_2
        

        for diagonal in range(3):
            x = 0
            o = 0
            for i in self.board.get_diagonal(diagonal):
                if i == self.player_1:
                    x += 1
                elif i == self.player_2:
                    o += 1

            if x == 3:
                return self.player_1
            elif o == 3:
                return self.player_2
                    


    def has_winner(self):
        if self.get_winner() == None:
            return False
        else:
            return True
            
    def is_tied(self):
        if self.has_winner():
            return False
        else:    
            for row in range(3):
                for column in range(3):
                    if self.board.get_row(row)[column] is None:
                        return False
            return True
        

    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True
        return False
        



    def next_turn(self):
        if self.turns % 2 == 0:
            return self.player_1
        else:
            return self.player_2
            

    def move(self, player, row, col):
        
        if self.has_winner():
            raise InvalidMovementException()
        
        elif row > 2 or row < 0 or col > 2 or col < 0:
            raise InvalidMovementException()
            
        elif player not in [self.player_1, self.player_2]:
            raise InvalidMovementException()
        
        elif player != self.next_turn():
            raise InvalidMovementException()
        
        elif self.is_finished():
            raise InvalidMovementException()
        
        elif self.is_tied():
            raise InvalidMovementException()
            
        elif self.board.board[row][col] is not None:
            raise InvalidMovementException()
        
        else:
            self.board.board[row][col] = player
            self.turns += 1
            
    #player either 'X' or 'O'
    #X always goes first

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
        board = [
                [None,None,None],
                [None,None,None],
                [None,None,None],
            ]
        if initial_board:
            self.board = initial_board
        else:
            self.board = board
            
    def move(self, figure, row, col):
        self.board[row][col] = figure
        
    
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
        column_list = []
        for row in self.board:
            column_list.append(row[col_number])
        return column_list
        

    def get_diagonal(self, row_number):
        diagonal = []
        if row_number == 0:
            for i in range(3):
                diagonal.append(self.board[i][i])
        elif row_number == 1:
            diagonal.append(self.board[0][2])
            diagonal.append(self.board[1][1])
            diagonal.append(self.board[2][0])
        return diagonal
