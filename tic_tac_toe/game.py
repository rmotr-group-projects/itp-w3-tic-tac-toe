class tic_tac(object):
    def __init__(self, board=None, name='my_board'):
        self.board = board
        self.name = name
    def move(self, player, row, column):
        if not self.board:
            board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
            ]
        else:
         if not self.board[row][column]:
                self.board[row][column] = player
         else:
                return "Place already chosen"
        
    def get_row(self, row):
        return self.board[row]
    
    def get_column(self, column):
        column_list = []
        for i in range(3):
            column_list.append(self.board[i][column])
        return column_list      
            
    def get_diagonals(self, num=None):
        if num == 0:
            diagonal = [self.board[0][0], self.board[1][1], self.board[2][2]]
            return diagonal
            
        elif num == 1 or num == 2:
            diagonal = [self.board[0][2], self.board[1][1], self.board[2][0]]
            return diagonal
            
        else:
            return "Invalid diagonal!" 
            
    def __str__(self):
        return board.name
            
class Game(object):
    def __init__(self, board, player_1, player_2):
        self.board = board
        pass
        
    def get_winning_lists(self):
        win_list = []
        for i in range(3):
            win_list.append(board.get_row(i))
            win_list.append(board.get_column(i))
        win_list.append(board.get_diagonals(0))
        win_list.append(board.get_diagonals(1))
        return win_list
        
        
    def check_equal(self, list):
        if list[0]==list[1] and list[0]==list[2] and list[0] != None :
            return {'info' : [True, list[0]]}
        else:
            return {'info' : [False]}
            
    def haswinner(self):
       for i in range(2):
           if self.check_equal(board.get_row(i))['info'][0] or self.check_equal(board.get_column(i))['info'][0] or self.check_equal(board.get_diagonals(i))['info'][0]:
               return True 
           else:
               return False
    
    def istied(self):
        no_cases_left = True
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == None:
                    no_cases_left = False
                else:
                    pass
        if no_cases_left and not self.haswinner():
            return True
        else:
            return False
            
    def is_finished(self):
        if self.istied() or self.haswinner:
            return True
        else:
            return False
            
    def get_winner(self):
        for i in range(8):
            temp = self.check_equal(self.get_winning_lists()[i])
            if temp['info'][0] == True:
                return temp['info'][1]
            else:
                pass
                
    def next_turn(self):
        count_x = 0
        count_y = 0
        
        for i in board.board:
            for j in i:
                if j == 'X':
                    count_x += 1
                elif j == 'Y':
                    count_y += 1 
                else:
                    pass
                    
        if count_x == count_y:
            return 'X'
        elif count_x > count_y:
            return 'Y'
        else:
            pass