import random

board = list(range(0,9))


def display_board() : 
   print (board[0], '|', board[1], '|',board[2])
   print ('----------')
   print (board[3], '|', board[4], '|',board[5])
   print ('----------')
   print (board[6], '|', board[7], '|',board[8])

display_board()

def check_row():
    row_1 = board[0] == board[1] == board[2]
    row_2 = board[3] == board[4] == board[5]
    row_3 = board[6] == board[7] == board[8]
    if row_1 or row_2 or row_3:
        return True

def check_column():
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        return True

def check_diagonals():
    diagonals_1 = board[0] == board[4] == board[8]
    diagonals_2 = board[6] == board[4] == board[2]
    if diagonals_1 or diagonals_2:
       return True
        
def checkAll():
    if check_row():
        return True
        
    if check_column():
        return True
        
    if check_diagonals():
        return True
        
    if board[0] == 0 or board[1] == 1 or board[2] == 2 or board[3]==3 or board[4] ==   4 or board[5]==5 or board[6]==6 or board[7]==7 or board[8]==8 :
        return False
    else:
        print ('Oops, game is a draw... Try Again?')
    display_board()

def play_game(): 
    while True:

        user_input = input("Select a Spot: ")
        choice = int(user_input)
        
        if board[choice] != 'o' and board[choice] != 'x':
            board[choice] = 'o'
            
            if checkAll() == True:
                print ("~~player WINS~~")
                break
            
            while True:
                random.seed() 
                computer = random.randint(0,8)
            
                if board[computer] != 'x' and board[computer] != 'o':
                    board[computer] = 'x'
                    
                    if checkAll() == True:
                        print ("~~computer WINS~~")
                        break
                    
                    break

        else:
            print ('Please choose another spot as this is taken')
        
        display_board()

play_game()
   
   
  
  