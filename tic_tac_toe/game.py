from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn = 1

    def is_finished(self):
        return self.is_tied() or self.has_winner()

    def has_winner(self):
        if self.get_winner():
            return True
        return False

    def is_tied(self):
        for row in self.board.board:
            if None in row:
                return False
        return True

    def get_winner(self):
        board = self.board
        win1 = ['X','X','X']
        win2 = ['O','O','O']
        for elem in range(3):
            if board.get_row(elem) == win1 or board.get_row(elem) == win2:
                return board.get_row(elem)[0]
            if board.get_column(elem) == win1 or board.get_column(elem) == win2:
                return board.get_column(elem)[0]
            if board.get_diagonal(elem) == win1 or board.get_diagonal(elem) == win2:
                return board.get_diagonal(elem)[0]
        return None

    def next_turn(self):
        if self.turn % 2 == 0:
            return self.player_2
        return self.player_1

    def move(self, player, row, col):
        if (row or col) not in range(3):
            raise InvalidMovementException()
        if player not in 'XO' or player != self.next_turn():
            raise InvalidMovementException()
        if self.board.board[row][col] != None:
            raise InvalidMovementException()
        if self.get_winner():
            raise InvalidMovementException()

        self.board.move(player,row,col)
        self.turn += 1


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
            initial_board = [
                [None, None, None], # 1 2 3
                [None, None, None], # 4 5 6
                [None, None, None] # 7 8 9
            ]
        self.board = initial_board #None != list of lists of None values   
        format_board = []
        for row in initial_board: #0 1 2
            for col in row: #0 1 2
                if not col: #not None = not False = True | not "anyvalue" = not True = False
                    col = '-' #initial_board[row][col] = '-'
                format_board.append(col) #[1,2,3,4,5,6,7,8,9]
        self.format_board = format_board


    def move(self, figure, row, col):
        self.board[row][col] = figure

    def __str__(self):                                    # [1,2,3,4,5,6,7,8,9]
        return BOARD_TEMPLATE.format(*self.format_board) #    \n| {} \n {}



    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        col = []
        for row in self.board:
            col.append(row[col_number])
        return col

    def get_diagonal(self, row_number):
        diag = []
        col = len(self.board) #3
        for row in range(0,len(self.board)): #0 1 2
            col -= 1 #2 1 0
            
            if row_number == 0:
                col = row #0 1 2
                
            diag.append(self.board[row][col])
        return diag
