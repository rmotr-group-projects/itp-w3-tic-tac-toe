import string
from exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        
        self.next_player = player_1

    def is_finished(self):
        if self.has_winner():
            return True
        
        if self.board._has_empty_square():
            return False
            
        return True
        
    def has_winner(self):
        for a in range(3):
            check_row_list = self.board.get_row(a)
            if 'O' in check_row_list and 'X' not in check_row_list and None not in check_row_list:
                return True
            elif 'X' in check_row_list and 'O' not in check_row_list and None not in check_row_list:
                return True
            elif 'O' in self.board.get_column(a) and 'X' not in self.board.get_column(a) and None not in self.board.get_column(a):
                return True
            elif 'X' in self.board.get_column(a) and 'O' not in self.board.get_column(a) and None not in self.board.get_column(a):
                return True
        for a in range(2):
            if 'O' in self.board.get_diagonal(a) and 'X' not in self.board.get_diagonal(a) and None not in self.board.get_diagonal(a):
                return True
            elif 'X' in self.board.get_diagonal(a) and 'O' not in self.board.get_diagonal(a) and None not in self.board.get_diagonal(a):
                return True
        return False
            
                

    def is_tied(self):
        if self.is_finished() and not self.has_winner():
            return True

    def get_winner(self):
        if self.has_winner():
            return self.next_player
        else: 
            return None

    def next_turn(self):
        
        return self.next_player

    def move(self, player, row, col):
        if self.is_finished():
            raise InvalidMovementException()
            
        if player != self.next_player:
            raise InvalidMovementException()
            
        if (row < 0 or row > 2) or (col < 0 or col > 2):
            raise InvalidMovementException()
            
        if self.board.get_row(row)[col] != None:
            raise InvalidMovementException()
        
        
        self.board.move(self.next_player, row, col)
        
        
        self.next_player = 'X' if player == 'O' else 'O'
            
        


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
            brd_array = []
            for row in range(3):
                brd_array.append([])
                for col in range(3):
                    brd_array[row].append(None)
            self.board = brd_array
            
                
    def _has_empty_square(self):
        for arr in self.board:
            if None in arr:
                return True
                
        return False
        
        
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
            self.board[2][2] or '-',) 

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        rtn_list = []
        # return self.board[:][col_number]
        for a in range(3):
            rtn_list.append(self.board[a][col_number])
        return rtn_list
            

    def get_diagonal(self, row_number):
        rtn_list = []
        if row_number == 0:
            rtn_list.append(self.board[0][0])
            rtn_list.append(self.board[1][1])
            rtn_list.append(self.board[2][2])
        else:
            rtn_list.append(self.board[0][2])
            rtn_list.append(self.board[1][1])
            rtn_list.append(self.board[2][0])
        return rtn_list
            
