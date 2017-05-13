from tic_tac_toe.exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        # Set up the board and players
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        # Set winner status and current player
        self.winner = None
        self.current_player = None

    def is_finished(self):
        # Number of rows/columns for win check, empty move list for tie check
        rows_and_cols = [0, 1, 2]
        move_list = []
        tie_result = None
        
        for num in rows_and_cols:
            # Sets only have 1 of each unique item, so if a set length is 1 and it's not None it must be a winner
            # Convert each type (row, column or diagonal) to a set then check if it's None
            # If it is, set the winner to the corresponding player
            if len(set(self.board.get_row(num))) == 1 and None not in set(self.board.get_row(num)):
                if self.player_1 in set(self.board.get_row(num)):
                    self.winner = self.player_1
                else:
                    self.winner = self.player_2
            elif len(set(self.board.get_column(num))) == 1 and None not in set(self.board.get_column(num)):
                if self.player_1 in set(self.board.get_column(num)):
                    self.winner = self.player_1
                else:
                    self.winner = self.player_2
            elif len(set(self.board.get_diagonal(num))) == 1 and None not in set(self.board.get_diagonal(num)):
                if self.player_1 in set(self.board.get_diagonal(num)):
                    self.winner = self.player_1
                else:
                    self.winner = self.player_2
        
        # If there's no winner, go through each row and check if there's a None
        # If None is not in any row or column that must mean each position is filled
        if self.winner == None:
            for row in self.board.board:
                for move in row:
                    move_list.append(move)
            if None not in move_list:
                tie_result = True
            else:
                tie_result = False
        
        # If there's a winner or a tie, the game is over
        if self.winner != None or tie_result is True:
            return True
        else:
            return False

    def has_winner(self):
        # Check the winner status
        if self.winner != None:
            return True
        else:
            return False

    def is_tied(self):
        # Check the tie status
        if self.is_finished() is True:
            if self.winner is None:
                return True
            else:
                return False

    def get_winner(self):
        # If the game has a winner return the winner's character
        if self.has_winner() is True:
            return self.winner

    def next_turn(self):
        # Set the curren tplayer based on the last player who moved (or if it's the first turn)
        if self.current_player is None:
            self.current_player = self.player_1
        elif self.current_player == self.player_2:
            self.current_player = self.player_1
        else:
            self.current_player = self.player_2
        return self.current_player

    def move(self, player, row, col):
        # Check that the player making a move is on their turn
        # Check that the move is valid
        # Call the board's move method and pass the values over
        if player != self.current_player:
            raise InvalidMovementException
        elif (row > 2 or row < 0) or (col > 2 or col < 0):
            raise InvalidMovementException
        elif self.board.board[row][col] != None:
            raise InvalidMovementException
        elif self.winner != None or self.is_tied() is True:
            raise InvalidMovementException
        else:
            self.board.move(player, row, col)


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
        # Hardcode None for empty board, otherwise accept board argument
        if initial_board == None:
            self.board = [[None, None, None],
                          [None, None, None],
                          [None, None, None]]
        else:
            self.board = initial_board
        

    def move(self, figure, row, col):
        # Rows and columns = 0, 1, 2, figure = X or O
        self.board[row][col] = figure


    def __str__(self):
        # Return template and insert figures based on moves made
        move_list = []
        for row in self.board:
            for move in row:
                move_list.append(move)
                
        for pos, move in enumerate(move_list):
            # Update move_list based on None position, replace with the -
            if move == None:
                move_list[pos] = '-'
                
        # Hardcoded individual positions        
        return BOARD_TEMPLATE.format(move_list[0],
        move_list[1], move_list[2], move_list[3], 
        move_list[4], move_list[5], move_list[6],
        move_list[7], move_list[8])

    def get_row(self, row_number):
        return self.board[row_number]

    def get_column(self, col_number):
        # Return all items in the given column
        column_list = []
        for row in self.board:
            column_list.append(row[col_number])
        return column_list

    def get_diagonal(self, row_number):
        # Return all items in the given diagonal
        diag_list = []
        # First diag, run a count and add for each row
        if row_number == 0:
            count = 0
            for row in self.board:
                diag_list.append(row[count])
                count += 1
        else:
            # Second diag, reverse count and count down
            count = 2
            for row in self.board:
                diag_list.append(row[count])
                count -= 1
        return diag_list