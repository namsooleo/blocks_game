import pygame
from pygame import *

# Used to draw grid
def draw_board(game_settings, screen):
	for row in range(5):
		for col in range(5):
			# draw.shape(where, color, [startx, starty, howwide, howtall], linesize)
			if game_settings.board[row][col] == 0:
				pygame.draw.rect(screen, game_settings.GRAY, [(game_settings.MARGIN + game_settings.WIDTH) * col + game_settings.MARGIN, game_settings.down_shift + (game_settings.MARGIN + game_settings.HEIGHT) * row + game_settings.MARGIN, game_settings.WIDTH, game_settings.HEIGHT])
			elif game_settings.board[row][col] == 1:
				pygame.draw.rect(screen, game_settings.RED, [(game_settings.MARGIN + game_settings.WIDTH) * col + game_settings.MARGIN, game_settings.down_shift + (game_settings.MARGIN + game_settings.HEIGHT) * row + game_settings.MARGIN, game_settings.WIDTH, game_settings.HEIGHT])
			elif game_settings.board[row][col] == 2:
				pygame.draw.rect(screen, game_settings.PURPLE, [(game_settings.MARGIN + game_settings.WIDTH) * col + game_settings.MARGIN, game_settings.down_shift + (game_settings.MARGIN + game_settings.HEIGHT) * row + game_settings.MARGIN, game_settings.WIDTH, game_settings.HEIGHT])
			elif game_settings.board[row][col] == 3:
				pygame.draw.rect(screen, game_settings.GREEN, [(game_settings.MARGIN + game_settings.WIDTH) * col + game_settings.MARGIN, game_settings.down_shift + (game_settings.MARGIN + game_settings.HEIGHT) * row + game_settings.MARGIN, game_settings.WIDTH, game_settings.HEIGHT])
			elif game_settings.board[row][col] == 4:
				pygame.draw.rect(screen, game_settings.ORANGE, [(game_settings.MARGIN + game_settings.WIDTH) * col + game_settings.MARGIN, game_settings.down_shift + (game_settings.MARGIN + game_settings.HEIGHT) * row + game_settings.MARGIN, game_settings.WIDTH, game_settings.HEIGHT])
			elif game_settings.board[row][col] == 5:
				pygame.draw.rect(screen, game_settings.BLUE, [(game_settings.MARGIN + game_settings.WIDTH) * col + game_settings.MARGIN, game_settings.down_shift + (game_settings.MARGIN + game_settings.HEIGHT) * row + game_settings.MARGIN, game_settings.WIDTH, game_settings.HEIGHT])

# Used To highlight the "hovered" boxes
def drawHighlightBox(game_settings, screen):
	if game_settings.current_piece.shape == 1:
		if game_settings.current_piece.rotation == 1:
			pygame.draw.rect(screen, game_settings.LIGHTRED, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTRED, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy)) + (game_settings.HEIGHT * (game_settings.cordy-1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
		elif game_settings.current_piece.rotation == 2:
			pygame.draw.rect(screen, game_settings.LIGHTRED, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTRED, [(game_settings.MARGIN * (game_settings.cordx + 2)) + (game_settings.WIDTH * (game_settings.cordx+1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
		elif game_settings.current_piece.rotation == 3:
			pygame.draw.rect(screen, game_settings.LIGHTRED, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTRED, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy+2)) + (game_settings.HEIGHT * (game_settings.cordy+1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
		elif game_settings.current_piece.rotation == 4:
			pygame.draw.rect(screen, game_settings.LIGHTRED, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTRED, [(game_settings.MARGIN * (game_settings.cordx)) + (game_settings.WIDTH * (game_settings.cordx-1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
	elif game_settings.current_piece.shape == 2:
		if game_settings.current_piece.rotation == 1:
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy)) + (game_settings.HEIGHT * (game_settings.cordy-1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx + 2)) + (game_settings.WIDTH * (game_settings.cordx+1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
		elif game_settings.current_piece.rotation == 2:			
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy+2)) + (game_settings.HEIGHT * (game_settings.cordy+1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx + 2)) + (game_settings.WIDTH * (game_settings.cordx+1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
		elif game_settings.current_piece.rotation == 3:
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy+2)) + (game_settings.HEIGHT * (game_settings.cordy+1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx)) + (game_settings.WIDTH * (game_settings.cordx-1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
		elif game_settings.current_piece.rotation == 4:
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy)) + (game_settings.HEIGHT * (game_settings.cordy-1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTPURPLE, [(game_settings.MARGIN * (game_settings.cordx)) + (game_settings.WIDTH * (game_settings.cordx-1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
	elif game_settings.current_piece.shape == 3:
		if game_settings.current_piece.rotation == 1:
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy)) + (game_settings.HEIGHT * (game_settings.cordy-1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 2)) + (game_settings.WIDTH * (game_settings.cordx+1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx)) + (game_settings.WIDTH * (game_settings.cordx-1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
		elif game_settings.current_piece.rotation == 2:
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy)) + (game_settings.HEIGHT * (game_settings.cordy-1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 2)) + (game_settings.HEIGHT * (game_settings.cordy+1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 2)) + (game_settings.WIDTH * (game_settings.cordx+1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
		elif game_settings.current_piece.rotation == 3:
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 2)) + (game_settings.HEIGHT * (game_settings.cordy+1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 2)) + (game_settings.WIDTH * (game_settings.cordx+1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx)) + (game_settings.WIDTH * (game_settings.cordx-1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
		elif game_settings.current_piece.rotation == 4:
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy)) + (game_settings.HEIGHT * (game_settings.cordy-1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 2)) + (game_settings.HEIGHT * (game_settings.cordy+1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTGREEN, [(game_settings.MARGIN * (game_settings.cordx)) + (game_settings.WIDTH * (game_settings.cordx-1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
	elif game_settings.current_piece.shape == 4:
		if game_settings.current_piece.rotation == 1 or game_settings.current_piece.rotation == 3:
			pygame.draw.rect(screen, game_settings.LIGHTORANGE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTORANGE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy)) + (game_settings.HEIGHT * (game_settings.cordy-1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTORANGE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 2)) + (game_settings.HEIGHT * (game_settings.cordy+1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
		elif game_settings.current_piece.rotation == 2 or game_settings.current_piece.rotation == 4:
			pygame.draw.rect(screen, game_settings.LIGHTORANGE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTORANGE, [(game_settings.MARGIN * (game_settings.cordx + 2)) + (game_settings.WIDTH * (game_settings.cordx+1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
			pygame.draw.rect(screen, game_settings.LIGHTORANGE, [(game_settings.MARGIN * (game_settings.cordx)) + (game_settings.WIDTH * (game_settings.cordx-1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
	elif game_settings.current_piece.shape == 5:
		# cursor coord
		pygame.draw.rect(screen, game_settings.LIGHTBLUE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
		# above and below cord
		pygame.draw.rect(screen, game_settings.LIGHTBLUE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy)) + (game_settings.HEIGHT * (game_settings.cordy - 1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
		pygame.draw.rect(screen, game_settings.LIGHTBLUE, [(game_settings.MARGIN * (game_settings.cordx + 1)) + (game_settings.WIDTH * game_settings.cordx), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 2)) + (game_settings.HEIGHT * (game_settings.cordy + 1)), game_settings.WIDTH, game_settings.HEIGHT], 4)
		# right and left of cord
		pygame.draw.rect(screen, game_settings.LIGHTBLUE, [(game_settings.MARGIN * (game_settings.cordx + 2)) + (game_settings.WIDTH * (game_settings.cordx + 1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)
		pygame.draw.rect(screen, game_settings.LIGHTBLUE, [(game_settings.MARGIN * (game_settings.cordx)) + (game_settings.WIDTH * (game_settings.cordx - 1)), game_settings.down_shift + (game_settings.MARGIN * (game_settings.cordy + 1)) + (game_settings.HEIGHT * game_settings.cordy), game_settings.WIDTH, game_settings.HEIGHT], 4)

# Draw the next block piece
def drawNextBlock(game_settings, screen):
	if game_settings.next_piece.shape == 1:
		pygame.draw.rect(screen, game_settings.RED, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 3) + (game_settings.HEIGHT * 2), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.RED, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 2) + (game_settings.HEIGHT * 1), game_settings.WIDTH, game_settings.HEIGHT])
	elif game_settings.next_piece.shape == 2:
		pygame.draw.rect(screen, game_settings.PURPLE, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 3) + (game_settings.HEIGHT * 2), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.PURPLE, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 2) + (game_settings.HEIGHT * 1), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.PURPLE, [(game_settings.MARGIN * 4) + (game_settings.WIDTH * 3), 30 + (game_settings.MARGIN * 3) + (game_settings.HEIGHT * 2), game_settings.WIDTH, game_settings.HEIGHT])
	elif game_settings.next_piece.shape == 3:
		pygame.draw.rect(screen, game_settings.GREEN, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 3) + (game_settings.HEIGHT * 2), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.GREEN, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 2) + (game_settings.HEIGHT * 1), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.GREEN, [(game_settings.MARGIN * 2) + (game_settings.WIDTH * 1), 30 + (game_settings.MARGIN * 3) + (game_settings.HEIGHT * 2), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.GREEN, [(game_settings.MARGIN * 4) + (game_settings.WIDTH * 3), 30 + (game_settings.MARGIN * 3) + (game_settings.HEIGHT * 2), game_settings.WIDTH, game_settings.HEIGHT])
	elif game_settings.next_piece.shape == 4:
		pygame.draw.rect(screen, game_settings.ORANGE, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 3) + (game_settings.HEIGHT * 2), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.ORANGE, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 2) + (game_settings.HEIGHT * 1), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.ORANGE, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 4) + (game_settings.HEIGHT * 3), game_settings.WIDTH, game_settings.HEIGHT])
	elif game_settings.next_piece.shape == 5:
		pygame.draw.rect(screen, game_settings.BLUE, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 3) + (game_settings.HEIGHT * 2), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.BLUE, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 2) + (game_settings.HEIGHT * 1), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.BLUE, [(game_settings.MARGIN * 3) + (game_settings.WIDTH * 2), 30 + (game_settings.MARGIN * 4) + (game_settings.HEIGHT * 3), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.BLUE, [(game_settings.MARGIN * 2) + (game_settings.WIDTH * 1), 30 + (game_settings.MARGIN * 3) + (game_settings.HEIGHT * 2), game_settings.WIDTH, game_settings.HEIGHT])
		pygame.draw.rect(screen, game_settings.BLUE, [(game_settings.MARGIN * 4) + (game_settings.WIDTH * 3), 30 + (game_settings.MARGIN * 3) + (game_settings.HEIGHT * 2), game_settings.WIDTH, game_settings.HEIGHT])

# Draw text - "Score" (current scoring is less ideal)
def draw_scoretext(game_settings, screen):
	# TODO: Improve Scoring
	font = pygame.font.Font(None, 48)
	text = font.render("Score: {}".format(game_settings.score*100), 1, (255, 255, 255)) # Should I replace this with game_settings.WHITE?
	textpos = text.get_rect()
	textpos.centerx = screen.get_rect().centerx
	screen.blit(text, textpos)

# Draw text - "Next Piece" 
def draw_piecetext(screen):
	font = pygame.font.Font(None, 24)
	text = font.render("Next Piece", 1, (255, 255, 255)) # Should I replace this with game_settings.WHITE?
	textpos = text.get_rect() 
	textpos.centerx = screen.get_rect().centerx
	screen.blit(text, (100, 60))

# Displays message if block drop is invalid
def draw_block_place_error(game_settings, screen):
	error_message = "Invalid Move!"
	font = pygame.font.Font('freesansbold.ttf', 32) # font file, size of font
	text = font.render(error_message, True, game_settings.LIGHTRED, game_settings.BLACK)
	textRect = text.get_rect() 
	textRect.center = (280 // 2, 420)
	screen.blit(text,textRect)
	pygame.display.update()
	pygame.time.delay(300)

# Displays Game Over and Play again message on loss
def draw_game_over_screen(game_settings, screen):
	again_font = pygame.font.Font('freesansbold.ttf', 25)
	over_font=  pygame.font.Font('freesansbold.ttf', 32)
	game_over_message = "Game Over"
	play_again_message = "Click to Play Again"
	game_over_text = over_font.render(game_over_message, True, game_settings.LIGHTRED, game_settings.BLACK)
	play_again_text = again_font.render(play_again_message, True, game_settings.LIGHTRED, game_settings.BLACK)
	game_over_textRect = game_over_text.get_rect()
	play_again_textRect = play_again_text.get_rect()
	game_over_textRect.center = (game_settings.WINDOW_SIZE[0] // 2, game_settings.WINDOW_SIZE[1] // 2 + 100)
	play_again_textRect.center = (game_settings.WINDOW_SIZE[0] // 2, game_settings.WINDOW_SIZE[1] // 2)
	screen.blit(play_again_text, play_again_textRect)
	screen.blit(game_over_text, game_over_textRect)
	pygame.display.update()

# Combine draw functions displaying game state
def draw_game_state(game_settings, screen):
    draw_board(game_settings, screen)
    drawHighlightBox(game_settings, screen) 
    drawNextBlock(game_settings, screen)
    draw_scoretext(game_settings, screen)
    draw_piecetext(screen)