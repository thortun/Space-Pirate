import pygame

FPS = 60

ZOOM = 1 # zoom scale

# Images to use
IMAGESDICT = {	'space': pygame.image.load('.\\art\\space.jpg'),
				'earth': pygame.image.load('.\\art\\earth1.png')}

SCREENWIDTH = 2*640
SCREENHEIGHT = 2*448

SCREENCENTER = (SCREENWIDTH//2, SCREENHEIGHT//2)

OFFSETX, OFFSETY = 0, 0

ENTITIES = [] # List of current entities

DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT)) # Make a display
pygame.display.set_caption('Space Pirates') # Make name for window