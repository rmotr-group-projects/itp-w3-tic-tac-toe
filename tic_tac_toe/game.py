class Game(object):
    VALID_POSITIONS = list(range(3))

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2

        self.next_player = self.player_1

    def is_finished(self):
        return self.has_winner() or self.is_tied()

    def has_winner(self):
        return self.get_winner() is not None

    def is_tied(self):
        for elem in self.board.flatten():
            if elem is None:
                return False
        return True

    def get_winner(self):
        valid_combinations = [
            self.board.get_row(i) for i in range(3)
        ] + [
            self.board.get_diagonal(i) for i in range(2)
        ] + [
            self.board.get_column(i) for i in range(3)
        ]
        for combination in valid_combinations:
            elems = set(combination)
            if None not in elems and len(elems) == 1:
                return combination[0]

        return None

    def next_turn(self):
        return self.next_player

    def move(self, player, row, col):
        invalid_move_condition = (
            player != self.next_player or
            row not in self.VALID_POSITIONS or
            col not in self.VALID_POSITIONS or
            self.board.get_row(row)[col] is not None or
            self.is_finished()
        )
        if invalid_move_condition:
            raise InvalidMovementException()

        self.board.move(player, row, col)
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
