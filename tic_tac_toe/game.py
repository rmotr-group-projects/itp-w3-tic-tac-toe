from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):
    winner = None
    
    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn_count = 1

    def is_finished(self):
        if self.has_winner():
            return True
        for x in self.board.board:
            for y in x:
                if y is None:
                    return False
        else:
            return True

    def has_winner(self):
        for x in range(3):
            l = self.board.get_row(x)
            if l[0] == l[1] == l[2]:
                if l[0] is not None:
                    self.winner = l[0]
                    return True
            l = self.board.get_column(x)
            if l[0] == l[1] == l[2]:
                if l[0] is not None:
                    self.winner = l[0]
                    return True
            l = self.board.get_diagonal(x)
            if l[0] == l[1] == l[2]:
                if l[0] is not None:
                    self.winner = l[0]
                    return True
        else:
            return False
        
    def is_tied(self):
        if self.winner is None and self.is_finished():
            return True

    def get_winner(self):
        return self.winner

    def next_turn(self):
        if self.turn_count % 2 == 0:
            return self.player_2
        else:
            return self.player_1

    def move(self, player, row, col):
        
        if (player not in ('X', 'O') or 
          self.next_turn() is not player or
           (row > 2) or (row < 0) or 
           (col > 2) or (col < 0) or 
           self.is_tied is True or 
           self.winner is not None or
           self.is_finished is True):
               raise InvalidMovementException()
            
        if self.board.board[row][col] is None:
            self.board.board[row][col] = player
        else:
            raise InvalidMovementException()
        self.turn_count += 1


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
            self.board = [
                [None, None, None],[None, None, None],[None, None, None]
            ]
        else:
            self.board = initial_board

    def move(self, figure, row, col):
        self.board[row][col] = figure
        
    def __str__(self):
        board_str = BOARD_TEMPLATE.format(
        self.board[0][0] or '-',
        self.board[0][1] or '-',
        self.board[0][2] or '-',
	
        self.board[1][0] or '-',
        self.board[1][1] or '-',
        self.board[1][2] or '-',
	
        self.board[2][0] or '-',
        self.board[2][1] or '-',
        self.board[2][2] or '-',
)
        return board_str

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        column = []
        list1 = []
        for i in range(len(self.board)):
            list1 = self.board[i]
            column.append(list1[col_number])
        return column

    def get_diagonal(self, row_number):
        diag = []
        if row_number == 0:
            diag.append(self.board[0][0])
            diag.append(self.board[1][1])
            diag.append(self.board[2][2])
        elif row_number == 1:
            diag.append(self.board[0][2])
            diag.append(self.board[1][1])
            diag.append(self.board[2][0])
        else:
            return [None, None, None]
        return diag
        
            
