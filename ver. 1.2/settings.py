# Class used to store all settings for BLocks; holds variables but not does manipulate them
class Settings():
    
    # Initialize game settings
    def __init__(self):

        # Game Colors
        self.WHITE       = (255, 255, 255)
        self.GRAY        = (185, 185, 185)
        self.BLACK       = (  0,   0,   0)
        self.RED         = (155,   0,   0)
        self.LIGHTRED    = (215,  60,  60)
        self.GREEN       = (  0, 155,   0)
        self.LIGHTGREEN  = ( 60, 215,  60)
        self.BLUE        = (  0,   0, 155)
        self.LIGHTBLUE   = ( 60,  60, 215)
        self.YELLOW      = (155, 155,   0)
        self.LIGHTYELLOW = (215, 215,   0)
        self.ORANGE      = (195, 105,   0)
        self.LIGHTORANGE = (255, 165,   0)
        self.PURPLE      = (128,   0, 128)
        self.LIGHTPURPLE = (188,  60, 188)

        # Screen Settings
        self.WIDTH = 50 # This sets the WIDTH and HEIGHT of each grid location
        self.HEIGHT = 50 # This sets the WIDTH and HEIGHT of each grid location
        self.MARGIN = 5 # This sets the margin between each cell        
        self.WINDOW_SIZE = [280, 560] # Set the WIDTH and HEIGHT of the screen
        
        # Board Settings
        self.board = [[0,0,0,0,0] for i in range(5)]
        self.cordx = 2 # X coordinate for moving "cursor" 
        self.cordy = 2 # Y coordinate for moving "cursor" 
        self.down_shift = 280 # used in draw_board and drawHighlightBox

        # Block Piece State settings
        self.number_blocks = 5 # used to determine which blocks spawn, 1-5. (eg. 4: 1-4 removes '+' block)
        self.current_piece = 0 # Current piece being dropped - 0 as placeholder
        self.next_piece = 0 # Next piece in queue and displayed - 0 as placeholder
        self.drop_succeed = False # Verify that a block was placed onto the board

        # Game State settings
        self.game_over = False  # check if game over 
        self.new_game = True # check if start of a new game
        self.score = 0 # Score at 0. Increment 100 for each line cleared currently TODO: Improve Scoring (10/14/20)

