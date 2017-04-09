class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2

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
        if initial_board == None:
            self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        else:
            self.board = initial_board

    def move(self, figure, row, col):
        pass




    def __str__(self):
        return BOARD_TEMPLATE.format(self.board[0][0] or '-', self.board[0][1] or '-',self.board[0][2] or '-',
        self.board[1][0] or '-', self.board[1][1] or '-', self.board[1][2] or '-',
        self.board[2][0] or '-', self.board[2][1] or '-', self.board[2][2] or '-')
"""
[
['X', None, None],
['O', 'X', None],
[None, 'O', 'X']
]

>>> mys = "Lets have this: {}"
>>> val = None
>>> val2 = 'X'
>>> news1 = mys.format(val or '-')
>>> print(news1)
Lets have this: -
>>> new2 = mys.format(val2 or '-')
>>> print(new2)
Lets have this: X


>>> None or '-'
'-'
>>> 'X' or '-'
'X'
>>> 'O' or '-'
'O'
>>> '-' or 'X'
'-'

"""
    def get_row(self, row_number):
        return board_data_as_lists[row_number]

    def get_column(self, col_number):
        column = []
        for row in board_data_as_lists:
            column.append(row[number])

    def get_diagonal(self, row_number):
        pass