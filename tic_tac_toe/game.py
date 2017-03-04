from exceptions import InvalidMovementException

class Game(object):
    CELLS = list(range(3))

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None
        self.turn = self.player_1

    def is_finished(self):
        if self.has_winner():
            return True
        else:
            for rows in self.board.board:
                for char in rows:
                    if char == None:
                        return False
            return True

    def has_winner(self):
        for i in Game.CELLS:
            if self.board.get_row(i) == ['X', 'X', 'X'] or self.board.get_column(i) == ['X', 'X', 'X']:
                self.winner = 'X'
            elif self.board.get_row(i) == ['O', 'O', 'O'] or self.board.get_column(i) == ['O', 'O', 'O']:
                self.winner = 'O'
        
        if self.board.get_diagonal(0) == ['X', 'X', 'X'] or self.board.get_diagonal(1) == ['X', 'X', 'X']:
            self.winner = 'X'
        elif self.board.get_diagonal(0) == ['O', 'O', 'O'] or self.board.get_diagonal(1) == ['O', 'O', 'O']:
            self.winner = 'O'
        
        if self.winner != None:
            return True
        return False
        
    def is_tied(self):
        if self.is_finished() and self.has_winner() is False:
            return True

    def get_winner(self):
        return self.winner

    def next_turn(self):
        return self.turn

    def move(self, player, row, col):
        if row not in Game.CELLS or col not in Game.CELLS: 
            raise InvalidMovementException("Move not on board")        
        elif self.board.board[row][col] != None:
            raise InvalidMovementException("Spot is taken")
        elif self.is_finished():
            raise InvalidMovementException("Game is finished!  Can't make a move.")
        elif player != self.turn:
            raise InvalidMovementException("It is not your turn.")
        else: 
            self.board.move(player, row, col)
            if self.turn == self.player_1:
                self.turn = self.player_2
            elif self.turn == self.player_2:
                self.turn = self.player_1
            else:
                raise InvalidMovementException("Hey, it's not your turn")
            

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
        my_board = [
            [None,None,None],
            [None,None,None],
            [None,None,None],
            ]
        
        if initial_board:
            self.board  = initial_board
        else:
            self.board = my_board

    def move(self, figure, row, col):
        self.board[row][col] = figure
        return self.board

    def __str__(self):
        my_board = []
        for row in self.board:
            for play in row:
                if play == None:
                    my_board.append('-')
                else: 
                    my_board.append(play)
            
        return BOARD_TEMPLATE.format(*my_board)

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        col_list = []
        for row in self.board:
            col_list.append(row[col_number])
        return col_list

    def get_diagonal(self, row_number):
        diag = []
        if row_number == 0:
            num = 0
            for row in self.board:
                diag.append(row[num])
                num += 1
        elif row_number == 1:
            num = 2
            for row in self.board:
                diag.append(row[num])
                num -= 1
        return diag
