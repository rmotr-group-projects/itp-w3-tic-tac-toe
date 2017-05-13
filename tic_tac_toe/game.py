from .exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board 
        self.player_1 = player_1
        self.player_2 = player_2
        self._winner = None
        self.player_turn = player_1

    def is_finished(self):
        """
        haswinner or istied
        True or True # True
        True or False # True
        False or True # True
        False or False # False
        """
        return self.has_winner() or self.is_tied()


    def has_winner(self):
        for row in self.board.board:
            if bool(row[0] or row[1] or row[2]) is False: # There is an empty space
                continue
            elif row[0] == row[1] and row[1] == row[2]: # Otherwise check to see all spaces match
                self._winner = row[0]
                return True
        for col_number in range(3):
            col = self.board.get_column(col_number)
            if bool(col[0] or col[1] or col[2]) is False:
                continue
            elif col[0] == col[1] and col[1] == col[2]:
                self._winner = col[0]
                return True        
        for diag_num in range(2):
            diag = self.board.get_diagonal(diag_num)
            if bool(diag[0] or diag[1] or diag[2]) is False:
                continue
            elif diag[0] == diag[1] and diag[1] == diag[2]:
                self._winner = diag[0]
                return True
        return False

    def is_tied(self):
        if self.has_winner() is False:
            for row in self.board.board:
                for col in row:
                    if col is None:
                        return False
        else: # somebody won, there isn't a tie
            return False
        return True
        
                        
    #if row[0] and row[1] and row[2] != None and Winner = False

    def get_winner(self):
        if self.has_winner():
            return self._winner

    def next_turn(self):
        return self.player_turn
        

    def move(self, player, row, col):               # It would be best to work your way from top to bottom for this class, since in `move` you will basically check most of them
        if (self.is_finished() or
            self.next_turn() != player or
            row not in range(3) or
            col not in range(3) or
            self.board.get_row(row)[col] != None):
            raise InvalidMovementException
        self.board.move(player, row, col) # YAAAAAASSS :D :D :D :D (Don't forget to do your checks first though)
        if player == self.player_1:
            self.player_turn = self.player_2
        else:
            self.player_turn = self.player_1

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
            self.board = [[None, None, None],[None, None, None],[None, None, None]]
        else:
            self.board = initial_board
        # In your parameters you have `initial_board=None`, which means that initial_board is optional, it could be passed it could not be. If it's not passed you must create a starting  board yourself.

    def move(self, figure, row, col):
        self.board[row][col] = figure

    def __str__(self):
        # board[0][1]
        output_list = []
        return BOARD_TEMPLATE.format(self.board[0][0] or '-',self.board[0][1] or '-',self.board[0][2] or '-',
        self.board[1][0] or '-',self.board[1][1] or '-',self.board[1][2] or '-',self.board[2][0] or '-',
        self.board[2][1] or '-',self.board[2][2] or '-')
# remember that if your "backend" value of the board is None it needs to be represented by a '-'
# >>> 'X' or '-'
# 'X'
# '{} {} {}'.format("", "", "")
    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        col_list = []
        for row in self.board:
            col_list.append(row[col_number])
        return col_list
        

    def get_diagonal(self, row_number):
        diag_list = []
        if row_number == 0:
            col_count = 0
            for row in self.board:
                diag_list.append(row[col_count])
                col_count += 1
            return diag_list
        elif row_number == 1:
            col_count = 2
            for row in self.board:
                diag_list.append(row[col_count])
                col_count -= 1
            return diag_list
            
            


# 'X' or '-'
# 'X'
# None or '-'
# '-'
#     name = "Josh"
#     greeting = "Hello my name is {}".format(name)