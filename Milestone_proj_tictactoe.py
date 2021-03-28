from Player_selection import Player_selection

def print_board():
	j=0
	for i in board:

		print(f'    {i[0]}\t|\t{i[1]}\t|  {i[2]}')
		if j<2:
			j+=1
			print('  ______|_______________|______')
	print('        |               |    ')


def game_over_check():
	#horizontal check 
	for i in board:
		if i[0]==i[1]==i[2]=='X' or i[0]==i[1]==i[2]=='O':
			print('must over the game')
			return i[0],True

	#vertical check 
	if board[0][0]==board[1][0]==board[2][0]=='X' or board[0][0]==board[1][0]==board[2][0]=='O':
		return board[0][0],True
	if board[0][1]==board[1][1]==board[2][1]=='X' or board[0][1]==board[1][1]==board[2][1]=='O':
		return board[0][1],True
	if board[0][2]==board[1][2]==board[2][2]=='X' or board[0][2]==board[1][2]==board[2][2]=='O':
		return board[0][2],True

	#diagonal check
	if board[0][0]==board[1][1]==board[2][2]=='X' or board[0][0]==board[1][1]==board[2][2]=='O':
		return board[0][0],True
	if board[0][2]==board[1][1]==board[2][0]=='X' or board[0][2]==board[1][1]==board[2][0]=='O':
		return board[0][2],True
	c=0
	for i in board:
		for j in i:
			if j not in ['']:
				c=c+1
	if c==9:
		return 'No',True
	else:
		return 'No',False


def choice(p,i):
	c='NOTHING'
	
	while c not in choice_dict:
		c=input(f'\nPlayer {i}: Pease select the position to enter {p} (1-9):\t')
		if c not in choice_dict:
			print('Please enter valid position!')
	i1,i2=choice_dict[c]
	while board[i1][i2] is not '':
		if board[i1][i2] is not '':
			print('That position is already occupied please enter another position: ')
		c=input(f'\nPlayer {i}: Pease select the position to enter \'{p}\' (1-9):\t')
		i1,i2=choice_dict[c]

	Winner,game_over=change_board(c,p)
	return Winner,game_over


def change_board(c,p):
	
	i1,i2=choice_dict[c]
	board[i1][i2]=p
	print_board()
	Winner,game_over=game_over_check()
	return Winner,game_over
	

def game_Start():
	user_input=''
	game_over=False
	Player1_chance=1
	Winner=''
	print('\nWelcome to TIC TAC TOE, All the best!!\n\n')
	player1,player2=Player_selection()
	print('Lets start!!')

	while not game_over:
		while Player1_chance==1:
			Winner,game_over=choice(player1,1)
			winner=1
			#print(game_over)
			Player1_chance=0
		if Player1_chance==0 and not game_over:
			Winner,game_over=choice(player2,2)
			#print(game_over)
			winner=2
			Player1_chance=1
	if Winner=='No':
		print('Game Tied, do you wanna play a new game?')
		
	else: 
		print(f'\nCongrtulation Player {winner} Won the game with \'{Winner}\' token!!!')	
		print('\n Do you wanna play a new game?')

	while user_input not in ['Y','N','n','y']:

		user_input=input('Press \'Y\' for yes and \'N\' for No: ').upper()
		if user_input not in ['Y','N','n','y']:
			print('Enter valid option!')
	if user_input=='Y':		
		return True
	else:
		print('\nOkay! Good Bye..')
		return False

	
#Global variables
board=[['' for x in range(3)] for y in range(3)]
choice_dict={'1':[0,0],'2':[0,1],'3':[0,2],'4':[1,0],'5':[1,1],'6':[1,2],'7':[2,0],'8':[2,1],'9':[2,2]}
restart=game_Start()
while restart:
	board=[['' for x in range(3)] for y in range(3)]
	restart=game_Start()


