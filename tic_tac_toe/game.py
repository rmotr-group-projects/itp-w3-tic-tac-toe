from tic_tac_toe.exceptions import InvalidMovementException
class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board=board
        self.player_1=player_1
        self.player_2=player_2
        self.next_player=self.player_1
        self.win_cond=[['X', 'X', 'X'], ['O', 'O', 'O']]
    
    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True
        return False

    def has_winner(self):
        if self.get_winner():
            return True
        return False

    def is_tied(self):
        for i in range(3):
            for z in range(3):
                if self.board.get_row(i)[z] is None:  
                    return False
        return True

    def get_winner(self):     
        for i in range(3):
            if self.board.get_row(i) == self.win_cond[0] or self.board.get_row(i) == self.win_cond[1]:
                winner=self.board.get_row(i)
                return winner[0]
        for i in range(3):
            if self.board.get_column(i) == self.win_cond[0] or self.board.get_column(i) == self.win_cond[1]:
                winner=self.board.get_column(i)
                return winner[0]
        for i in range(2):
            if self.board.get_diagonal(i) == self.win_cond[0] or self.board.get_diagonal(i) == self.win_cond[1]:
                winner=self.board.get_diagonal(i)
                return winner[0]
        return None
    def next_turn(self):
        return self.next_player

    def move(self, player, row, col):
        moves_is_invalid = (
            row not in range(3) or
            col not in range(3) or
            player is not self.next_player or
            self.is_finished() or
            self.board.init_board[row][col] is not None
            )
        if moves_is_invalid:
            raise InvalidMovementException
            
        self.board.move(player, row, col)
        if player == 'X':
            self.next_player = 'O'
        elif player == 'O':
            self.next_player = 'X'


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
        """If no value is given the default None value will cause the board to be an empty board, otherwise the board will be the initial board given."""
        if initial_board==None:
            self.init_board = [ 
                [None, None, None],
                [None, None, None],
	            [None, None, None],
                ]
        else:
            self.init_board = initial_board
	    
            

    def move(self, figure, row, col):
        """This essentially appends to the board, given the row, col, and figure perameters."""
        self.init_board[row][col]=figure

    def __str__(self):
        """Here we just index self.board and using format we use the board template to show the board with the figures."""
        return BOARD_TEMPLATE.format(
	    self.init_board[0][0] or '-',
	    self.init_board[0][1] or '-',
	    self.init_board[0][2] or '-',
        self.init_board[1][0] or '-',
	    self.init_board[1][1] or '-',
	    self.init_board[1][2] or '-',
        self.init_board[2][0] or '-',
	    self.init_board[2][1] or '-',
	    self.init_board[2][2] or '-',
	
)
 

    def get_row(self, row_number):
        """Perameters 0-2 get a row back."""
        return self.init_board[row_number]

    def get_column(self, col_number):
        """Perameters 0-2 get a column back."""
        newcol=[]
        for i in range(3):
            newcol.append(self.init_board[i][col_number])
        return newcol

    def get_diagonal(self, row_number):
        """Diagonal 0 is left to right diagonal going downwards. Diagonal 1 is right to left diagonal going downwards."""
        diag=[]
        if row_number == 0:
            for i in range(3):
                diag.append(self.init_board[i][i])
            return diag
        elif row_number == 1:
            diag.append(self.init_board[0][2])
            diag.append(self.init_board[1][1])
            diag.append(self.init_board[2][0])
            return diag