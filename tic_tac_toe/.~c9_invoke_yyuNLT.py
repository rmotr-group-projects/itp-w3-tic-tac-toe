class Board(object):
    def __init__(self, initial_board = None):
        if initial_board == None:
            self.board = initial_board
        else:
            board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        self.board =
            
            
    def get_row(self, row_number):
        return self.board[row_number] # Simple
    
    def get_column(self, col_number):
        return [self.board[0][col_number], self.board[1]col_number, self.board[2]col_number]
    
    def get_diagonal(self, number):
        if number == 0:
            return self.board[0][0], self.board[1][1], self.board[2][2]
            elif number == 1:
                return [self.board[0][2], self.board[1][1], self.board[2][0]]
                