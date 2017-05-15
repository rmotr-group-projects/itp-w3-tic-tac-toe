from .exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board   # self.board = The instance of the board class that they made in the test
        self.player_1 = player_1
        self.player_2 = player_2
        self.next_player = self.player_1
    # print(self.board)
    # <__main__.object at 0xFFt4t>
    # print(self.board.board)
    # [[None, None, None]], [None, None, None], [None, None, None]]

    def is_finished(self):
        if (self.has_winner() == False and 
        self.is_tied() == False):
            return False
        else:
            return True
        
    def has_winner(self):
        if self.get_winner():
            return True
        else:
            return False

    def is_tied(self):
        for x in range(3):
            for o in range(3):
                if self.board.initial_board[x][o] is None:
                    return False
        return True
        
        
    def get_winner(self):
        #if self.board.get_row(row_number)[0] == self.board.get_row(row_number)[1] == self.board.get_row(row_number)[2]:
            #return True
        #elif self.board.get_column(col_number)[0] == self.board.get_column(col_number)[1] == self.board.get_column(col_number)[2]:
            #return True
        #elif self.board.get_diagonal(row_number)[0] == self.board.get_diagonal(row_number)[1] == self.board.get_diagonal(row_number)[2]:
            #return True
        #else:
            #return False
        
        x_win = ['X', 'X', 'X']
        o_win = ['O', 'O', 'O']
        
        for x in range(3):
            if (self.board.get_row(x) == x_win or
            self.board.get_column(x) == x_win or
            self.board.get_diagonal(x) == x_win):
                return 'X'
                
        for o in range(3):
            if (self.board.get_row(o) == o_win or
            self.board.get_column(o) == o_win or
            self.board.get_diagonal(o) == o_win):
                return 'O'
        
        return None
        
            
    def next_turn(self):
        return self.next_player

    def move(self,player,row,col):
        if player != self.next_player:
            raise InvalidMovementException()
        elif row not in range(3) or col not in range(3): #valid positions [0, 1, 2]
            raise InvalidMovementException()
                #if position_is_already_taken:
                #raise InvalidMovementException()
        elif self.board.initial_board[row][col] is not None:
            raise InvalidMovementException()
        elif self.is_finished():
            raise InvalidMovementException()
        else:
             self.board.move(player, row, col)
            
        if player == "X":
            self.next_player = "O"
        elif player == "O":
            self.next_player = "X"


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
            self.initial_board = (
                [None, None, None],
                [None, None, None],
                [None, None, None])
        else:
            self.initial_board = initial_board
        
    def move(self, figure, row, col):
        self.initial_board[row][col] = figure

    def __str__(self):
        return BOARD_TEMPLATE.format(*(item or '-' for element in self.initial_board for item in element))

    def get_row(self, row_number):
        return self.initial_board[row_number]

    def get_column(self, col_number):
        col_list = []
        for row in self.initial_board:
            col_list.append(row[col_number])
        return col_list
        
        #return [self.initial_board[i][col_number] 
        #for i, item in enumerate(self.initial_board)]

    def get_diagonal(self, row_number):


        diagonal = []
        left_diagonal_index = 0
        right_diagonal_index = 2
        
        if row_number == 0:
            for row in self.initial_board:
                diagonal.append(row[left_diagonal_index])
                left_diagonal_index += 1
        
        if row_number == 1:
            for row in self.initial_board:
                diagonal.append(row[right_diagonal_index])
                right_diagonal_index -= 1
            
        return diagonal
        
        #       diag = []
        
        # if row_number == 0:
        #     for spot, item in enumerate(self.initial_board):
        #         diag.append(self.initial_board[spot][spot])
                
        # elif row_number == 1:
        #     diag.append(self.initial_board[0][2])
        #     diag.append(self.initial_board[1][1]) 
        #     diag.append(self.initial_board[2][0])
        
        #return diag
    
          #PYTHONPATH=. py.test tests/test_board.py::BoardTestCase::test_make_move_on_board



"""
>>> 0 == False
True
>>> 1 == True
True
>>> 

>>> 'X' or '-'
'X'
>>> None or '-'
'-'
>>> 'O' or '-'
'O'
>>> True or False
True
>>> False or True
True
>>> 




>>> class Game(object):
	def __init__(self, board):
		print(board)
		self.board = board

	
>>> class Game(object):
	def __init__(self, board):
		print(board)
		self.board = board
	def new_board(self, first, second, third):
		self.board = [first, second, third]

		
>>> mylist  = Board()
>>> print(board)
<__main__.Board object at 0x03A88590>
>>> print(board.mylist)
['X', 'O', None]


>>> new_game = Game(mylist)
# printing mylist
<__main__.Board object at 0x03A88590>
>>> 

"""