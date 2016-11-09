from exceptions import InvalidMovementException

class Game(object):
    def __init__(self, board , player_1="X", player_2="Y"):
        self.p1 = player_1
        self.p2 = player_2
        self.finished = False
        self.there_is_winner = False
        self.tied = False
        self.winner = None
        self.next = self.p1
        self.board = board

    def is_finished(self):
        if(self.has_winner()):
            self.finished = True
        elif ( None not in self.board.get_diagonal(0) or  None not in self.board.get_diagonal(1)):
            self.finished = True 
        return self.finished

    def has_winner(self):
        for i in range(3):
            if self.board.get_column(i) == ['X' , 'X' , 'X']:
                self.winner = 'X'
            elif self.board.get_column(i) == ['Y' , 'Y' , 'Y']:
                self.winner = 'Y'
            if self.board.get_row(i) == ['X' , 'X' , 'X']:
                self.winner = 'X'
            elif self.board.get_row(i) == ['Y' , 'Y' , 'Y']:
                self.winner = 'Y'

        if self.board.get_diagonal(0) == ['X' , 'X' , 'X']:
            self.winner = 'X'
        elif self.board.get_diagonal(0) == ['Y' , 'Y' , 'Y']:
            self.winner = 'Y'
        if self.board.get_diagonal(1) == ['X' , 'X' , 'X']:
            self.winner = 'X'
        elif self.board.get_diagonal(1) == ['Y' , 'Y' , 'Y']:
            self.winner = 'Y'
            
        if self.winner != None : 
            return True

    def is_tied(self):
        if self.is_finished() and self.winner == None : 
            return True

    def get_winner(self):
        return self.winner

    def next_turn(self):
        return self.next
    
    def move(self, player, row, col):
        if(row > 2 or col > 2 or col < 0 or row < 0): raise InvalidMovementException
        # make sure slot is empty and player is the next player 
        if(self.board.empty(row , col) and player == self.next and not self.is_finished() ):
            # make move 
            self.board.move(player , row , col)
            print('success')
            # update player.next
            self.next = self.p1 if self.next == self.p2 else self.p2
        else:
            raise InvalidMovementException


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
    #empty = True;
    def __init__(self, initial_board=None):
        temp = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.board = initial_board if (initial_board) else temp 
    
    def empty(self , row , col):
        return self.board[row][col] == None

    def move(self, figure, row, col):
        self.board[row][col] = figure

    def __str__(self):
        li = []
        for i in self.board:
            for j in i : 
                li.append('-' if j == None else j)
                
        return BOARD_TEMPLATE.format(*li)

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        col = []
        for i in self.board:
            col.append(i[col_number])
        return col

    def get_diagonal(self, row_number):
        if(row_number == 0):
            return [self.board[0][0] , self.board[1][1] , self.board[2][2]]
        else:
            return [self.board[0][2] , self.board[1][1] , self.board[2][0]]
    
