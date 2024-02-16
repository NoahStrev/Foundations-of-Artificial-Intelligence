# Tic Tac Toe possibility

board= [ ' ' for x in range (9) ]


def spaceIsFree(pos):
    if board[pos] == ' ' :
        return True
    else:
        return False
        

def printBoard(board):
    print() 
    print (' ', board[0], ' | ', board[1], ' | ', board[2])
    print ('==========')  
    print (' ', board[3], ' | ', board[4], ' | ', board[5])
    print ('==========')   
    print (' ', board[6], ' | ', board[7], ' | ', board[8])
    print()
    

def isWinner (board, marker ) :
    # check the three rows across
    if board[0] == board[1] == board[2] == marker: # parentheses may change result!
        return True
    if board[3] == board[4] == board[5] == marker :
        return True
    if board[6] == board[7] == board[8] == marker:
           return True
    # check the three columns down
    if board[0] == board[3] == board[6] == marker:
           return True
    if board[1] == board[4] == board[7] == marker:
           return True
    if board[2] == board[5] == board[8] == marker:
           return True
    #check the diagonals
    if board[0] == board[4] == board[8] == marker:
           return True
    if board[2] == board[4] == board[6] == marker:
           return True
    else:
            return False


def playerMove():  # player is 'O'
    needValidMove = True
    while needValidMove:
        move = input('What is your move? Enter a position 0 through 8:')
        try:
            move = int(move)
            if move >= 0 and move < 9:
                # is the position available?
                if spaceIsFree(move):
                    board[move] = 'O'
                    needValidMove = False
                else:
                    print ('Sorry, that position is already taken!')
            else:
                print ('Invalid move -- does not exist!')
        except:
            print('Invalid move')
    


                    

def computerMove():
    #print('okedoke')
    # make a copy of the board

    # check to see if we can win
    for pos, m in enumerate(board):
        boardCopy = board[:]
        # print('BOARD COPY')
        # printBoard(boardCopy)
        
        #print(pos, '  ', m)
        if m == ' ':
            # will we win if place our marker in position pos
            boardCopy [pos] = 'X'
            if isWinner(boardCopy, 'X'):
                board[pos] = 'X'
                return

     # we cannot win this move, but could we lose on the next move of the player?
    for pos, m in enumerate(board):
        boardCopy = board[:]
        # print('BOARD COPY')
        # printBoard(boardCopy)
        
        #print(pos, '  ', m)
        if m == ' ':
            # will player win if place their marker in position pos
            boardCopy [pos] = 'O'
            if isWinner(boardCopy, 'O'):
                board[pos] = 'X'
                return

    # cannot win cannot yet lose, so play a "square"
    play_pos = board.index(' ')
    board[play_pos] = 'X'
    return


def isBoardFull(board):
    for i in range(9):
        if board[i] == ' ':
            return False
    # optionally could just if board.count(' ') == 0 return True else return False
    return True


def main():
    print(' * * *   WELCOME TO TIC*TAC*TOE  * * * ')
    print( ' ..... explain the game and the numbering of the board, etc. etc. ')

    printBoard(board)
  # debugging  print(isWinner (board, 'X'))

    # who moves first?? assume the human player
    whoseMove = 'O'
    while True:
       if isWinner(board, 'X'):
           print ('X has won! ')
           return

       if isWinner(board, 'O'):
           print ('O has won!')
           return

       if isBoardFull(board):
           print ("It is CATS -- a tie game! ")
           return

       if whoseMove == 'O':
           playerMove()
           whoseMove = 'X'
       else:
            computerMove()
            whoseMove = 'O'
            
       printBoard(board)
       
       
            

main()
print ('Thanks for playing Tic*Tac*Toe!')
       
