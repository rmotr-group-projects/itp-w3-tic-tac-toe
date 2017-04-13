from .exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        
        self.next_player = player_1

    def is_finished(self):
        if self.has_winner() is True or self.is_tied() is True:
            return True
        return False
        
    def has_winner(self):
        if self.get_winner() is not None:
            return True
        return False

    def is_tied(self):
        for first_position in self.board.board:
            for second_position in first_position:
                if second_position is None:
                    return False
        return True

    def get_winner(self):
        x_combo = ['X', 'X', 'X']
        o_combo = ['O', 'O', 'O']
        
        for i in range(3):
            if self.board.get_row(i) == x_combo:
                return 'X'
            elif self.board.get_row(i) == o_combo:
                return 'O'

        for i in range(3):
            if self.board.get_column(i) == x_combo:
                return 'X'
            elif self.board.get_column(i) == o_combo:
                return 'O'

        for i in range(2):
            if self.board.get_diagonal(i) == x_combo:
                return 'X'
            elif self.board.get_diagonal(i) == o_combo:
                return 'O'        
        return None
       
    def next_turn(self):
        return self.next_player

    def move(self, player, row, col):
        if self.next_player != player:
            raise InvalidMovementException()
        elif row not in range(3) or col not in range(3):
             raise InvalidMovementException()
        elif self.board.board[row][col] is not None:
            raise InvalidMovementException()
        elif self.is_finished() is True:
            raise InvalidMovementException()
        
        self.board.move(player, row, col)
        
        if player == self.player_1:
            self.next_player = self.player_2
        elif player == self.player_2:
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
        if initial_board == None:
            self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        else:
            self.board = initial_board

    def move(self, figure, row, col):
        self.board[row][col] = figure

    def __str__(self):
        return BOARD_TEMPLATE.format(self.board[0][0] or '-', self.board[0][1] or '-', self.board[0][2] or '-',
        self.board[1][0] or '-', self.board[1][1] or '-', self.board[1][2] or '-',
        self.board[2][0] or '-', self.board[2][1] or '-', self.board[2][2] or '-')

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
            
            # for i in range(3):
            #     diagonal.append(self.board[i][i])
        else:
            diagonal.append(self.board[0][2])
            diagonal.append(self.board[1][1])
            diagonal.append(self.board[2][0])
            
            # for i in range(3):
            #     for j in range(2:-1:-1):
            #         diagonal.append(self.board[i][j])
        return diagonal
        
        