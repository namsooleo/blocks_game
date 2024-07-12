import pygame
from pygame import *
from settings import Settings
from block_pieces import Block_Piece
import game_functions 
import draw_functions 

def run_game():
    # Initialize pygame
    pygame.init()

    game_settings = Settings()
    clock = pygame.time.Clock() # Used to manage how fast the screen updates
    screen = pygame.display.set_mode(game_settings.WINDOW_SIZE) # Make window    
    pygame.display.set_caption("Blocks Game") # Set title of screen
    
    # TODO: Determine if these varialbles should be declared in another module/file
    # TODO: Write this into a single function    
    game_settings.current_piece = Block_Piece(game_settings)
    game_settings.current_piece.get_shape(game_settings)
    game_settings.next_piece = Block_Piece(game_settings)
    game_settings.next_piece.get_shape(game_settings)
    
    while True:
        game_settings.new_game = False # set to false, new game is starting

        # Set the screen background`
        screen.fill(game_settings.BLACK)
        
        # Draw the grid, hightlighted/cursor, and next up piece
        # TODO: Write this into a single function
        draw_functions.draw_board(game_settings, screen)
        draw_functions.drawHighlightBox(game_settings, screen) 
        draw_functions.drawNextBlock(game_settings, screen)
        draw_functions.draw_scoretext(game_settings, screen)
        draw_functions.draw_piecetext(screen)
        
        # Check for game over status return boolean then peform game_over "routine"
        game_settings.game_over = game_functions.game_over_check(game_settings)
        if game_settings.game_over:
            draw_functions.draw_game_over_screen(game_settings, screen)
            game_functions.check_play_again(game_settings)
            # If they clicked play again new is true and reset settings
            if game_settings.new_game:
                # TODO: Write this into a single function
                game_settings.board = [[0,0,0,0,0] for i in range(5)]
                game_settings.current_piece = Block_Piece(game_settings)
                game_settings.current_piece.get_shape(game_settings)
                game_settings.next_piece = Block_Piece(game_settings)
                game_settings.next_piece.get_shape(game_settings)
                game_settings.score = 0

        # Get user input
        game_functions.get_input(game_settings,screen)

        # Check for row/col clears
        game_functions.rc_check(game_settings)

        # Update screen
        pygame.display.flip()

if __name__ == "__main__":
    run_game()