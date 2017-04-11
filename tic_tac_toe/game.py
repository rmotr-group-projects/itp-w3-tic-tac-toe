from .exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.cur_player = player_1
        self.winner = None

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
            for x in range(0,2): #check all rows to see if there are still blank squares on the board
                if not all(self.board.get_row(x)):
                    return False
            return True

    def get_winner(self):
        for rows in range(len(self.board.initial_board)): #for rows in range of the number of elements in the initial board (0,1,2)
            if self.board.get_row(rows)[1:] == self.board.get_row(rows)[:-1]: #if all elements in a particular row are the same 
                if self.board.get_row(rows)[0] == self.player_1: #check to see if they are player one
                    self.winner = self.player_1
                elif self.board.get_row(rows)[0] == self.player_2: #...or player 2
                    self.winner = self.player_2
        for cols in range(len(self.board.initial_board)): #for columns in range of the number of elements in the initial board (0,1,2)
            if self.board.get_column(cols)[1:] == self.board.get_column(cols)[:-1]: #if all elements in a particular column are the same 
                if self.board.get_column(cols)[0] == self.player_1: #check to see if they are player one
                    self.winner = self.player_1
                elif self.board.get_column(cols)[0] == self.player_2: #...or player 2
                    self.winner = self.player_2
        for diagonals in range(2):
            if self.board.get_diagonal(diagonals)[1:] == self.board.get_diagonal(diagonals)[:-1]: #if all elements in a particular column are the same 
                if self.board.get_diagonal(diagonals)[0] == self.player_1: #check to see if they are player one
                    self.winner = self.player_1
                elif self.board.get_diagonal(diagonals)[0] == self.player_2: #...or player 2
                    self.winner = self.player_2
        return self.winner
        
        
    def next_turn(self):
        return self.cur_player

    def move(self, player, row, col):
        r=range(0,3) #0,1,2
        if row not in r or col not in r: #row or col not 0 1 or 2
            raise InvalidMovementException
        elif player != self.cur_player: #wrong player trying to move
            raise InvalidMovementException
        elif self.board.initial_board[row][col] is not None: #spot taken
            raise InvalidMovementException
        elif self.is_finished() is True: #game is over already
            raise InvalidMovementException
 
        self.board.initial_board[row][col] = player
        
        if player == self.player_1:
            self.cur_player = self.player_2
        else:
            self.cur_player = self.player_1


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
        if initial_board == None:
            self.initial_board = [
                [None,None,None],
                [None,None,None],
                [None,None,None]
            ]
        else:
            self.initial_board = initial_board

    def move(self, figure, row, col):
        if not self.initial_board[row][col]:
            self.initial_board[row][col] = figure

    def __str__(self):
        return BOARD_TEMPLATE.format(self.initial_board[0][0] or '-', self.initial_board[0][1] or '-',self.initial_board[0][2] or '-',
        self.initial_board[1][0] or '-', self.initial_board[1][1] or '-', self.initial_board[1][2] or '-',
        self.initial_board[2][0] or '-', self.initial_board[2][1] or '-', self.initial_board[2][2] or '-')

    def get_row(self, row_number):
        return self.initial_board[row_number]

    def get_column(self, col_number):
        col = []
        for x in range(len(self.initial_board)):
            col.append(self.initial_board[x][col_number])
        return col

    def get_diagonal(self, row_number):
        diagonal = []
        if not row_number: #only options seem to be one and 0
            for row in range(len(self.initial_board)): #should work for any size board
                diagonal.append(self.initial_board[row][row])
        else:
            for row in range(len(self.initial_board)): #should work for any size board
                index = len(self.initial_board) -row - 1
                diagonal.append(self.initial_board[row][index])
        return diagonal
        
            
