from .exceptions import InvalidMovementException


class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.next_player = self.player_1
        
    def is_finished(self):
        if (self.has_winner() is False and self.is_tied() is False):
            return False
        else:
            return True

    def has_winner(self):
        if self.get_winner() != None:
            return True
        else:
            return False

    def is_tied(self):
        for i in range(3):
            for j in range(3):
                if self.board.initial_board[i][j] is None:
                    return False
        return True

    def get_winner(self):
        all_x = ['X', 'X', 'X']
        all_o = ['O', 'O', 'O']
        
        # Winner is O
        for i in range(3):
            if (self.board.get_row(i) == all_o or 
                self.board.get_column(i) == all_o or 
                self.board.get_diagonal(i) == all_o):
                    return 'O'
        # Winner is X
        for j in range(3):
            if (self.board.get_row(j) == all_x or
                self.board.get_column(j) == all_x or 
                self.board.get_diagonal(j) == all_x):
                    return 'X'
        # No Winner; Tie
        return None
        
    def next_turn(self):
        return self.next_player
    
    def move(self, player, row, col):
        if player != self.next_player:
            raise InvalidMovementException()
        if row not in range(3) or col not in range(3):
            raise InvalidMovementException()
        if self.board.initial_board[row][col] != None: 
            raise InvalidMovementException()
        if self.is_finished() == True:
            raise InvalidMovementException()
       
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
        if initial_board == None:
            self.initial_board = [[None, None, None],
                                [None, None, None],
                                [None, None, None]]
        else:    
            self.initial_board = initial_board
        

    def move(self, figure, row, col):
        self.initial_board[row][col] = figure
        
    def __str__(self):
        return BOARD_TEMPLATE.format(self.initial_board[0][0] or '-', self.initial_board[0][1] or '-', self.initial_board[0][2] or '-',
                            self.initial_board[1][0] or '-', self.initial_board[1][1] or '-', self.initial_board[1][2] or '-',
                            self.initial_board[2][0] or '-', self.initial_board[2][1] or '-', self.initial_board[2][2] or '-')
        
    def get_row(self, row_number):
        return self.initial_board[row_number]

    def get_column(self, col_number):
        return [self.initial_board[i][col_number] for i, item in enumerate(self.initial_board)]

    def get_diagonal(self, row_number):
        new_diagonal = []
        if row_number == 0:
            for i, item in enumerate(self.initial_board):
                new_diagonal.append(self.initial_board[i][i])
                
        elif row_number == 1:
            
            new_diagonal.append(self.initial_board[0][2])
            new_diagonal.append(self.initial_board[1][1]) 
            new_diagonal.append(self.initial_board[2][0]) 
            
        return new_diagonal