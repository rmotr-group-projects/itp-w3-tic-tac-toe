class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board=board  
        self.turn_count=1
        self.p1=player_1
        self.p2=player_2
        self.current_p=self.p1
        self.winning_condition = [['X','X','X'],['O','O','O']]

    def is_finished(self):
        #check all end game conditions
        '''
        for i in [self.p1,self.p2]:
            for j in range(0,3):
                if self.board.get_row(j)==[i,i,i]:
                    return True
            for k in range(0,3):
                if self.board.get_column(k)==[i,i,i]:
                    return True   
            for l in range(0,2):
                if self.board.get_diagonal(l)==[i,i,i]:
                    return True 
'''                    
        if self.is_tied() or self.has_winner():
            return True
        else:
            return False

    def has_winner(self):
        return self.get_winner() is not None

    def is_tied(self):
        for row in range(3):
            for col in range(len(self.board.initial_board[row])):
                if None in self.board.initial_board[row]:
                    return False
                else:
                    return True

    def get_winner(self):
        winning_condion = [['X','X','X'],['O','O','O']]
        for i in range(2):
            if self.board.get_diagonal(i) in self.winning_condition:
                return self.board.get_diagonal(i)[0]
        for i in range(3):
            if self.board.get_row(i) in self.winning_condition:
                return self.board.get_row(i)[0]
        for i in range(3):
            if self.board.get_column(i) in self.winning_condition:
                return self.board.get_column(i)[0]
        pass

    def next_turn(self):
        if self.turn_count%2==0:
            self.current_p=self.p2
            return self.p2
        else:
            self.current_p=self.p1            
            return self.p1

    def move(self, player, row, col):
        if player!=self.current_p:
            raise InvalidMovementException
        if row >2 or row <0 or col > 2 or col <0:
            raise InvalidMovementException
        if self.is_tied() or self.has_winner():  
            raise InvalidMovementException
        self.turn_count+=1
        self.board.move(player,row,col)
        
        


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
from exceptions import InvalidMovementException
from copy import deepcopy

class Board(object):
    def __init__(self, initial_board=None):
        '''
        self.initial_board = initial_board
        if self.initial_board == None:
            self.initialboard = self.initial_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
            '''
            
        if initial_board:
            self.initial_board=initial_board
            
            
        else:
            self.initial_board=[[None, None, None], [None, None, None], [None, None, None]]            
        
        

    def move(self, figure, row, col):
        if self.initial_board[row][col]=='X' or self.initial_board[row][col]=='O':
            raise InvalidMovementException
        else:
            self.initial_board[row][col]=figure

    def __str__(self):
        self.nice_board = deepcopy(self.initial_board)
        for row in range(3):
            for col in range(len(self.nice_board[row])):
                if self.nice_board[row][col] == None:
                    self.nice_board[row][col] ='-'
        return BOARD_TEMPLATE.format(self.nice_board[0][0],self.nice_board[0][1],self.nice_board[0][2],
                                     self.nice_board[1][0],self.nice_board[1][1],self.nice_board[1][2],
                                     self.nice_board[2][0],self.nice_board[2][1],self.nice_board[2][2])        
    


    def get_row(self, row_number):
        a=[]
        #for i in self.initial_board[row_number]:
        #    a.append(i)
        return self.initial_board[row_number]

    def get_column(self, col_number):
        self.col_number = col_number
        self.col_display = []
        for i in range(3):
            self.col_display.append(self.initial_board[i][col_number])
        return self.col_display
         

    def get_diagonal(self, row_number):
        a=[]
        if row_number==0:
            a.append(self.initial_board[0][0])
            a.append(self.initial_board[1][1])
            a.append(self.initial_board[2][2])
        else:
            a.append(self.initial_board[0][2])
            a.append(self.initial_board[1][1])
            a.append(self.initial_board[2][0])
        return a  
 