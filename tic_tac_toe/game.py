from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.next_player = player_1
        self.winner = None

    def is_finished(self):
        if self.has_winner() or self.is_tied():
            return True
        return False

    def has_winner(self):
        for i in range(3):
            if self.board.get_row(i)[0] and len(set(self.board.get_row(i)))==1:
                self.winner = self.board.get_row(i)[0]
                return True
            elif self.board.get_column(i)[0] and len(set(self.board.get_column(i)))==1:
                self.winner = self.board.get_column(i)[0]
                return True
        for j in range(2):
            if self.board.get_diagonal(j)[0] and len(set(self.board.get_diagonal(j)))==1:
                self.winner = self.board.get_diagonal(j)[0]
                return True
        return False

    def is_tied(self):
        flatboard = sum(self.board.board, [])
        if self.has_winner():
            return False
        if None in flatboard:
            return False
        return True

    def get_winner(self):
        return self.winner

    def next_turn(self):
        return self.next_player

    def move(self, player, row, col):
        if self.winner:
            raise InvalidMovementException("{} has won. No more moves".format(self.get_winner()))
        elif self.is_tied():
            raise InvalidMovementException("Game is tied, no more moves")
        elif player != self.player_1 and player != self.player_2:
            raise InvalidMovementException("Player selection is invalid, please pick {} or {}".format(self.player_1, self.player_2))
        elif player != self.next_player:
            raise InvalidMovementException("It is not {}'s turn, it is {}'s turn".format(player, self.next_turn()))
        elif row > 2 or row < 0 or col > 2 or col < 0:
            raise InvalidMovementException("This is move is not on the playing grid")    
        elif self.board.board[row][col]:
            raise InvalidMovementException("There is already a move here, place elsewhere")
        
        
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
            self.board = [[None, None, None],
                          [None, None, None],
                          [None, None, None]]
        else:
            self.board = initial_board

    def move(self, figure, row, col):
        self.board[row][col] = figure

    def __str__(self):
        stringboard = sum(self.board, []) #flattens the self.board list
        for index, item in enumerate(stringboard):
            if item == None:
                stringboard[index] = "-"
        return BOARD_TEMPLATE.format(*stringboard)

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
        
        elif row_number == 1:
            diagonal.append(self.board[0][2])
            diagonal.append(self.board[1][1])
            diagonal.append(self.board[2][0])
        
        return diagonal
            
