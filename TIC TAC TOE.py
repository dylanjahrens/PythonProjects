#STEP 1: BOARD
def display_board(board):
	print(board[1]+'|' +board[2]+'|' +board[3])
	print('-----')
	print(board[4]+'|' +board[5]+'|' +board[6])
	print('-----')
	print(board[7]+'|' +board[8]+'|' +board[9])
#for this to run board needs to be assigned a list of 10 STRINGS, indexed through 9


#STEP 2: ASSIGNING X AND O TO PLAYERS 1 AND 2
def xo_assignments():
	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input('Player 1, choose X or O: ').upper()
	player1 = marker
	#Marker is either X or O
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'
	return(player1, player2) #Tuple


#STEP 3: PLACING THE MARKS ON THE SQUARES OF THE BOARD
def square_marker(board, marker, position):
	#board needs to defined as a list of 10 strings
	#marker is a 'string' X or O assigned to players and needs to be defined
        board[position] = marker
        #"TypeError: 'tuple' object does not support item assignment"

#STEP 4: CHECKING THE GAME FOR A WINNER
def winnercheck(board,pick):
	return((board[1] == pick and board[2] == pick and board[3] == pick) or #across the top
	(board[4] == pick and board[5] == pick and board[6] == pick) or #across the middle
	(board[7] == pick and board[8] == pick and board[9] == pick) or #across the bottom
	(board[1] == pick and board[4] == pick and board[7] == pick) or #down the left
	(board[2] == pick and board[5] == pick and board[8] == pick) or #down the middle
	(board[3] == pick and board[6] == pick and board[9] == pick) or #down the right
	(board[1] == pick and board[5] == pick and board[9] == pick) or #diagonal
	(board[3] == pick and board[5] == pick and board[7] == pick)) #diagonal

#STEP 5: RANDOMLY ASSIGNING WHO GOES FIRST
import random 
def goes_first():
	if random.randint(1,2) == 1:
		return 'Player 1 goes first'
	else:
		return 'Player 2 goes first'

#STEP 6: A CHECK TO DETERMINE IF A SPACE ON THE BOARD IS AVAILABLE
def availability_check(board, position):
	return board[position] == ' ' #RETURNS BOOLEAN

#STEP 7: A CHECK TO DETERMINE IF THE BOARD IS FULL
def fullboard_check(board):
	if ' ' in board:
		return False
	else:
		return True

#JOSE'S BOARD CHECK -- ASSUMING THE LIST IS NOT FULL TO BEGIN WITH
def full_board_check(board):
    for i in range(1,10):
        if availability_check(board, i):
            return False #If the board is not full
    return True

#STEP 8: PLAYER SELECTS THEIR POSITION, KEEPS ASKING UNTIL THEY PICK AN OPEN SPACE OR A LEGIT CHOICE
def player_choice(board):
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9] or not availability_check(board, position):
		position = int(input('Please choose your board position (1-9): '))
	return position

#STEP 9: ASKING THE PLAYER IF THEY'D LIKE TO PLAY AGAIN
def replay():
	return input('Do you want to play again? Enter yes or no: ').lower()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#FULL GAME FUNCTION


print('Welcome to Tic Tac Toe!')

while True:
    ttt_board = [' ']*10
    player1_marker, player2_marker = xo_assignments()
    turn = goes_first()
    print(turn)

game_on = True

while game_on:
	if turn == 'Player 1 goes first': #Player 1's turn
        #print display board
		display_board(ttt_board)
        #choose a spot
		position = player_choice(ttt_board)
		square_marker(ttt_board, player1_marker, position)
        #win check
		if winnercheck(ttt_board,pick):
			display_board(ttt_board)
			print('Player 1 has won the game!')
			game_on = False
        #tie check
		else:
			if full_board_check(ttt_board):
			     display_board(ttt_board)
			     print('The game is a tie!')
			     break
			else:
			     turn = 'Player 2 goes first'

	else: #Player 2's turn
	#print display board
		display_board(ttt_board)
        #choose a spot
		position = player_choice(ttt_board)
		square_marker(ttt_board, player2_marker, position)
        #win check
		if winnercheck(ttt_board,pick):
			display_board(ttt_board)
			print('Player 1 has won the game!')
			game_on = False
        #tie check
		else:
			if full_board_check(ttt_board):
			     display_board(ttt_board)
			     print('The game is a tie!')
			     break
			else:
			     turn = 'Player 2 goes first'
	if not replay():
		break
