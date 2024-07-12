import pygame, sys, random
from pygame import *
'''
block1 & rotations:
1:  [0,1,0] 2:  [0,0,0] 3:  [0,0,0] 4:  [0,0,0]
	[0,1,0]     [0,1,1]     [0,1,0]     [1,1,0]
	[0,0,0]     [0,0,0]     [0,1,0]     [0,0,0]
block2 & rotations:
1:  [0,1,0] 2:  [0,0,0] 3:  [0,0,0] 4:  [0,1,0]
	[0,1,1]     [0,1,1]     [1,1,0]     [1,1,0]
	[0,0,0]     [0,1,0]     [0,1,0]     [0,0,0]
block3 & rotations:
1:  [0,1,0] 2:  [0,1,0] 3:  [0,0,0] 4:  [0,1,0]
	[1,1,1]     [0,1,1]     [1,1,1]     [1,1,0]
	[0,0,0]     [0,1,0]     [0,1,0]     [0,1,0]
block4 & rotations:
1:  [0,1,0] 2:  [0,0,0] 
	[0,1,0]     [1,1,1]
	[0,1,0]     [0,0,0]
block5 & rotations:
1:  [0,1,0]
	[1,1,1]
	[0,1,0]
'''


# Initialize pygame
pygame.init()
 
# Define some colors
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (215,  60,  60)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 60, 215,  60)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 60,  60, 215)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (215, 215,   0)
ORANGE      = (195, 105,   0)
LIGHTORANGE = (255, 165,   0)
PURPLE      = (128,   0, 128)
LIGHTPURPLE = (188,  60, 188)

score = 0
WIDTH = 50 # This sets the WIDTH and HEIGHT of each grid location
HEIGHT = 50 # This sets the WIDTH and HEIGHT of each grid location
MARGIN = 5 # This sets the margin between each cell
down_shift = 280
WINDOW_SIZE = [280, 560] # Set the WIDTH and HEIGHT of the screen
cordx = 2 # X coordinate for moving "cursor" 
cordy = 2 # Y coordinate for moving "cursor" 
#board = [[0,0,0,0,0] for i in range(5)] # this was moved to the the main game loop
drop_succeed = False # Verify that a block was placed onto the board
game_over = False  # check for game over 
new_game = True # check if start of a new game
number_blocks = 5 # adjust which blocks spawn, 1-5. (eg. 4: 1-4 removes '+' block)

screen = pygame.display.set_mode(WINDOW_SIZE) # Make window
pygame.display.set_caption("Blocks Game") # Set title of screen
clock = pygame.time.Clock() # Used to manage how fast the screen updates

# Used for testing
def drawbcmd():
	global board
	for row in board:
		print(row)

class Block_Piece:
	# Define block attributes. 
	def __init__(self, shape=0, rotation=1, color=WHITE):
		self.shape = shape # What block it is 
		self.rotation = rotation # What orientation/rotation state 
		self.color = color # Color of the block, should be a tuple - could be removed?
		#self.error = "CAN'T PLACE BLOCK HERE"

	# Randomly select a block piece shape
	def get_shape(self):
		self.shape = random.randint(1,number_blocks) #  See blocks and rotation comments above for their shape. 
		# Each shape assigned a specific color
		if self.shape == 1: 
			self.color = "RED"
		elif self.shape == 2:
			self.color = "PURPLE"
		elif self.shape == 3:
			self.color = "GREEN"
		elif self.shape == 4:
			self.color = "ORANGE"
		elif self.shape == 5:
			self.color = "BLUE"

	# Adjust rotation attribute. Left 
	def rotate_left(self):
		if self.rotation  == 1:
			self.rotation = 4
		else:
			self.rotation -= 1

	# Adjust rotation attribute. Right
	def rotate_right(self):
		if self.rotation  == 4:
			self.rotation = 1
		else:
			self.rotation += 1

	# Attempt to add the block to the board. 
	# Function to display error message on invalid drop belongs here
	def drop_block(self, board, cordx, cordy):
		global drop_succeed
		# If the cursor is currently over a occupied space fail
		if board[cordy][cordx] != 0:
			#print("CAN'T PLACE BLOCK HERE")
			drop_succeed = False
			drop_succeed = False
		else:
			# Depending on block shape (1-5) follow the same basic 3 steps. 
			if self.shape == 1:
				# checks depend on current_piece shape's rotation
				if self.rotation == 1:
					# if cursor is at top of board, this shape/rotation combination will fail. 
					if cordy == 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					# if the space above cursor is ocupied, this will fail. (See block/rotation comment above for shape)
					elif board[cordy-1][cordx] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False     
					# Otherwise add this shape to board. (See block/rotation comment above for shape)
					else: 
						board[cordy][cordx] = 1
						board[cordy-1][cordx] = 1
						drop_succeed = True
				elif self.rotation == 2:
					if cordx == 4:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy][cordx+1] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 1
						board[cordy][cordx+1] = 1
						drop_succeed = True
				elif self.rotation == 3:
					if cordy == 4:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy+1][cordx] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 1
						board[cordy+1][cordx] = 1
						drop_succeed = True
				elif self.rotation == 4:
					if cordx == 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy][cordx-1] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 1
						board[cordy][cordx-1] = 1
						drop_succeed = True
			elif self.shape == 2:
				if self.rotation == 1:
					if cordy == 0 or cordx == 4:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy-1][cordx] != 0 or board[cordy][cordx+1] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 2
						board[cordy-1][cordx] = 2 
						board[cordy][cordx+1] = 2
						drop_succeed = True
				elif self.rotation == 2:
					if cordy == 4 or cordx == 4:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy+1][cordx] != 0 or board[cordy][cordx+1] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 2
						board[cordy+1][cordx] = 2 
						board[cordy][cordx+1] = 2
						drop_succeed = True
				elif self.rotation == 3:
					if cordy == 4 or cordx == 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy+1][cordx] != 0 or board[cordy][cordx-1] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 2
						board[cordy+1][cordx] = 2 
						board[cordy][cordx-1] = 2
						drop_succeed = True
				elif self.rotation == 4:
					if cordy == 0 or cordx == 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy-1][cordx] != 0 or board[cordy][cordx-1] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 2
						board[cordy-1][cordx] = 2 
						board[cordy][cordx-1] = 2
						drop_succeed = True
			elif self.shape == 3:
				if self.rotation == 1:
					if cordy == 0 or cordx == 4 or cordx == 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy-1][cordx] != 0 or board[cordy][cordx-1] != 0 or board[cordy][cordx+1] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 3
						board[cordy-1][cordx] = 3 
						board[cordy][cordx-1] = 3
						board[cordy][cordx+1] = 3
						drop_succeed = True
				elif self.rotation == 2:
					if cordy == 0 or cordy == 4 or cordx == 4:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy-1][cordx] != 0 or board[cordy+1][cordx] != 0 or board[cordy][cordx+1] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 3
						board[cordy-1][cordx] = 3 
						board[cordy+1][cordx] = 3
						board[cordy][cordx+1] = 3
						drop_succeed = True
				elif self.rotation == 3:
					if cordy == 4 or cordx == 4 or cordx == 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy+1][cordx] != 0 or board[cordy][cordx-1] != 0 or board[cordy][cordx+1] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 3
						board[cordy+1][cordx] = 3 
						board[cordy][cordx-1] = 3
						board[cordy][cordx+1] = 3
						drop_succeed = True
				elif self.rotation == 4:
					if cordy == 0 or cordy == 4 or cordx == 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy-1][cordx] != 0 or board[cordy+1][cordx] != 0 or board[cordy][cordx-1] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 3
						board[cordy-1][cordx] = 3 
						board[cordy+1][cordx] = 3
						board[cordy][cordx-1] = 3
						drop_succeed = True
			elif self.shape == 4:
				if self.rotation == 1 or self.rotation == 3:
					if cordy == 0 or cordy == 4:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy+1][cordx] != 0 or board[cordy-1][cordx] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 4
						board[cordy-1][cordx] = 4 
						board[cordy+1][cordx] = 4
						drop_succeed = True
				elif self.rotation == 2 or self.rotation == 4:
					if cordx == 0 or cordx == 4:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					elif board[cordy][cordx+1] != 0 or board[cordy][cordx-1] != 0:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
					else: 
						board[cordy][cordx] = 4
						board[cordy][cordx+1] = 4 
						board[cordy][cordx-1] = 4
						drop_succeed = True
			elif self.shape == 5:
				if cordy == 0 or cordy == 4 or cordx == 0 or cordx == 4:
						#print("CAN'T PLACE BLOCK HERE")
						drop_succeed = False
				elif board[cordy+1][cordx] != 0 or board[cordy-1][cordx] != 0 or board[cordy][cordx+1] != 0 or board[cordy][cordx-1] != 0:
					#print("CAN'T PLACE BLOCK HERE")
					drop_succeed = False
				else:
					board[cordy][cordx] = 5
					board[cordy+1][cordx] = 5 
					board[cordy-1][cordx] = 5
					board[cordy][cordx+1] = 5 
					board[cordy][cordx-1] = 5
					drop_succeed = True

''' This is apparently unused 
# Grabs current/new block on start
def get_piece():
	global current_piece
	current_piece = Block_Piece()
	current_piece.get_shape()
'''

''' This is apparently unused 
# Generate the next incoming block
def next_piece():
	global next_piece
	next_piece = Block_Piece()
	next_piece.get_shape()
'''

# Row/Column full check, includes clear
# Scoring implemented here currently
def rc_check(board):
	global score
	for row in board:
		if '0' not in ''.join(map(str,row)):
			board[board.index(row)] = [9,9,9,9,9]
			score += 1
	temp = []
	for col in range(len(board)):
		for row in range(len(board)):
			temp.append(board[row][col])
		if '0' not in ''.join(map(str,temp)):
			for row in range(len(board)):
				board[row][col] = 9
			score += 1
		temp = []
	
	for row in range(len(board)):
		for val in range(len(board)):
			if board[row][val] == 9:
				board[row][val] = 0

# check for game over based on current piece
def game_over_check(board, current_piece):	
	if current_piece.shape == 1:
		# check for rotation 1/3 (vertical)
		for row in range(1, len(board)):
			for val in range(len(board)):
				if board[row][val] == 0 and board[row-1][val] == 0:
					# return game over = false
					return False
		# check for rotation 2/4 (horizontal)
		for row in range(len(board)):
			for val in range(1, len(board)):
				if board[row][val] == 0 and board[row][val-1] == 0:
					# return game over = false       
					return False
		# else return game over = true
		return True
	elif current_piece.shape == 2:
		# rotation 1
		for row in range(1, len(board)):
			for val in range(len(board)-1):
				if board[row][val] == 0 and board[row-1][val] == 0 and board[row][val+1] == 0:
					# return game over = false
					return False
		# rotation 2
		for row in range(len(board)-1):
			for val in range(len(board)-1):
				if board[row][val] == 0 and board[row+1][val] == 0 and board[row][val+1] == 0:
					# return game over = false
					return False
		# rotation 3
		for row in range(len(board)-1):
			for val in range(1, len(board)):
				if board[row][val] == 0 and board[row+1][val] == 0 and board[row][val-1] == 0:
					# return game over = false
					return False
		# rotation 4
		for row in range(1, len(board)):
			for val in range(1, len(board)):
				if board[row][val] == 0 and board[row-1][val] == 0 and board[row][val-1] == 0:
					# return game over = false
					return False
		# else return game over = true
		return True
	elif current_piece.shape == 3:
		# rotation 1
		for row in range(1, len(board)):
			for val in range(1, len(board)-1):
				if board[row][val] == 0 and board[row-1][val] == 0 and board[row][val+1] == 0 and board[row][val-1] == 0:
					# return game over = False
					return False
		# rotation 2
		for row in range(1, len(board)-1):
			for val in range(len(board)-1):
				if board[row][val] == 0 and board[row+1][val] == 0 and board[row-1][val] == 0 and board[row][val+1] == 0:
					# return game over = False
					return False
		# rotation 3
		for row in range(len(board)-1):
			for val in range(1, len(board)-1):
				if board[row][val] == 0 and board[row+1][val] == 0 and board[row][val+1] == 0 and board[row][val-1] == 0:
					# return game over = False
					return False
		# rotation 4
		for row in range(1, len(board)-1):
			for val in range(1, len(board)):
				if board[row][val] == 0 and board[row+1][val] == 0 and board[row-1][val] == 0 and board[row][val-1] == 0:
					# return game over = False
					return False
		# Else return game over = true
		return True
	elif current_piece.shape == 4:
		# check for rotation 1/3 (vertical)
		for row in range(1, len(board)-1):
			for val in range(len(board)):
				if board[row][val] == 0 and board[row-1][val] == 0 and board[row+1][val] == 0:
					# return game over = False					
					return False
		# check for rotation 2/4 (horizontal)
		for row in range(len(board)):
			for val in range(1, len(board)-1):
				if board[row][val] == 0 and board[row][val-1] == 0 and board[row][val+1] == 0:
					# return game over = False
					return False
		# Else return game over = true
		return True
	elif current_piece.shape == 5:
		# check for 5
		for row in range(1, len(board)-1):
			for val in range(1, len(board)-1):
				if board[row][val] == 0 and board[row-1][val] == 0 and board[row+1][val] == 0 and board[row][val-1] == 0 and board[row][val+1] == 0:
					# return game over = False
					return False
		# Else return game over = true
		return True

# Used to draw grid
def draw_board():
	for row in range(5):
		for col in range(5):
			# draw.shape(where, color, [startx, starty, howwide, howtall], linesize)
			if board[row][col] == 0:
				pygame.draw.rect(screen, GRAY, [(MARGIN + WIDTH) * col + MARGIN,down_shift + (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
			elif board[row][col] == 1:
				pygame.draw.rect(screen, RED, [(MARGIN + WIDTH) * col + MARGIN,down_shift + (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
			elif board[row][col] == 2:
				pygame.draw.rect(screen, PURPLE, [(MARGIN + WIDTH) * col + MARGIN,down_shift + (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
			elif board[row][col] == 3:
				pygame.draw.rect(screen, GREEN, [(MARGIN + WIDTH) * col + MARGIN,down_shift + (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
			elif board[row][col] == 4:
				pygame.draw.rect(screen, ORANGE, [(MARGIN + WIDTH) * col + MARGIN,down_shift + (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
			elif board[row][col] == 5:
				pygame.draw.rect(screen, BLUE, [(MARGIN + WIDTH) * col + MARGIN,down_shift + (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

# Used To highlight the "selected" box
def drawHighlightBox():
	global cordx, cordy, current_piece
	if current_piece.shape == 1:
		if current_piece.rotation == 1:
			pygame.draw.rect(screen, LIGHTRED, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTRED, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy)) + (HEIGHT * (cordy-1)), WIDTH, HEIGHT], 4)
		elif current_piece.rotation == 2:
			pygame.draw.rect(screen, LIGHTRED, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTRED, [(MARGIN * (cordx + 2)) + (WIDTH * (cordx+1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
		elif current_piece.rotation == 3:
			pygame.draw.rect(screen, LIGHTRED, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTRED, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy+2)) + (HEIGHT * (cordy+1)), WIDTH, HEIGHT], 4)
		elif current_piece.rotation == 4:
			pygame.draw.rect(screen, LIGHTRED, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTRED, [(MARGIN * (cordx)) + (WIDTH * (cordx-1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
	elif current_piece.shape == 2:
		if current_piece.rotation == 1:
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy)) + (HEIGHT * (cordy-1)), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx + 2)) + (WIDTH * (cordx+1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
		elif current_piece.rotation == 2:			
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy+2)) + (HEIGHT * (cordy+1)), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx + 2)) + (WIDTH * (cordx+1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
		elif current_piece.rotation == 3:
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy+2)) + (HEIGHT * (cordy+1)), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx)) + (WIDTH * (cordx-1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
		elif current_piece.rotation == 4:
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy)) + (HEIGHT * (cordy-1)), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTPURPLE, [(MARGIN * (cordx)) + (WIDTH * (cordx-1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
	elif current_piece.shape == 3:
		if current_piece.rotation == 1:
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy)) + (HEIGHT * (cordy-1)), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 2)) + (WIDTH * (cordx+1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx)) + (WIDTH * (cordx-1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
		elif current_piece.rotation == 2:
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy)) + (HEIGHT * (cordy-1)), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 2)) + (HEIGHT * (cordy+1)), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 2)) + (WIDTH * (cordx+1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
		elif current_piece.rotation == 3:
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 2)) + (HEIGHT * (cordy+1)), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 2)) + (WIDTH * (cordx+1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx)) + (WIDTH * (cordx-1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
		elif current_piece.rotation == 4:
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy)) + (HEIGHT * (cordy-1)), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 2)) + (HEIGHT * (cordy+1)), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTGREEN, [(MARGIN * (cordx)) + (WIDTH * (cordx-1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
	elif current_piece.shape == 4:
		if current_piece.rotation == 1 or current_piece.rotation == 3:
			pygame.draw.rect(screen, LIGHTORANGE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTORANGE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy)) + (HEIGHT * (cordy-1)), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTORANGE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 2)) + (HEIGHT * (cordy+1)), WIDTH, HEIGHT], 4)
		elif current_piece.rotation == 2 or current_piece.rotation == 4:
			pygame.draw.rect(screen, LIGHTORANGE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTORANGE, [(MARGIN * (cordx + 2)) + (WIDTH * (cordx+1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
			pygame.draw.rect(screen, LIGHTORANGE, [(MARGIN * (cordx)) + (WIDTH * (cordx-1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
	elif current_piece.shape == 5:
		# cursor coord
		pygame.draw.rect(screen, LIGHTBLUE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
		# above and below cord
		pygame.draw.rect(screen, LIGHTBLUE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy)) + (HEIGHT * (cordy - 1)), WIDTH, HEIGHT], 4)
		pygame.draw.rect(screen, LIGHTBLUE, [(MARGIN * (cordx + 1)) + (WIDTH * cordx), down_shift + (MARGIN * (cordy + 2)) + (HEIGHT * (cordy + 1)), WIDTH, HEIGHT], 4)
		# right and left of cord
		pygame.draw.rect(screen, LIGHTBLUE, [(MARGIN * (cordx + 2)) + (WIDTH * (cordx + 1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)
		pygame.draw.rect(screen, LIGHTBLUE, [(MARGIN * (cordx)) + (WIDTH * (cordx - 1)), down_shift + (MARGIN * (cordy + 1)) + (HEIGHT * cordy), WIDTH, HEIGHT], 4)

# Draw the next block piece
def drawNextBlock(next_piece):
	if next_piece.shape == 1:
		pygame.draw.rect(screen, RED, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 3) + (HEIGHT * 2), WIDTH, HEIGHT])
		pygame.draw.rect(screen, RED, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 2) + (HEIGHT * 1), WIDTH, HEIGHT])
	elif next_piece.shape == 2:
		pygame.draw.rect(screen, PURPLE, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 3) + (HEIGHT * 2), WIDTH, HEIGHT])
		pygame.draw.rect(screen, PURPLE, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 2) + (HEIGHT * 1), WIDTH, HEIGHT])
		pygame.draw.rect(screen, PURPLE, [(MARGIN * 4) + (WIDTH * 3), 30 + (MARGIN * 3) + (HEIGHT * 2), WIDTH, HEIGHT])
	elif next_piece.shape == 3:
		pygame.draw.rect(screen, GREEN, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 3) + (HEIGHT * 2), WIDTH, HEIGHT])
		pygame.draw.rect(screen, GREEN, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 2) + (HEIGHT * 1), WIDTH, HEIGHT])
		pygame.draw.rect(screen, GREEN, [(MARGIN * 2) + (WIDTH * 1), 30 + (MARGIN * 3) + (HEIGHT * 2), WIDTH, HEIGHT])
		pygame.draw.rect(screen, GREEN, [(MARGIN * 4) + (WIDTH * 3), 30 + (MARGIN * 3) + (HEIGHT * 2), WIDTH, HEIGHT])
	elif next_piece.shape == 4:
		pygame.draw.rect(screen, ORANGE, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 3) + (HEIGHT * 2), WIDTH, HEIGHT])
		pygame.draw.rect(screen, ORANGE, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 2) + (HEIGHT * 1), WIDTH, HEIGHT])
		pygame.draw.rect(screen, ORANGE, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 4) + (HEIGHT * 3), WIDTH, HEIGHT])
	elif next_piece.shape == 5:
		pygame.draw.rect(screen, BLUE, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 3) + (HEIGHT * 2), WIDTH, HEIGHT])
		pygame.draw.rect(screen, BLUE, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 2) + (HEIGHT * 1), WIDTH, HEIGHT])
		pygame.draw.rect(screen, BLUE, [(MARGIN * 3) + (WIDTH * 2), 30 + (MARGIN * 4) + (HEIGHT * 3), WIDTH, HEIGHT])
		pygame.draw.rect(screen, BLUE, [(MARGIN * 2) + (WIDTH * 1), 30 + (MARGIN * 3) + (HEIGHT * 2), WIDTH, HEIGHT])
		pygame.draw.rect(screen, BLUE, [(MARGIN * 4) + (WIDTH * 3), 30 + (MARGIN * 3) + (HEIGHT * 2), WIDTH, HEIGHT])

# draw text - "Score" (current scoring is less ideal)
def draw_scoretext():
	global score
	font = pygame.font.Font(None, 48)
	text = font.render("Score: {}".format(score*100), 1, (255, 255, 255))
	textpos = text.get_rect()
	textpos.centerx = screen.get_rect().centerx
	screen.blit(text, textpos)

# Draw text - "Next Piece" 
def draw_piecetext():
	font = pygame.font.Font(None, 24)
	text = font.render("Next Piece", 1, (255, 255, 255))
	textpos = text.get_rect() 
	textpos.centerx = screen.get_rect().centerx
	screen.blit(text, (100, 60))

# Gets input from user
def get_input():
	global cordx, cordy, current_piece, next_piece, score, drop_succeed
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN: #if (n := cordy-= 1 >= 0) WALRUS OPERATOR \n#cordy = n
			if event.key == K_UP:
				# move cursor up
				if current_piece.shape == 1:
					if current_piece.rotation == 1:
						if cordy - 1 >= 1:
							cordy -= 1
					elif current_piece.rotation == 2 or current_piece.rotation == 3 or current_piece.rotation == 4:
						if cordy - 1 >= 0:      
							cordy -= 1          
				elif current_piece.shape == 2:
					if current_piece.rotation == 1 or current_piece.rotation == 4:
						if cordy - 1 >= 1:
							cordy -= 1
					elif current_piece.rotation == 2 or current_piece.rotation == 3:
						if cordy - 1 >= 0:      
							cordy -= 1    
				elif current_piece.shape == 3:
					if current_piece.rotation == 1 or current_piece.rotation == 2 or current_piece.rotation == 4:
						if cordy - 1 >= 1:
							cordy -= 1
					elif current_piece.rotation == 3:
						if cordy - 1 >= 0:      
							cordy -= 1   
				elif current_piece.shape == 4:
					if current_piece.rotation == 1 or current_piece.rotation == 3:
						if cordy - 1 >= 1:
							cordy -= 1
					elif current_piece.rotation == 2 or current_piece.rotation == 4:
						if cordy - 1 >= 0:      
							cordy -= 1 
				elif current_piece.shape == 5:
					if cordy - 1 >= 1:
						cordy -= 1    
				else:
					if cordy - 1 >= 0:      
						cordy -= 1         
			elif event.key == pygame.K_DOWN:
				# move cursor down
				if current_piece.shape == 1:
					if current_piece.rotation == 3:
						if cordy + 1 <= 3:
							cordy += 1
					elif current_piece.rotation == 1 or current_piece.rotation == 2 or current_piece.rotation == 4:
						if cordy + 1 <= 4:      
							cordy += 1          
				elif current_piece.shape == 2:
					if current_piece.rotation == 2 or current_piece.rotation == 3:
						if cordy + 1 <= 3:
							cordy += 1
					elif current_piece.rotation == 1 or current_piece.rotation == 4:
						if cordy + 1 <= 4:      
							cordy += 1    
				elif current_piece.shape == 3:
					if current_piece.rotation == 2 or current_piece.rotation == 3 or current_piece.rotation == 4:
						if cordy + 1 <= 3:
							cordy += 1
					elif current_piece.rotation == 1:
						if cordy + 1 <= 4:      
							cordy += 1   
				elif current_piece.shape == 4:
					if current_piece.rotation == 1 or current_piece.rotation == 3:
						if cordy + 1 <= 3:
							cordy += 1
					elif current_piece.rotation == 2 or current_piece.rotation == 4:
						if cordy + 1 <= 4:      
							cordy += 1 
				elif current_piece.shape == 5:
					if cordy + 1 <= 3:
						cordy += 1    
				else:
					if cordy + 1 <= 4:
						cordy += 1
			elif event.key == K_RIGHT:
				# move cursor right
				if current_piece.shape == 1:
					if current_piece.rotation == 2:
						if cordx + 1 <= 3:
							cordx += 1
					elif current_piece.rotation == 1 or current_piece.rotation == 3 or current_piece.rotation == 4:
						if cordx + 1 <= 4:      
							cordx += 1          
				elif current_piece.shape == 2:
					if current_piece.rotation == 1 or current_piece.rotation == 2:
						if cordx + 1 <= 3:
							cordx += 1
					elif current_piece.rotation == 3 or current_piece.rotation == 4:
						if cordx + 1 <= 4:      
							cordx += 1    
				elif current_piece.shape == 3:
					if current_piece.rotation == 1 or current_piece.rotation == 2 or current_piece.rotation == 3:
						if cordx + 1 <= 3:
							cordx += 1
					elif current_piece.rotation == 4:
						if cordx + 1 <= 4:      
							cordx += 1   
				elif current_piece.shape == 4:
					if current_piece.rotation == 2 or current_piece.rotation == 4:
						if cordx + 1 <= 3:
							cordx += 1
					elif current_piece.rotation == 1 or current_piece.rotation == 3:
						if cordx + 1 <= 4:      
							cordx += 1 
				elif current_piece.shape == 5:
					if cordx + 1 <= 3:
						cordx += 1    
				else:
					if cordx + 1 <= 4:
						cordx += 1
			elif event.key == K_LEFT:
				# move cursor left
				if current_piece.shape == 1:
					if current_piece.rotation == 4:
						if cordx - 1 >= 1:
							cordx -= 1
					elif current_piece.rotation == 1 or current_piece.rotation == 2 or current_piece.rotation == 3:
						if cordx - 1 >= 0:      
							cordx -= 1          
				elif current_piece.shape == 2:
					if current_piece.rotation == 3 or current_piece.rotation == 4:
						if cordx - 1 >= 1:
							cordx -= 1
					elif current_piece.rotation == 1 or current_piece.rotation == 2:
						if cordx - 1 >= 0:      
							cordx -= 1    
				elif current_piece.shape == 3:
					if current_piece.rotation == 1 or current_piece.rotation == 3 or current_piece.rotation == 4:
						if cordx - 1 >= 1:
							cordx -= 1
					elif current_piece.rotation == 2:
						if cordx - 1 >= 0:      
							cordx -= 1   
				elif current_piece.shape == 4:
					if current_piece.rotation == 2 or current_piece.rotation == 4:
						if cordx - 1 >= 1:
							cordx -= 1
					elif current_piece.rotation == 1 or current_piece.rotation == 3:
						if cordx - 1 >= 0:      
							cordx -= 1 
				elif current_piece.shape == 5:
					if cordx - 1 >= 1:
						cordx -= 1    
				else:
					if cordx - 1 >= 0:
						cordx -= 1
			elif event.key == K_q:
				# rotate block left
				if current_piece.shape == 1:
					if current_piece.rotation == 1:
						if cordx != 0:
							current_piece.rotate_left()
					elif current_piece.rotation == 2:
						if cordy != 0:
							current_piece.rotate_left()
					elif current_piece.rotation == 3:
						if cordx != 4:
							current_piece.rotate_left()
					elif current_piece.rotation == 4:
						if cordy != 4:
							current_piece.rotate_left()
				elif current_piece.shape == 2:
					if current_piece.rotation == 1:
						if cordx != 0:
							current_piece.rotate_left()
					elif current_piece.rotation == 2:
						if cordy != 0:
							current_piece.rotate_left()
					elif current_piece.rotation == 3:
						if cordx != 4:
							current_piece.rotate_left()
					elif current_piece.rotation == 4:
						if cordy != 4:
							current_piece.rotate_left()
				elif current_piece.shape == 3:
					if current_piece.rotation == 1:
						if cordy != 4:
							current_piece.rotate_left()
					elif current_piece.rotation == 2:
						if cordx != 0:
							current_piece.rotate_left()
					elif current_piece.rotation == 3:
						if cordy != 0:
							current_piece.rotate_left()
					elif current_piece.rotation == 4:
						if cordx != 4:
							current_piece.rotate_left()
				elif current_piece.shape == 4:
					if current_piece.rotation == 1 or current_piece.rotation == 3:
						if cordx == 0:
							pass
						elif cordx == 4:
							pass
						else:
							current_piece.rotate_left()
					elif current_piece.rotation == 2 or current_piece.rotation == 4:
						if cordy == 0:
							pass
						elif cordy == 4:
							pass
						else: 
							current_piece.rotate_left()
			elif event.key == K_e:
				# rotate block right
				if current_piece.shape == 1:
					if current_piece.rotation == 1:
						if cordx != 4:
							current_piece.rotate_right()
					elif current_piece.rotation == 2:
						if cordy != 4:
							current_piece.rotate_right()
					elif current_piece.rotation == 3:
						if cordx != 0:
							current_piece.rotate_right()
					elif current_piece.rotation == 4:
						if cordy != 0:
							current_piece.rotate_right()
				elif current_piece.shape == 2:
					if current_piece.rotation == 1:
						if cordy != 4:
							current_piece.rotate_right()
					elif current_piece.rotation == 2:
						if cordx != 0:
							current_piece.rotate_right()
					elif current_piece.rotation == 3:
						if cordy != 0:
							current_piece.rotate_right()
					elif current_piece.rotation == 4:
						if cordx != 4:
							current_piece.rotate_right()
				elif current_piece.shape == 3:
					if current_piece.rotation == 1:
						if cordy != 4:
							current_piece.rotate_right()
					elif current_piece.rotation == 2:
						if cordx != 0:
							current_piece.rotate_right()
					elif current_piece.rotation == 3:
						if cordy != 0:
							current_piece.rotate_right()
					elif current_piece.rotation == 4:
						if cordx != 4:
							current_piece.rotate_right()
				elif current_piece.shape == 4:
					if current_piece.rotation == 1 or current_piece.rotation == 3:
						if cordx == 0:
							pass
						elif cordx == 4:
							pass
						else:
							current_piece.rotate_right()
					elif current_piece.rotation == 2 or current_piece.rotation == 4:
						if cordy == 0:
							pass
						elif cordy == 4:
							pass
						else: 
							current_piece.rotate_right()
			elif event.key == K_SPACE:
				# drop block
				current_piece.drop_block(board, cordx, cordy)
				if drop_succeed == True:
					current_piece = next_piece
					next_piece = Block_Piece()
					next_piece.get_shape()
					drop_succeed = False
					cordx = 2
					cordy = 2
				else:
					# Can't place block here method?
					draw_block_place_error()

# Displays message if block drop is invalid
def draw_block_place_error():
	error_message = "Invalid Move!"
	font = pygame.font.Font('freesansbold.ttf', 32) # font file, size of font
	text = font.render(error_message, True, LIGHTRED, BLACK)
	textRect = text.get_rect() 
	textRect.center = (280 // 2, 420)
	screen.blit(text,textRect)
	pygame.display.update()
	pygame.time.delay(500)

def game_over_screen():
	global game_over
	again_font = pygame.font.Font('freesansbold.ttf', 25)
	over_font=  pygame.font.Font('freesansbold.ttf', 32)

	game_over_message = "Game Over"
	play_again_message = "Click to Play Again"

	game_over_text = over_font.render(game_over_message, True, LIGHTRED, BLACK)
	play_again_text = again_font.render(play_again_message, True, LIGHTRED, BLACK)

	game_over_textRect = game_over_text.get_rect()
	play_again_textRect = play_again_text.get_rect()

	game_over_textRect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 100)
	play_again_textRect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

	screen.blit(play_again_text, play_again_textRect)
	screen.blit(game_over_text, game_over_textRect)

	pygame.display.update()

def play_again():
	global game_over, new_game
	mouse_x, mouse_y = pygame.mouse.get_pos()
	
	again_font = pygame.font.Font('freesansbold.ttf', 25)
	play_again_message = "Click to Play Again"
	play_again_text = again_font.render(play_again_message, True, LIGHTRED, BLACK)
	play_again_textRect = play_again_text.get_rect()
	play_again_textRect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
	button_clicked = play_again_textRect.collidepoint(mouse_x, mouse_y)
	
	if button_clicked and (pygame.mouse.get_pressed()[0] == 1):
		game_over = False
		new_game = True
		print("Starting over")

# -------- Main Program Loop -----------
while True:
	if new_game:
		board = [[0,0,0,0,0] for i in range(5)]
		current_piece = Block_Piece()
		current_piece.get_shape()
		next_piece = Block_Piece()
		next_piece.get_shape()
		score = 0
		new_game = False

	# Limit to 60 frames per second
	clock.tick(60)

	# Set the screen background`
	screen.fill(BLACK)
 
	# Draw the grid, hightlighted/cursor, and next up piece
	draw_board()
	drawHighlightBox() 
	drawNextBlock(next_piece)
	draw_scoretext()
	draw_piecetext()

	# check for game over
	game_over = game_over_check(board, current_piece)
	#game_over = True
	if game_over:
		game_over_screen()
		play_again()
	# Loop for Game over status
	# This currently just clears the board
	# Needs to pause, then reset on approval
	# needs to reset score
	'''
	if game_over:
		# print game over message & ask if they wanna play again
		#again = input("Play again?: ")
		again = 'yes'

		text = font.render(error_message, True, RED, BLACK)
		button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
		if button_clicked: 
			new_game = True
		if again[0] == 'y':
			game_over = False
			new_game = True
	'''

	# Get input
	get_input() 

	#check for r/c clear
	rc_check(board)
	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip() # or.update?