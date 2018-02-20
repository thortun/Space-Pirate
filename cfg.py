import pygame
from pygame.locals import *
FPS = 60

ZOOM = 1 # zoom scale

# Images to use
IMAGESDICT = {	'space': pygame.image.load('.\\art\\space.jpg'),
				'earth': pygame.image.load('.\\art\\earth1.png')}

SCREENWIDTH = 640
SCREENHEIGHT = 448

SCREENCENTER = (SCREENWIDTH//2, SCREENHEIGHT//2)
SCREENCENTERX, SCREENCENTERY = SCREENCENTER[0], SCREENCENTER[1]


# ________CONTAINERS________ #
ENTITIES = [] # List of all current entities

LAYERS = {} # Layer dictionary
LAYERS['background'] = None
LAYERS['middleground'] = [] # Planets, stations etc
LAYERS['foreground'] = [] # Ships
LAYERS['buttons'] = [] # Buttons, always in the foreground. Also text boxes and stuff, UI

# ________IMPORTANT OBJECTS________ #
SELOBJ = None # The object which is currently selected

DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT)) # Make a display
pygame.display.set_caption('Space Pirates') # Make name for window