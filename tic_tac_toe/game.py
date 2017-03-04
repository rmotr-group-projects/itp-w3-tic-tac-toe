from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):
    
    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.current_player = self.player_1

    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True
        else:
            return False

    def has_winner(self):
        if self.get_winner():
            return True
        return False
        
    def is_tied(self):
        for x, lst in enumerate(self.board.initial_board):
            for i, item in enumerate(lst):
                if item is None:
                    return False
        return True


    def get_winner(self):
        p1 = ['X', 'X', 'X']
        p2 = ['O', 'O', 'O']
        if self.board.get_diagonal(0) == p1 or self.board.get_diagonal(1) == p1:
            return self.player_1
        elif self.board.get_diagonal(0) == p2 or self.board.get_diagonal(1) == p2:
            return self.player_2
        elif self.board.get_row(0) == p1 or self.board.get_row(1) == p1 or self.board.get_row(2) == p1:
            return self.player_1
        elif self.board.get_row(0) == p2 or self.board.get_row(1) == p2 or self.board.get_row(2) == p2:
            return self.player_2
        elif self.board.get_column(0) == p1 or self.board.get_column(1) == p1 or self.board.get_column(2) == p1:
            return self.player_1
        elif self.board.get_column(0) == p2 or self.board.get_column(1) == p2 or self.board.get_column(2) == p2:
            return self.player_2
        else:
            return None
        

    def next_turn(self):
        return self.current_player
            

    def move(self, player, row, col):
        invalid_moves = (row not in range(3) or
                        col not in range(3) or
                        self.board.initial_board[row][col] is not None or
                        self.is_finished() or
                        player != self.current_player)
        if invalid_moves:
            raise InvalidMovementException()
        
        self.board.move(player, row, col)
                
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

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
        if initial_board is None:
            self.initial_board =[[None, None, None],
                                [None, None, None],
                                [None, None, None]]
        else:
            self.initial_board = initial_board
        
    def move(self, figure, row, col):
        self.initial_board[row][col] = figure

    def __str__(self):
        for x, lst in enumerate(self.initial_board):
            for i, item in enumerate(lst):
                if item is None:
                    self.initial_board[x][i] = '-'
        the_board = self.initial_board[0] + self.initial_board[1] + self.initial_board[2]
        return BOARD_TEMPLATE.format(*the_board)
        
    def get_row(self, row_number):
        return self.initial_board[row_number]

    def get_column(self, col_number):
        col = []
        if col_number == 0:
            col.append(self.initial_board[0][0])
            col.append(self.initial_board[1][0])
            col.append(self.initial_board[2][0])
        elif col_number == 1:
            col.append(self.initial_board[0][1])
            col.append(self.initial_board[1][1])
            col.append(self.initial_board[2][1])
        elif col_number == 2:
            col.append(self.initial_board[0][2])
            col.append(self.initial_board[1][2])
            col.append(self.initial_board[2][2])
        return col
            

    def get_diagonal(self, row_number):
        diagonal = []
        if row_number == 0:
            diagonal.append(self.initial_board[0][0])
            diagonal.append(self.initial_board[1][1])
            diagonal.append(self.initial_board[2][2])
        elif row_number == 1:
            diagonal.append(self.initial_board[0][2])
            diagonal.append(self.initial_board[1][1])
            diagonal.append(self.initial_board[2][0])
        return diagonal
