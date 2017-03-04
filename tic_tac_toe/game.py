from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.next_player = player_1
        self.winner = None

    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True
        return False

    def has_winner(self):
        for row in range(3):
            if self.all_equal(self.board.get_row(row)):
                return True
        for col in range(3):
            if self.all_equal(self.board.get_column(col)):
                return True
        for dia in range(2):
            if self.all_equal(self.board.get_diagonal(dia)):
                return True
        return False
        

    def all_equal(self, a_list):
        if a_list[0] and (a_list[0] == a_list[1] == a_list[2]):
            self.winner = a_list[0]
            return True
        return False
       

    def is_tied(self):
        if self.winner:
            return False
        if self.board_is_full():
            return True
        

    def board_is_full(self):
        for row in range(3):
            for col in range(3):
                if self.board.get_row(row)[col] is None:
                    return False
        return True
        

    def get_winner(self):
        return self.winner

    def next_turn(self):
        return self.next_player

    def move(self, player, row, col):
        if self.winner:
            raise InvalidMovementException('Game is won!')
        if player not in [self.player_1, self.player_2]:
            raise InvalidMovementException('That is not a player!')
        if player != self.next_turn():
            raise InvalidMovementException('Wrong player turn!')
        self.board.move(player, row, col)
        if player == self.player_1:
            self.next_player = self.player_2
        else:
            self.next_player = self.player_1


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
            self.board = [[None, None, None],
                          [None, None, None],
                          [None, None, None]]

    def move(self, figure, row, col):
        if row > 2 or row < 0 or col > 2 or col < 0:
            raise InvalidMovementException('That is not on the board!')
        if self.board[row][col]:
            raise InvalidMovementException('Hey, that is not not a real move!')
        else:
            self.board[row][col] = figure

    def __str__(self):
        string_board = []
        for row in self.board:
            for col in row:
                if not col:
                    string_board.append('-')
                else:
                    string_board.append(col)

        return BOARD_TEMPLATE.format(*string_board)

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        column = []
        for row in self.board:
            column.append(row[col_number])
        return column

    def get_diagonal(self, row_number):
        diagonal = []
        if row_number == 0:
            diagonal.append(self.board[0][0])
            diagonal.append(self.board[1][1])
            diagonal.append(self.board[2][2])
        elif row_number == 1:
            diagonal.append(self.board[0][2])
            diagonal.append(self.board[1][1])
            diagonal.append(self.board[2][0])
        return diagonal
