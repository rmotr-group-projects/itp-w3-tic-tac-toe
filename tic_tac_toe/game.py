from tic_tac_toe.exceptions import *

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn_count = 0

    def is_finished(self):
        self.win_check = self.has_winner()
        self.tie_check = self.is_tied()
        
        if self.win_check == True or self.tie_check == True:
            self.turn_count = 0
            return True
            
        else:
            return False

    def has_winner(self):
        self.check = self.get_winner()
        
        if self.check == self.player_1 or self.check == self.player_2:
            return True
        else:
            return False

    def is_tied(self):
        '''Verify that all spaces have been played'''
        self.moves_left = 0
        self.win_check = self.has_winner()

        for i, values in enumerate(self.board.grid):
            for j, items in enumerate(values):
                if items == None:
                    self.moves_left += 1

        if self.moves_left == 0 and self.win_check == False:#all spaces were played and no winner was found
            return True
        else:
            return False

    def get_winner(self):
        '''Check every row, column, and diagonal for a win condition'''
        self.r0 = self.board.get_row(0)
        self.r1 = self.board.get_row(1)
        self.r2 = self.board.get_row(2)
        self.c0 = self.board.get_column(0)
        self.c1 = self.board.get_column(1)
        self.c2 = self.board.get_column(2)
        self.d1 = self.board.get_diagonal(0)
        self.d2 = self.board.get_diagonal(1)

        #The win condition
        self.p1 = [self.player_1, self.player_1, self.player_1]
        self.p2 = [self.player_2, self.player_2, self.player_2]


        #Check if player 1 (X) won
        if self.r0 == self.p1 or self.r1 == self.p1 or self.r2 == self.p1:
            return self.player_1 #'X'

        elif self.c0 == self.p1 or self.c1 == self.p1 or self.c2 == self.p1:
            return self.player_1
 
        elif self.d1 == self.p1 or self.d2 == self.p1:
            return self.player_1


        #Check if player 2(O) won
        elif self.r0 == self.p2 or self.r1 == self.p2 or self.r2 == self.p2:
            return self.player_2 #'O'
  
        elif self.c0 == self.p2 or self.c1 == self.p2 or self.c2 == self.p2:
            return self.player_2
            
        elif self.d1 == self.p2 or self.d2 == self.p2:
            return self.player_2


        #No winner was found
        else:
            return None

    def next_turn(self):
        #when turn_count is even, X is next. This includes when turn_count starts at 0
        if self.turn_count % 2 == 0:
            return self.player_1
        else:
            return self.player_2

    def move(self, player, row, col):
        '''Check for invalid move options, such as incorrect player(not X or O), 
        taking turns out of order out of bounds, game is finished, or an attempt 
        to play a spot that is already taken'''
        
        if self.is_finished() == True:
            raise InvalidMovementException
            
        elif (player != self.player_1 and player != self.player_2):
            raise InvalidMovementException
            
        elif player != self.next_turn():
            raise InvalidMovementException
            
        elif row > 2 or row < 0:
            raise InvalidMovementException
            
        elif col > 2 or col < 0:
            raise InvalidMovementException
            
        # check if the move has not already been completed by the players. 
        #If it hasn't, the space should say None
        elif self.board.grid[row][col] != None:
            self.turn_count += 1
            if player != self.board.grid[row][col]:
                raise InvalidMovementException
            else:
                pass


        #if the move is valid, then find the space they are requesting and 
        #place their symbol(player) there(the correct row and column). 
        else:
            self.board.move(player,row,col)
            self.turn_count += 1

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

#Make an empty board matrix

Starting_Board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

class Board(object):
    def __init__(self, initial_board=Starting_Board):
        self.grid = initial_board

    def move(self, figure, row, col):
        if self.grid[row][col] != None:
            raise InvalidMovementException
        else:
            for i, values in enumerate(self.grid):
                if i == row:
                    values[col] = figure

    def __str__(self):
              
        return BOARD_TEMPLATE.format(
            self.grid[0][0] or '-',
            self.grid[0][1] or '-',
            self.grid[0][2] or '-',
            self.grid[1][0] or '-',
            self.grid[1][1] or '-',
            self.grid[1][2] or '-',
            self.grid[2][0] or '-',
            self.grid[2][1] or '-',
            self.grid[2][2] or '-'
            )

    def get_row(self, row_number):
        self.row_results = self.grid[row_number]
        return self.row_results

    def get_column(self, col_number):
        self.col_results = []
        
        for i, values in enumerate(self.grid):
            self.col_results.append(values[col_number])
            
        return self.col_results

    def get_diagonal(self, row_number):
        self.diag_results = []
        
        #forward diagonal
        if row_number == 0:
            for i, values in enumerate(self.grid):
                self.diag_results.append(values[i])
        
        #backward diagonal        
        elif row_number == 1:
            for i, values in enumerate(self.grid):
                self.diag_results.append(values[2 - i])
                
        return self.diag_results