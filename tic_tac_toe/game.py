from .exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.next_player = player_1

    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True

    def has_winner(self):
        if self.get_winner():
            return True

    def is_tied(self):
        if self.get_winner():
            return False
        for i in range(3):
            if None in self.board.get_row(i):
                return False
        else:
            return True

    def get_winner(self):
        player_1_wins = [self.player_1, self.player_1, self.player_1]
        player_2_wins = [self.player_2, self.player_2, self.player_2]
        for i in range(3):
            if self.board.get_row(i) == player_1_wins:
                return self.player_1
            elif self.board.get_column(i) == player_1_wins:
                return self.player_1
            elif self.board.get_row(i) == player_2_wins:
                return self.player_2
            elif self.board.get_column(i) == player_2_wins:
                return self.player_2
        if self.board.get_diagonal(0) == player_1_wins or self.board.get_diagonal(1) == player_1_wins:
                return self.player_1
        elif self.board.get_diagonal(0) == player_2_wins or self.board.get_diagonal(1) == player_2_wins:
                return self.player_2


    def next_turn(self):
        return self.next_player

   
    def move(self, player, row, col):
        if player != self.next_turn():
            raise InvalidMovementException
        elif row not in [0, 1, 2]:
            raise InvalidMovementException
        elif col not in [0, 1, 2]:
            raise InvalidMovementException
        elif self.board.board[row][col] is not None:
            raise InvalidMovementException
        elif self.is_finished():
            raise InvalidMovementException
        
        self.board.move(player, row, col)
        if player == self.player_2:
            self.next_player = self.player_1 
        else:
            self.next_player = self.player_2

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
        template = []
        for x in self.board:
            for y in x:
                if y:
                    template.append(y)
                else:
                    template.append('-')
        return BOARD_TEMPLATE.format(*template)

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        results = []
        for row in self.board:
            results.append(row[col_number])
        return results

    def get_diagonal(self, row_number):
        if row_number == 0:
            positions = [self.board[0][0], self.board[1][1], self.board[2][2]]
            return positions
        elif row_number == 1:
            positions = [self.board[0][2], self.board[1][1], self.board[2][0]]
            return positions
        diagonal = []
        for position in positions:
            row = position[0]
            col = position[1]
            diagonal.append(self.board[row][col])
        return diagonal