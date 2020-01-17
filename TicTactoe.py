
def display_board(board):    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def checkforwin(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal



def space_check(board, position):
    
    return board[position] == ' '

def player_choice(board):
    # Using strings because of raw_input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        
        position = input('Choose your next position: (1-9) ')
    return int(position)


def checkfullboard(theBoard):
    for i in range(1,10):
        if (space_check(theBoard,i)):
            return False

    return True


def inserting(theBoard,mark,position):
    theBoard[position] = mark
    return theBoard






def main_fn():
    print('Welcome to Tic Tac Toe!')

    while True:
        # Reset the board
        theBoard = [' '] * 10
        #player1_marker, player2_marker = player_input()
        #turn = choose_first()
       # print(turn + ' will go first.')
       
        game_on = True
        turn  = 'Player 1'

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.
                mark = 'X'
                display_board(theBoard)
                position = player_choice(theBoard)
                inserting(theBoard, mark, position)

                if checkforwin(theBoard, mark):
                    display_board(theBoard)
                    print('Player 1 Wins')
                    
                    game_on = False
                    break
                else:
                    if checkfullboard(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.
                mark = '0'
                display_board(theBoard)
                position = player_choice(theBoard)
                inserting(theBoard, mark, position)

                if checkforwin(theBoard, mark):
                    display_board(theBoard)
                    print('Player 2 has won!')
                    game_on = False
                    break
                else:
                    if checkfullboard(theBoard):
                        display_board(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 1'

        return False
main_fn()
