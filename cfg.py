import pygame

FPS = 60

# Global Camera Offset
OFFSETX = 0
OFFSETY = 0

ZOOM = 1 # zoom scale

# Images to use
IMAGESDICT = {	'space': pygame.image.load('.\\art\\space.jpg'),
				'earth': pygame.image.load('.\\art\\earth1.png')}

SCREENWIDTH = 640
SCREENHEIGHT = 448

SCREENCENTER = (SCREENWIDTH//2, SCREENHEIGHT//2)

DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT)) # Make a display
pygame.display.set_caption('Space Pirates') # Make name for window