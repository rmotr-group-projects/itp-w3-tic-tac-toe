from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board
        self.count = 2

    def is_finished(self):
        if self.has_winner() == True:
            return True
        elif self.is_tied() == True:
            return True
        else:
            return False

    def has_winner(self):
        for i in range(3):
            winner = self.board.get_row(i)
            if winner[0] is None:
                pass
            elif winner.count(winner[0]) > 2:
                return True
        for i in range(3):
            winner = self.board.get_column(i)
            if winner[0] is None:
                pass
            elif winner.count(winner[0]) > 2:
                return True
        for i in range(2):
            winner = self.board.get_diagonal(i)
            if winner[0] is None:
                pass
            elif winner.count(winner[0]) > 2:
                return True
        return False

    def is_tied(self):
        if self.has_winner() == True:
            return False
        for i in range(3):
          if None in self.board.get_row(i):
                return False
        for i in range(3):
          if None in self.board.get_column(i):
            return False
        return True
        
            

    def get_winner(self):
        if self.has_winner() == True:
            for i in range(3):
                winner = self.board.get_row(i)
                if winner[0] is None:
                    pass
                elif winner.count(winner[0]) > 2:
                    return winner[0]
            for i in range(3):
                winner = self.board.get_column(i)
                if winner[0] is None:
                    pass
                elif winner.count(winner[0]) > 2:
                    return winner[0]
            for i in range(2):
                winner = self.board.get_diagonal(i)
                if winner[0] is None:
                    pass
                elif winner.count(winner[0]) > 2:
                    return winner[0]
        else:
            return None

    def next_turn(self):
        if self.count % 2 == 0:
            return self.player_1
        else:
            return self.player_2

    def move(self, player, row, col):
        if self.has_winner() == True or self.is_tied() == True:
            raise InvalidMovementException
        elif player is not 'X' and player is not 'O':
            raise InvalidMovementException
        elif (row > 2 or row < 0) or (col > 2 or col < 0):
            raise InvalidMovementException
        elif self.next_turn() != player:
            raise InvalidMovementException
        elif self.board.get_row(row)[col] is not None:
            raise InvalidMovementException
        else:
            pass
        self.board.move(player, row, col)
        self.count += 1


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
        self.board = initial_board
        if initial_board is None:
            self.board = ([None, None, None], [None, None, None], [None, None, None])

    def move(self, figure, row, col):
        self.board[row][col] = figure
        return self.board
        
    def __str__(self):
        for i in self.board:
            count = 0
            for j in i:
                if j is None:
                  i[i.index(j)] = '-'
              
        return BOARD_TEMPLATE.format(
          self.board[0][0],
          self.board[0][1],
          self.board[0][2],
          self.board[1][0],
          self.board[1][1],
          self.board[1][2],
          self.board[2][0],
          self.board[2][1],
          self.board[2][2]
          )  # .format()

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        col = []
        for i in self.board:
            col.append(i[col_number])
        return col

    def get_diagonal(self, row_number):
        diag = []
        if row_number == 0: #start on left side
            count = 0
            for i in self.board:
                diag.append(i[count])
                count += 1
            return diag
        elif row_number == 1: #start on right side
            count = 2
            for i in self.board:
                diag.append(i[count])
                count -= 1
            return diag
        else:
            return "Invalid Selection"
