import pygame
from pygame.locals import *
import time
import random

import utilities as u
import classes, utilityClasses

# Global variables

def handleScrolling(mouseButtonsPressed, scrollObj):
	"""Handles scrolling and sets global offset variables."""
	global OFFSETX, OFFSETY
	# Scroll if we need to
	if mouseButtonsPressed[0]:
		scrollObj.update(pygame.math.Vector2(pygame.mouse.get_rel()))
	else:
		scrollObj.reset()


	if scrollObj:
		# We are going to scroll, scroll
		OFFSETX += scrollObj.relativeDrag().x
		OFFSETY += scrollObj.relativeDrag().y

def makeSystem():
	"""Makes a little planet system."""
	return [classes.Planet(pygame.Rect((random.randint(50, 600), random.randint(50, 400)), IMAGESDICT['earth'].get_rect().size)),
			classes.Planet(pygame.Rect((random.randint(50, 600), random.randint(50, 400)), IMAGESDICT['earth'].get_rect().size)),
			classes.Planet(pygame.Rect((random.randint(50, 600), random.randint(50, 400)), IMAGESDICT['earth'].get_rect().size)),
			classes.Planet(pygame.Rect((random.randint(50, 600), random.randint(50, 400)), IMAGESDICT['earth'].get_rect().size))]

def draw():
	"""Draw phase of the game."""
	DISPLAYSURF.blit(IMAGESDICT['space'], pygame.Rect((0 + OFFSETX/20, 0 + OFFSETY/20), (100, 100))) # Get a smooth backdrop

def initializeModules():
	"""Initiazlises the modules we are going to use."""
	pygame.init() # Initialize the game
	pygame.font.init() # Initialize fonts
	if not pygame.font.get_init():
		print 'pygame.font failed to initialize'

def main():
	global DISPLAYSURF, IMAGESDICT, FPS, OFFSETX, OFFSETY
	FPS = 60

	# Global camera offset
	OFFSETX = 0
	OFFSETY = 0

	# Initialize clock
	fpsClock = pygame.time.Clock()

	# Initialize pygame modules
	initializeModules()

	# Images to use
	IMAGESDICT = {	'space': pygame.image.load('.\\art\\space.jpg'),
					'earth': pygame.image.load('.\\art\\earth1.png')}

	DISPLAYSURF = pygame.display.set_mode((640, 448)) # Make a display
	pygame.display.set_caption('Space Pirates') # Make name for window

	# Make some general instances of stuff
	scrollObj = utilityClasses.MouseScroll() # Make a mouse-scroll instance

	clickRect = utilityClasses.ClickRect() # Rect to check what we are clicking

	planets = makeSystem()
	clickObj = utilityClasses.Clickable(planets)

	clickedObject = None
	textBox = utilityClasses.TextBox()

	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
	print 'epple'
	while True:
		# Main game loop
		pygame.event.pump() # Get stuff from keyboard and stuff
		mouseButtonsPressed = pygame.mouse.get_pressed() # Which mouse buttons are pressed
		keysPressed = pygame.key.get_pressed() # Get which keys are currently pressed

		# Terminate if we should
		u.checkTermination(keysPressed)

		for event in pygame.event.get():
		    # View events
			if event.type is QUIT:
			    # Quit the game
			    u.terminate()

			if event.type is MOUSEBUTTONDOWN:
				# If we press the mouse and we are not scrolling,
				# make a rect object to check what we clicked
				if event.button is 1 and not scrollObj:
					clickObj.click(event.pos)
					clickRect.isActive = True # Activate the object
					clickRect.rect = pygame.Rect((0, 0), (10, 10)) # Update the rect variable of the object
					clickRect.rect.center = (event.pos[0] - OFFSETX, event.pos[1] - OFFSETY) # Center the rect

		# Handle scrolling
		handleScrolling(mouseButtonsPressed, scrollObj)

		# ________UPDATE GAME STATE________
		pygame.mouse.get_rel() 	# Update scroll object

		# ________DRAW PHASE________
		draw()

		somethingClicked = False
		for planet in planets:
			if (not clickRect.rect.collidelist([planet])) and clickRect:
				textBox = utilityClasses.TextBox(planet.name, pygame.Rect(planet.rect))
				clickedObject = planet
				somethingClicked = True
		
			planet.draw(DISPLAYSURF, OFFSETX, OFFSETY) # Draw all the planets

		# Draw info box
		clickedObject = None

		textBox.draw(DISPLAYSURF, OFFSETX, OFFSETY)
		#________LAST PART OF CYCLE________
		# Reset the click
		clickRect.isActive = False

		pygame.display.update()
		fpsClock.tick(FPS)

if __name__ == '__main__':
    main()

