import pygame
import math
import numpy as np
import sys


#costants
WIDTH=800
HEIGHT=WIDTH
LINE_WIDTH=15
BOARD_ROWS=3
BOARD_COLS=3
SQUARE_SIZE=WIDTH//BOARD_COLS
CIRCLE_RADIUS=SQUARE_SIZE//3
CIRCLE_WIDTH=15
CROSS_WIDTH=25
SPACE=SQUARE_SIZE//4

#rgb:red green blue
BG_COLOR=(28,170,156)
LINE_COLOR=(23,145,135)
CIRCLE_COLOR=(239,231,200)
CROSS_COLOR=(66,66,66)

pygame.init()

#screen settings
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

#board
board=np.zeros((BOARD_ROWS,BOARD_COLS))

#draws 4 lines of the board
def draw_lines():
	#horizotal
	pygame.draw.line(screen,LINE_COLOR,(0,SQUARE_SIZE),(WIDTH,SQUARE_SIZE),LINE_WIDTH)
	pygame.draw.line(screen,LINE_COLOR,(0,2*SQUARE_SIZE),(WIDTH,2*SQUARE_SIZE),LINE_WIDTH)

	#vertical
	pygame.draw.line(screen,LINE_COLOR,(SQUARE_SIZE,0),(SQUARE_SIZE,HEIGHT),LINE_WIDTH)
	pygame.draw.line(screen,LINE_COLOR,(2*SQUARE_SIZE,0),(2*SQUARE_SIZE,HEIGHT),LINE_WIDTH)

#draws circle-player1::cross-player2
def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col]==1:
				pygame.draw.circle(screen, CIRCLE_COLOR ,(int(col*SQUARE_SIZE+SQUARE_SIZE//2),int(row*SQUARE_SIZE+SQUARE_SIZE//2)),CIRCLE_RADIUS,CIRCLE_WIDTH)

			elif board[row][col]==2:
				pygame.draw.line(screen,CROSS_COLOR,(col*SQUARE_SIZE+SPACE,row*SQUARE_SIZE+SQUARE_SIZE-SPACE),(col*SQUARE_SIZE+SQUARE_SIZE-SPACE,row*SQUARE_SIZE+SPACE),CROSS_WIDTH)
				pygame.draw.line(screen,CROSS_COLOR,(col*SQUARE_SIZE+SPACE,row*SQUARE_SIZE+SPACE),(col*SQUARE_SIZE+SQUARE_SIZE-SPACE,row*SQUARE_SIZE+SQUARE_SIZE-SPACE),CROSS_WIDTH)


#for marking the squares of the console board
def mark_square(row,col,player):
	board[row][col]=player

#for checking if a particular square is available or not
def availabe_square(row,col):
	return board[row][col]==0

#for checking if the board is full or not
def is_board_full():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col]==0:
				return False
	return True

#checks if the player passed in the function wins
def check_win(player):
	#check vertical win
	for col in range(BOARD_COLS):
		if board[0][col]==player and board[1][col]==player and board[2][col]==player:
			draw_vertical_winning_line(col,player)
			return True

	#check horizontal win
	for row in range(BOARD_ROWS):
		if board[row][0]==player and board[row][1]==player and board[row][2]==player:
			draw_horizontal_winning_line(row,player)
			return True

	#check asc diagonal win
	if board[2][0]==player and board[1][1]==player and board[0][2]==player:
		draw_asc_diagonal(player)
		return True

	#check desc diagonal win
	if board[0][0]==player and board[1][1]==player and board[2][2]==player:
		draw_desc_diagonal(player)
		return True

	#No win
	return False

#functions for drawing the winning lines	

#draws a vertical winning line
def draw_vertical_winning_line(col,player):
	posX=col*SQUARE_SIZE+SQUARE_SIZE//2
	if player==1:
		color=CIRCLE_COLOR
	elif player==2:
		color=CROSS_COLOR

	pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)

#draws a horizontal winning line
def draw_horizontal_winning_line(row,player):
	posY=row*SQUARE_SIZE+SQUARE_SIZE//2
	if player==1:
		color=CIRCLE_COLOR
	elif player==2:
		color=CROSS_COLOR

	pygame.draw.line(screen,color,(15,posY),(WIDTH-15,posY),15)

#draws a winning line through the ascending diagonal
def draw_asc_diagonal(player):
	if player==1:
		color=CIRCLE_COLOR
	elif player==2:
		color=CROSS_COLOR

	pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)

#draws a winning line through the descending diagonal
def draw_desc_diagonal(player):
	if player==1:
		color=CIRCLE_COLOR
	elif player==2:
		color=CROSS_COLOR

	pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)

#restarts the game
def restart():
	screen.fill(BG_COLOR)
	draw_lines()
	player=1
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col]=0

#finction call for drawing the board lines
draw_lines()

player=1
game_over=False

#main loop
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()

		#to start the game
		if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
			mouseX=event.pos[0]#x
			mouseY=event.pos[1]#y

			clicked_row=int(mouseY//SQUARE_SIZE)
			clicked_col=int(mouseX//SQUARE_SIZE)

			if availabe_square(clicked_row,clicked_col):
				mark_square(clicked_row,clicked_col,player)
				if check_win(player):
					game_over=True
				player=player%2+1

				draw_figures()

		#to restart the game
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_r:
				restart()
				game_over=False

	#for updating the display
	pygame.display.update()
