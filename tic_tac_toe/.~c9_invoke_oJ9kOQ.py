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
        my_board = [
            [None,None,None],
            [None,None,None],
            [None,None,None],
            ]
        
        if initial_board:
            self.board  = self.initial_board  
        else:
            self.board = my_board

    def move(self, figure, row, col):
        pass

    def __str__(self):
        my_board = []
        for row in self.board:
            for play in row:
                if play == None:
                    my_board.append('-')
                else: 
                    my_board.append(play)
            
        return BOARD_TEMPLATE.format(*my_board)

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        col_list = []
        for row in self.board:
            col_list.append(row[col_number])
        return col_list

    def get_diagonal(self, row_number):
        f

