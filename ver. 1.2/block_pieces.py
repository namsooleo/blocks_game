import pygame, random
from pygame import *

class Block_Piece:
	# Define block attributes. 
	def __init__(self, game_settings):
		self.shape = 0 # What block shape it is (1-5)
		self.rotation = 1 # What orientation/rotation state 
		self.color = (255, 255, 255) # Color of the block
		self.game_settings = game_settings # imports block settings from class 

	# Randomly select a block piece shape
	def get_shape(self, game_settings):
		self.shape = random.randint(1, self.game_settings.number_blocks) #  See readme for shape/rotations
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

	# Change rotation attribute. Spin Left 
	def rotate_left(self):
		if self.rotation  == 1:
			self.rotation = 4
		else:
			self.rotation -= 1

	# Change rotation attribute. Spin Right
	def rotate_right(self):
		if self.rotation  == 4:
			self.rotation = 1
		else:
			self.rotation += 1

	# Attempt to add the block to the board. 
	def drop_block(self, game_settings):
		# If the cursor is currently over a occupied space fail
		if self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] != 0:
			self.game_settings.drop_succeed = False
		else:
			# Depending on block shape (1-5) follow the same basic 3 steps. 
			if self.shape == 1:
				# checks depend on current_piece shape's rotation
				if self.rotation == 1:
					# if cursor is at top of board, this shape/rotation combination will fail. 
					if self.game_settings.cordy == 0:
						self.game_settings.drop_succeed = False
					# if the space above cursor is ocupied, this will fail. (See block/rotation comment above for shape)
					elif self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] != 0:
						self.game_settings.drop_succeed = False     
					# Otherwise add this shape to board. (See block/rotation comment above for shape)
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 1
						self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] = 1
						self.game_settings.drop_succeed = True
				elif self.rotation == 2:
					if self.game_settings.cordx == 4:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 1
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] = 1
						self.game_settings.drop_succeed = True
				elif self.rotation == 3:
					if self.game_settings.cordy == 4:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 1
						self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] = 1
						self.game_settings.drop_succeed = True
				elif self.rotation == 4:
					if self.game_settings.cordx == 0:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 1
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] = 1
						self.game_settings.drop_succeed = True
			elif self.shape == 2:
				if self.rotation == 1:
					if self.game_settings.cordy == 0 or self.game_settings.cordx == 4:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 2
						self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] = 2 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] = 2
						self.game_settings.drop_succeed = True
				elif self.rotation == 2:
					if self.game_settings.cordy == 4 or self.game_settings.cordx == 4:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 2
						self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] = 2 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] = 2
						self.game_settings.drop_succeed = True
				elif self.rotation == 3:
					if self.game_settings.cordy == 4 or self.game_settings.cordx == 0:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 2
						self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] = 2 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] = 2
						self.game_settings.drop_succeed = True
				elif self.rotation == 4:
					if self.game_settings.cordy == 0 or self.game_settings.cordx == 0:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 2
						self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] = 2 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] = 2
						self.game_settings.drop_succeed = True
			elif self.shape == 3:
				if self.rotation == 1:
					if self.game_settings.cordy == 0 or self.game_settings.cordx == 4 or self.game_settings.cordx == 0:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 3
						self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] = 3 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] = 3
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] = 3
						self.game_settings.drop_succeed = True
				elif self.rotation == 2:
					if self.game_settings.cordy == 0 or self.game_settings.cordy == 4 or self.game_settings.cordx == 4:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 3
						self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] = 3 
						self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] = 3
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] = 3
						self.game_settings.drop_succeed = True
				elif self.rotation == 3:
					if self.game_settings.cordy == 4 or self.game_settings.cordx == 4 or self.game_settings.cordx == 0:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 3
						self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] = 3 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] = 3
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] = 3
						self.game_settings.drop_succeed = True
				elif self.rotation == 4:
					if self.game_settings.cordy == 0 or self.game_settings.cordy == 4 or self.game_settings.cordx == 0:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 3
						self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] = 3 
						self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] = 3
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] = 3
						self.game_settings.drop_succeed = True
			elif self.shape == 4:
				if self.rotation == 1 or self.rotation == 3:
					if self.game_settings.cordy == 0 or self.game_settings.cordy == 4:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 4
						self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] = 4 
						self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] = 4
						self.game_settings.drop_succeed = True
				elif self.rotation == 2 or self.rotation == 4:
					if self.game_settings.cordx == 0 or self.game_settings.cordx == 4:
						self.game_settings.drop_succeed = False
					elif self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] != 0:
						self.game_settings.drop_succeed = False
					else: 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 4
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] = 4 
						self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] = 4
						self.game_settings.drop_succeed = True
			elif self.shape == 5:
				if self.game_settings.cordy == 0 or self.game_settings.cordy == 4 or self.game_settings.cordx == 0 or self.game_settings.cordx == 4:
						self.game_settings.drop_succeed = False
				elif self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] != 0 or self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] != 0:
					self.game_settings.drop_succeed = False
				else:
					self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx] = 5
					self.game_settings.board[self.game_settings.cordy+1][self.game_settings.cordx] = 5 
					self.game_settings.board[self.game_settings.cordy-1][self.game_settings.cordx] = 5
					self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx+1] = 5 
					self.game_settings.board[self.game_settings.cordy][self.game_settings.cordx-1] = 5
					self.game_settings.drop_succeed = True
