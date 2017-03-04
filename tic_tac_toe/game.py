from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):
    
    def __init__(self,board,player_1,player_2):
        self.board= board
        self.player_1= 'X'
        self.player_2= 'O'
        self.next_player = self.player_1

    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True
        else:
            return False

    def has_winner(self):
        if self.get_winner():
            return True
            
    def is_tied(self):
        for i in range(3):
            for j in range (3):
                if self.board.get_row(i)[j] is None:
                    return False
        return True

    def get_winner(self):
        winner1 = ['X', 'X', 'X']
        winner2 = ['O', 'O', 'O']
        for i in range(3):
            if self.board.get_row(i) == winner1:
                return winner1[0]
            elif self.board.get_row(i) == winner2:
                return winner2[0]
        for i in range(3):
            if self.board.get_column(i) == winner1:
                return winner1[0]
            elif self.board.get_column(i) == winner2:
                return winner2[0]
        for i in range(2):
            if self.board.get_diagonal(i) == winner1:
                return winner1[0]
            elif self.board.get_diagonal(i) == winner2:
                return winner2[0]
        return None

    def next_turn(self):
        return self.next_player

    def move(self, player, row, col):
        
        invalid_moves= (  
            row not in range(3) or
            col not in range(3) or
            self.is_finished() or 
            self.board.board[row][col] is not None or
            player != self.next_player 
            )
         #game.move('X', row=3, col=0)
        if invalid_moves:
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
        if initial_board is None:
            self.board = {
                0: [None, None, None],
                1: [None, None, None],
                2: [None, None, None],
            }
        else:
            self.board = initial_board

    def move(self, figure, row, col):
        self.board[row][col] = figure

    def __str__(self):
        return BOARD_TEMPLATE.format(
            self.board[0][0] or '-',
            self.board[0][1] or '-',
            self.board[0][2] or '-',
            self.board[1][0] or '-',
            self.board[1][1] or '-',
            self.board[1][2] or '-',
            self.board[2][0] or '-',
            self.board[2][1] or '-',
            self.board[2][2] or '-',)
        
    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        column_return = []
        for i in range(3):
            column_return.append(self.board[i][col_number])
        return column_return

    def get_diagonal(self, diagonal):
        diagonal_return = []
        count = 2
        if diagonal is 0:
            for i in range(3):
                diagonal_return.append(self.board[i][i])
        else:
            for i in range(3):
                diagonal_return.append(self.board[i][count])
                count -= 1
        return diagonal_return
        

