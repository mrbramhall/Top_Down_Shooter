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
GRASS =      "grass64.png"
DIRT =       "dirt32.png"
WATER =      "water16.png"
SANDI = "sandi_face.png"

# Tile length (all are square)
TILE_LENGTH = 32

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
sandiTile = pygame.image.load(PATH_TO_TILES + SANDI)

# Create Rect objects for tiles
grassRect = grassTile.get_rect()
dirtRect =  dirtTile.get_rect()
waterRect = waterTile.get_rect()
sandiRect = sandiTile.get_rect()

# Create a background surface
background = pygame.Surface((WINDOW_DIMENSIONS))
for x in xrange(0, WINDOW_WIDTH, TILE_LENGTH):
    for y in xrange(0, WINDOW_HEIGHT, TILE_LENGTH):
        background.blit(dirtTile, (x, y))

# Initialize list for projectile coordinates
# Will store [x, y] coords
projectileCoords = list();

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

        # Shoot on left-click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print "BUTTON 1"
                print str(event.pos)
                if sandiRect.collidepoint(event.pos):
                    print "You clicked on Sandi!"
            if event.button == 2:
                print "BUTTON 2"
                print str(event.pos)
            if event.button == 3:
                print "BUTTON 3"
                print str(event.pos)

    # Movement of Sandi
    if pygame.key.get_pressed()[pygame.K_w]:
        if sandiRect.top > 0:
            sandiRect = sandiRect.move([0, -1])
    if pygame.key.get_pressed()[pygame.K_a]:
        if sandiRect.left > 0:
            sandiRect = sandiRect.move([-1, 0])
    if pygame.key.get_pressed()[pygame.K_s]:
        if sandiRect.bottom < WINDOW_HEIGHT:
            sandiRect = sandiRect.move([0, 1])
    if pygame.key.get_pressed()[pygame.K_d]:
        if sandiRect.right < WINDOW_WIDTH:
            sandiRect = sandiRect.move([1, 0])

    # DRAWING TO SCREEN

    # Blit background to screen
    screen.blit(background, (0, 0))

    # Draw a line from the grass tile to the mouse pointer
    pygame.draw.line(screen, WHITE, sandiRect.center, pygame.mouse.get_pos(), 1)

    # Draw a target at the position of the mouse pointer
    pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), 4)

    # Draw the grass tile
    screen.blit(sandiTile, sandiRect)

    # Update screen
    pygame.display.flip()
