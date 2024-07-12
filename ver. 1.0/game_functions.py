import pygame, sys
from pygame import *
from block_pieces import Block_Piece
import draw_functions

# Row/Column full check, clear, and score
def rc_check(game_settings):
	# Check for row complete (Subs in 9)
	for row in game_settings.board:
		if '0' not in ''.join(map(str,row)):
			game_settings.board[game_settings.board.index(row)] = [9,9,9,9,9]
			# Add to score # TODO: Improve Scoring
			game_settings.score += 1
	temp = []
	# Check for column complete (Subs in 9)
	for col in range(len(game_settings.board)):
		for row in range(len(game_settings.board)):
			temp.append(game_settings.board[row][col])
		if '0' not in ''.join(map(str,temp)):
			for row in range(len(game_settings.board)):
				game_settings.board[row][col] = 9
			# Add to score # TODO: Improve Scoring
			game_settings.score += 1
		temp = []
	# Clears out 9s that were subbed in
	for row in range(len(game_settings.board)):
		for val in range(len(game_settings.board)):
			if game_settings.board[row][val] == 9:
				game_settings.board[row][val] = 0

# Check for game over based on current piece
def game_over_check(game_settings):
	if game_settings.current_piece.shape == 1:
		# Check for rotations 1+3 (vertical)
		for row in range(1, len(game_settings.board)):
			for val in range(len(game_settings.board)):
				if game_settings.board[row][val] == 0 and game_settings.board[row-1][val] == 0:
					return False
		# Check for rotations 2+4 (horizontal)
		for row in range(len(game_settings.board)):
			for val in range(1, len(game_settings.board)):
				if game_settings.board[row][val] == 0 and game_settings.board[row][val-1] == 0:       
					return False
		return True
	elif game_settings.current_piece.shape == 2:
		# Rotation 1
		for row in range(1, len(game_settings.board)):
			for val in range(len(game_settings.board)-1):
				if game_settings.board[row][val] == 0 and game_settings.board[row-1][val] == 0 and game_settings.board[row][val+1] == 0:
					return False
		# Rotation 2
		for row in range(len(game_settings.board)-1):
			for val in range(len(game_settings.board)-1):
				if game_settings.board[row][val] == 0 and game_settings.board[row+1][val] == 0 and game_settings.board[row][val+1] == 0:
					return False
		# Rotation 3
		for row in range(len(game_settings.board)-1):
			for val in range(1, len(game_settings.board)):
				if game_settings.board[row][val] == 0 and game_settings.board[row+1][val] == 0 and game_settings.board[row][val-1] == 0:
					return False
		# Rotation 4
		for row in range(1, len(game_settings.board)):
			for val in range(1, len(game_settings.board)):
				if game_settings.board[row][val] == 0 and game_settings.board[row-1][val] == 0 and game_settings.board[row][val-1] == 0:
					return False
		return True
	elif game_settings.current_piece.shape == 3:
		# Rotation 1
		for row in range(1, len(game_settings.board)):
			for val in range(1, len(game_settings.board)-1):
				if game_settings.board[row][val] == 0 and game_settings.board[row-1][val] == 0 and game_settings.board[row][val+1] == 0 and game_settings.board[row][val-1] == 0:
					return False
		# Rotation 2
		for row in range(1, len(game_settings.board)-1):
			for val in range(len(game_settings.board)-1):
				if game_settings.board[row][val] == 0 and game_settings.board[row+1][val] == 0 and game_settings.board[row-1][val] == 0 and game_settings.board[row][val+1] == 0:
					return False
		# Rotation 3
		for row in range(len(game_settings.board)-1):
			for val in range(1, len(game_settings.board)-1):
				if game_settings.board[row][val] == 0 and game_settings.board[row+1][val] == 0 and game_settings.board[row][val+1] == 0 and game_settings.board[row][val-1] == 0:
					return False
		# Rotation 4
		for row in range(1, len(game_settings.board)-1):
			for val in range(1, len(game_settings.board)):
				if game_settings.board[row][val] == 0 and game_settings.board[row+1][val] == 0 and game_settings.board[row-1][val] == 0 and game_settings.board[row][val-1] == 0:
					return False
		return True
	elif game_settings.current_piece.shape == 4:
		# Check for rotations 1+3 (vertical)
		for row in range(1, len(game_settings.board)-1):
			for val in range(len(game_settings.board)):
				if game_settings.board[row][val] == 0 and game_settings.board[row-1][val] == 0 and game_settings.board[row+1][val] == 0:					
					return False
		# Check for rotations 2+4 (horizontal)
		for row in range(len(game_settings.board)):
			for val in range(1, len(game_settings.board)-1):
				if game_settings.board[row][val] == 0 and game_settings.board[row][val-1] == 0 and game_settings.board[row][val+1] == 0:
					return False
		return True
	elif game_settings.current_piece.shape == 5:
		# Check for 5
		for row in range(1, len(game_settings.board)-1):
			for val in range(1, len(game_settings.board)-1):
				if game_settings.board[row][val] == 0 and game_settings.board[row-1][val] == 0 and game_settings.board[row+1][val] == 0 and game_settings.board[row][val-1] == 0 and game_settings.board[row][val+1] == 0:
					return False
		return True

# Gets input from user (Arrow Keys, Q/E, and Space)
def get_input(game_settings, screen):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		# TODO: Add ALT+F4 Key combination for close game
		elif event.type == pygame.KEYDOWN:
			# Move cursor up
			if event.key == K_UP:
				if game_settings.current_piece.shape == 1:
					if game_settings.current_piece.rotation == 1:
						if game_settings.cordy - 1 >= 1:
							game_settings.cordy -= 1
					elif game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 3 or game_settings.current_piece.rotation == 4:
						if game_settings.cordy - 1 >= 0:      
							game_settings.cordy -= 1          
				elif game_settings.current_piece.shape == 2:
					if game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 4:
						if game_settings.cordy - 1 >= 1:
							game_settings.cordy -= 1
					elif game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 3:
						if game_settings.cordy - 1 >= 0:      
							game_settings.cordy -= 1    
				elif game_settings.current_piece.shape == 3:
					if game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 4:
						if game_settings.cordy - 1 >= 1:
							game_settings.cordy -= 1
					elif game_settings.current_piece.rotation == 3:
						if game_settings.cordy - 1 >= 0:      
							game_settings.cordy -= 1   
				elif game_settings.current_piece.shape == 4:
					if game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 3:
						if game_settings.cordy - 1 >= 1:
							game_settings.cordy -= 1
					elif game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 4:
						if game_settings.cordy - 1 >= 0:      
							game_settings.cordy -= 1 
				elif game_settings.current_piece.shape == 5:
					if game_settings.cordy - 1 >= 1:
						game_settings.cordy -= 1    
				else:
					if game_settings.cordy - 1 >= 0:      
						game_settings.cordy -= 1         
			# Move cursor down
			elif event.key == pygame.K_DOWN:
				if game_settings.current_piece.shape == 1:
					if game_settings.current_piece.rotation == 3:
						if game_settings.cordy + 1 <= 3:
							game_settings.cordy += 1
					elif game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 4:
						if game_settings.cordy + 1 <= 4:      
							game_settings.cordy += 1          
				elif game_settings.current_piece.shape == 2:
					if game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 3:
						if game_settings.cordy + 1 <= 3:
							game_settings.cordy += 1
					elif game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 4:
						if game_settings.cordy + 1 <= 4:      
							game_settings.cordy += 1    
				elif game_settings.current_piece.shape == 3:
					if game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 3 or game_settings.current_piece.rotation == 4:
						if game_settings.cordy + 1 <= 3:
							game_settings.cordy += 1
					elif game_settings.current_piece.rotation == 1:
						if game_settings.cordy + 1 <= 4:      
							game_settings.cordy += 1   
				elif game_settings.current_piece.shape == 4:
					if game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 3:
						if game_settings.cordy + 1 <= 3:
							game_settings.cordy += 1
					elif game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 4:
						if game_settings.cordy + 1 <= 4:      
							game_settings.cordy += 1 
				elif game_settings.current_piece.shape == 5:
					if game_settings.cordy + 1 <= 3:
						game_settings.cordy += 1    
				else:
					if game_settings.cordy + 1 <= 4:
						game_settings.cordy += 1
			# Move cursor right
			elif event.key == K_RIGHT:
				if game_settings.current_piece.shape == 1:
					if game_settings.current_piece.rotation == 2:
						if game_settings.cordx + 1 <= 3:
							game_settings.cordx += 1
					elif game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 3 or game_settings.current_piece.rotation == 4:
						if game_settings.cordx + 1 <= 4:      
							game_settings.cordx += 1          
				elif game_settings.current_piece.shape == 2:
					if game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 2:
						if game_settings.cordx + 1 <= 3:
							game_settings.cordx += 1
					elif game_settings.current_piece.rotation == 3 or game_settings.current_piece.rotation == 4:
						if game_settings.cordx + 1 <= 4:      
							game_settings.cordx += 1    
				elif game_settings.current_piece.shape == 3:
					if game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 3:
						if game_settings.cordx + 1 <= 3:
							game_settings.cordx += 1
					elif game_settings.current_piece.rotation == 4:
						if game_settings.cordx + 1 <= 4:      
							game_settings.cordx += 1   
				elif game_settings.current_piece.shape == 4:
					if game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 4:
						if game_settings.cordx + 1 <= 3:
							game_settings.cordx += 1
					elif game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 3:
						if game_settings.cordx + 1 <= 4:      
							game_settings.cordx += 1 
				elif game_settings.current_piece.shape == 5:
					if game_settings.cordx + 1 <= 3:
						game_settings.cordx += 1    
				else:
					if game_settings.cordx + 1 <= 4:
						game_settings.cordx += 1
			# Move cursor left
			elif event.key == K_LEFT:
				if game_settings.current_piece.shape == 1:
					if game_settings.current_piece.rotation == 4:
						if game_settings.cordx - 1 >= 1:
							game_settings.cordx -= 1
					elif game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 3:
						if game_settings.cordx - 1 >= 0:      
							game_settings.cordx -= 1          
				elif game_settings.current_piece.shape == 2:
					if game_settings.current_piece.rotation == 3 or game_settings.current_piece.rotation == 4:
						if game_settings.cordx - 1 >= 1:
							game_settings.cordx -= 1
					elif game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 2:
						if game_settings.cordx - 1 >= 0:      
							game_settings.cordx -= 1    
				elif game_settings.current_piece.shape == 3:
					if game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 3 or game_settings.current_piece.rotation == 4:
						if game_settings.cordx - 1 >= 1:
							game_settings.cordx -= 1
					elif game_settings.current_piece.rotation == 2:
						if game_settings.cordx - 1 >= 0:      
							game_settings.cordx -= 1   
				elif game_settings.current_piece.shape == 4:
					if game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 4:
						if game_settings.cordx - 1 >= 1:
							game_settings.cordx -= 1
					elif game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 3:
						if game_settings.cordx - 1 >= 0:      
							game_settings.cordx -= 1 
				elif game_settings.current_piece.shape == 5:
					if game_settings.cordx - 1 >= 1:
						game_settings.cordx -= 1    
				else:
					if game_settings.cordx - 1 >= 0:
						game_settings.cordx -= 1
			# Rotate block left
			elif event.key == K_q:
				if game_settings.current_piece.shape == 1:
					if game_settings.current_piece.rotation == 1:
						if game_settings.cordx != 0:
							game_settings.current_piece.rotate_left()
					elif game_settings.current_piece.rotation == 2:
						if game_settings.cordy != 0:
							game_settings.current_piece.rotate_left()
					elif game_settings.current_piece.rotation == 3:
						if game_settings.cordx != 4:
							game_settings.current_piece.rotate_left()
					elif game_settings.current_piece.rotation == 4:
						if game_settings.cordy != 4:
							game_settings.current_piece.rotate_left()
				elif game_settings.current_piece.shape == 2:
					if game_settings.current_piece.rotation == 1:
						if game_settings.cordx != 0:
							game_settings.current_piece.rotate_left()
					elif game_settings.current_piece.rotation == 2:
						if game_settings.cordy != 0:
							game_settings.current_piece.rotate_left()
					elif game_settings.current_piece.rotation == 3:
						if game_settings.cordx != 4:
							game_settings.current_piece.rotate_left()
					elif game_settings.current_piece.rotation == 4:
						if game_settings.cordy != 4:
							game_settings.current_piece.rotate_left()
				elif game_settings.current_piece.shape == 3:
					if game_settings.current_piece.rotation == 1:
						if game_settings.cordy != 4:
							game_settings.current_piece.rotate_left()
					elif game_settings.current_piece.rotation == 2:
						if game_settings.cordx != 0:
							game_settings.current_piece.rotate_left()
					elif game_settings.current_piece.rotation == 3:
						if game_settings.cordy != 0:
							game_settings.current_piece.rotate_left()
					elif game_settings.current_piece.rotation == 4:
						if game_settings.cordx != 4:
							game_settings.current_piece.rotate_left()
				elif game_settings.current_piece.shape == 4:
					if game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 3:
						if game_settings.cordx == 0:
							pass
						elif game_settings.cordx == 4:
							pass
						else:
							game_settings.current_piece.rotate_left()
					elif game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 4:
						if game_settings.cordy == 0:
							pass
						elif game_settings.cordy == 4:
							pass
						else: 
							game_settings.current_piece.rotate_left()
			# Rotate block right
			elif event.key == K_e:
				if game_settings.current_piece.shape == 1:
					if game_settings.current_piece.rotation == 1:
						if game_settings.cordx != 4:
							game_settings.current_piece.rotate_right()
					elif game_settings.current_piece.rotation == 2:
						if game_settings.cordy != 4:
							game_settings.current_piece.rotate_right()
					elif game_settings.current_piece.rotation == 3:
						if game_settings.cordx != 0:
							game_settings.current_piece.rotate_right()
					elif game_settings.current_piece.rotation == 4:
						if game_settings.cordy != 0:
							game_settings.current_piece.rotate_right()
				elif game_settings.current_piece.shape == 2:
					if game_settings.current_piece.rotation == 1:
						if game_settings.cordy != 4:
							game_settings.current_piece.rotate_right()
					elif game_settings.current_piece.rotation == 2:
						if game_settings.cordx != 0:
							game_settings.current_piece.rotate_right()
					elif game_settings.current_piece.rotation == 3:
						if game_settings.cordy != 0:
							game_settings.current_piece.rotate_right()
					elif game_settings.current_piece.rotation == 4:
						if game_settings.cordx != 4:
							game_settings.current_piece.rotate_right()
				elif game_settings.current_piece.shape == 3:
					if game_settings.current_piece.rotation == 1:
						if game_settings.cordy != 4:
							game_settings.current_piece.rotate_right()
					elif game_settings.current_piece.rotation == 2:
						if game_settings.cordx != 0:
							game_settings.current_piece.rotate_right()
					elif game_settings.current_piece.rotation == 3:
						if game_settings.cordy != 0:
							game_settings.current_piece.rotate_right()
					elif game_settings.current_piece.rotation == 4:
						if game_settings.cordx != 4:
							game_settings.current_piece.rotate_right()
				elif game_settings.current_piece.shape == 4:
					if game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 3:
						if game_settings.cordx == 0:
							pass
						elif game_settings.cordx == 4:
							pass
						else:
							game_settings.current_piece.rotate_right()
					elif game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 4:
						if game_settings.cordy == 0:
							pass
						elif game_settings.cordy == 4:
							pass
						else: 
							game_settings.current_piece.rotate_right()
			# Drop block on Board
			elif event.key == K_SPACE:
				game_settings.current_piece.drop_block(game_settings)
				# Acquire next piece, getting new piece, reset cursor
				if game_settings.drop_succeed == True:
					game_settings.current_piece = game_settings.next_piece
					game_settings.next_piece = Block_Piece(game_settings)
					game_settings.next_piece.get_shape(game_settings)
					game_settings.drop_succeed = False
					game_settings.cordx = 2
					game_settings.cordy = 2
				# Display error message; block doesn't fit
				else:
					draw_functions.draw_block_place_error(game_settings, screen)

# Check is "Play Again" is clicked on screen
def check_play_again(game_settings):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	again_font = pygame.font.Font('freesansbold.ttf', 25)
	play_again_message = "Click to Play Again"
	play_again_text = again_font.render(play_again_message, True, game_settings.LIGHTRED, game_settings.BLACK)
	play_again_textRect = play_again_text.get_rect()
	play_again_textRect.center = (game_settings.WINDOW_SIZE[0] // 2, game_settings.WINDOW_SIZE[1] // 2)
	button_clicked = play_again_textRect.collidepoint(mouse_x, mouse_y)
	# If hovering button and button clicked reset. New_game=true, 
	if button_clicked and (pygame.mouse.get_pressed()[0] == 1):
		game_settings.game_over = False
		game_settings.new_game = True
		