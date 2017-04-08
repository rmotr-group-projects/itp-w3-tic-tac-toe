from .exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.player1figure = player_1
        self.player2figure = player_2
        self.board = board
        self.nextplayer = player_1
        self.valid_position = [0,1,2]

    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True
        return False
    
    def has_winner(self):
        if self.get_winner() is not None:
            return True
        return False

    def is_tied(self):
        isFull = True
        for row in self.board.board:
            if None not in row:
                continue
            else:
                isFull = False
        if isFull and self.get_winner() is None:
            return True
        return False

    def get_winner(self):
        owinner = ['O','O','O']
        xwinner = ['X','X','X']
        
        for row in self.board.board:
            if row == xwinner:
                return 'X' 
            else: 
                if row == owinner:
                    return 'O'
                    
        for column in range(3):
            if self.board.get_column(column) == xwinner:
                return 'X'
            else: 
                if self.board.get_column(column) == owinner:
                    return 'O'
                    
        for diagonal in range(2):
            if self.board.get_diagonal(diagonal) == xwinner:
                return 'X'
            else: 
                if self.board.get_diagonal(diagonal) == owinner:
                    return 'O'
        return None

    def next_turn(self):
        return self.nextplayer

    def move(self, player, row, col):
        if player != self.nextplayer:
            raise InvalidMovementException
        if row not in self.valid_position:  # valid positions [0, 1, 2]
            raise InvalidMovementException
        if col not in self.valid_position:
            raise InvalidMovementException
        if self.board.board[row][col] != None:
            raise InvalidMovementException
        if self.is_finished():
            raise InvalidMovementException
        
        # All good, make the move!
        self.board.move(player, row, col)
        self.nextplayer = 'X' if player == 'O' else 'O'


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
            row1 = [None, None, None]
            row2 = [None, None, None]
            row3 = [None, None, None]
            self.board = [row1, row2, row3]
            
        else:
            self.board = initial_board
        

    def move(self, figure, row, col):
        self.board[row][col] = figure

    def __str__(self):
        return BOARD_TEMPLATE.format(
            self.board[0][0] or '-', self.board[0][1] or '-', self.board[0][2] or '-',
            self.board[1][0] or '-', self.board[1][1] or '-', self.board[1][2] or '-',
            self.board[2][0] or '-', self.board[2][1] or '-', self.board[2][2] or '-',
        )  # .format()

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        result = [
            self.board[0][col_number],
            self.board[1][col_number],
            self.board[2][col_number]
        ]
        
        return result

    def get_diagonal(self, row_number):
        
        if row_number == 0:
            result = [
            self.board[0][0],
            self.board[1][1],
            self.board[2][2]
            ]
                
        else:
            result = [
            self.board[0][2],
            self.board[1][1],
            self.board[2][0]
            ]
            
        return result