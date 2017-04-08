from .exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.current_player = player_1

    def is_finished(self):
        if self.has_winner():
            return True
        count = 0
        temp = []
        temp.append(self.board.get_row(0))
        temp.append(self.board.get_row(1))
        temp.append(self.board.get_row(2))
        for rows in temp:
            for col in rows:
                if col == self.player_1 or col == self.player_2:
                    count += 1
        if count >= 9:
            return True
        return False

    def has_winner(self):
        if self.get_winner() == None:
            return False
        else:
            return True

    def is_tied(self):
        if self.is_finished() and self.has_winner() == False:
            return True
        else:
            return False

    def get_winner(self):
        winner = None
        temp = []
        temp.append(self.board.get_row(0))
        temp.append(self.board.get_row(1))
        temp.append(self.board.get_row(2))
        for rows in temp:#Horizontal
            if rows.count(self.player_1) == 3:
                winner = self.player_1
            elif rows.count(self.player_2) == 3:
                winner = self.player_2
        for i in range(0, 2):#vertical
            if temp[0][i] == temp[1][i] and temp[1][i] == temp[2][i]:
                if temp[0][i] == self.player_1:
                    winner = self.player_1
                elif temp[0][i] == self.player_2:
                    winner = self.player_2
        if self.board.get_diagonal(0)[0] == self.board.get_diagonal(0)[1] and self.board.get_diagonal(0)[1] == self.board.get_diagonal(0)[2]:#diagonal l to r
            if self.board.get_diagonal(0)[0] == self.player_1:
                winner = self.player_1
            elif self.board.get_diagonal(0)[0] == self.player_2:
                winner = self.player_2
        if self.board.get_diagonal(1)[0] == self.board.get_diagonal(1)[1] and self.board.get_diagonal(1)[1] == self.board.get_diagonal(1)[2]:#diagonal r to l
            if self.board.get_diagonal(1)[2] == self.player_1:
                winner = self.player_1
            elif self.board.get_diagonal(1)[2] == self.player_2:
                winner = self.player_2
        return winner

    def next_turn(self):
        return self.current_player

    def move(self, player, row, col):
        if row not in range(3) or col not in range(3):
            raise InvalidMovementException()
        elif self.is_finished():
            raise InvalidMovementException()
        elif self.board.get_row(row)[col] != None:
            raise InvalidMovementException()
        elif player != self.current_player:
            raise InvalidMovementException()
        elif self.current_player == self.player_1:
            self.board.move(player, row, col)
            self.current_player = self.player_2
        elif self.current_player == self.player_2:
            self.board.move(player, row, col)
            self.current_player = self.player_1
        return self.current_player

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
        if not initial_board:
            self.complete_board = [ [initial_board ]*3, [initial_board]*3, [initial_board]*3]
        else:
            self.complete_board = initial_board
        
    def move(self, figure, row, col):
        self.complete_board[row][col] = figure
        
    def __str__(self):
        answer = []
        for rows in self.complete_board:
            for col in rows:
                if col == None:
                    answer.append('-')
                else:
                    answer.append(col)
        
        return BOARD_TEMPLATE.format(*answer) 

    def get_row(self, row_number):
        return self.complete_board[row_number]

    def get_column(self, col_number):
        columbus = []
        for i in self.complete_board:
            columbus.append(i[col_number])
        return columbus

    def get_diagonal(self, row_number):
        if row_number == 0:
            positions = [(0, 0), (1, 1),(2, 2),]
        elif row_number ==1:
            positions = [(0, 2), (1, 1), (2, 0),]
        diagonal = []
        for position in positions:
            row = position[0]
            col = position[1]
            diagonal.append(self.complete_board[row][col])
        return diagonal 
