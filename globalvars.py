import pygame

FPS = 60

# Global Camera Offset
OFFSETX = 0
OFFSETY = 0

# Images to use
IMAGESDICT = {	'space': pygame.image.load('.\\art\\space.jpg'),
				'earth': pygame.image.load('.\\art\\earth1.png')}

DISPLAYSURF = pygame.display.set_mode((640, 448)) # Make a display
pygame.display.set_caption('Space Pirates') # Make name for window
