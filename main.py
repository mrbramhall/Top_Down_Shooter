""" Top-Down Shooter Game

DESCRIPTION:
    This game is all about shooting from the top-down
    perspective. Have fun! LOL

CONTROLS:
    wasd               ---> movement
    left-click         ---> shoot
    mouse movement     ---> aim
    e                  ---> open/close inventory
    mouse scroll       ---> iterate through quick-select items
    middle-mouse click ---> center camera on player
"""

import pygame

""" CONSTANTS """

# Name of game
GAME_NAME = "Top-Down Shooter"

# Path to tiles
PATH_TO_TILES = "images\\tiles\\"

# Backspace delimiter
BS = "\\"

# Tile names
GRASS = "grass64.png"
DIRT  = "dirt16.png"
WATER = "water16.png"

# Max fps setting
MAX_FPS = 60

# Window dimensions
WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT = (1280, 960)

# Colors in RGB format
BLACK = (  0,   0, 255)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

""" CLASSES/FUNCTIONS """

""" MAIN """

# Initialize pygame
pygame.init()

# Display window initialization
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
pygame.display.set_caption(GAME_NAME)

# Load tiles
grassTile = pygame.image.load(PATH_TO_TILES + GRASS)
dirtTile =  pygame.image.load(PATH_TO_TILES + DIRT)
waterTile = pygame.image.load(PATH_TO_TILES + WATER)

# Create Rect objects for tiles
grassRect = grassTile.get_rect()
dirtRect =  dirtTile.get_rect()
waterRect = waterTile.get_rect()

# Will be used in main loop to limit FPS
fpsClock = pygame.time.Clock()

# Main game loop
while True:
    
    # Limit FPS
    fpsClock.tick(MAX_FPS)

    for event in pygame.event.get():

        # Quit when window is closed
        if event.type == pygame.QUIT:
            sys.exit()

    # Move grass tile
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if grassRect.right < WINDOW_WIDTH:
            grassRect = grassRect.move([1, 0])

    # Update screen
    screen.fill(BLACK)
    screen.blit(grassTile, grassRect)
    pygame.display.flip()


