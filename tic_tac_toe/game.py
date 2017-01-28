class Game(object):

    def __init__(self, board, player_1, player_2):
        pass

    def is_finished(self):
        pass

    def has_winner(self):
        pass

    def is_tied(self):
        pass

    def get_winner(self):
        pass

    def next_turn(self):
        pass

    def move(self, player, row, col):
        pass


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
        return BOARD_TEMPLATE.format(*(
            [val or '-' for val in self.board[0]] +
            [val or '-' for val in self.board[1]] +
            [val or '-' for val in self.board[2]]
        ))

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        return [
            self.board[0][col_number], self.board[1][col_number], self.board[2][col_number]
            ]

    def get_diagonal(self, right_diag):
        diag = [0,0,0]
        if right_diag:
            diag[0] = self.board[0][2]
            diag[2] = self.board[2][0]
        else:
            diag[0] = self.board[0][0]
            diag[2] = self.board[2][2]
        diag[1] = self.board[1][1]
        return diag
