import pygame
from pygame.locals import *
import time
import random

import utilities as u
import classes
import utilityClasses as uC

import cfg # All global variables and stuff

def handleScrolling(mouseButtonsPressed, scrollObj):
	"""Handles scrolling and sets global offset variables."""
	# Scroll if we need to
	if mouseButtonsPressed[0]: # If mouse1 is pressed
		# Update the scroll object
		scrollObj.update(pygame.math.Vector2(pygame.mouse.get_rel()))
	else:
		# If mouse1 is not pressed, reset the instance.
		scrollObj.reset()

	if scrollObj:
		# We are going to scroll move all entities
		for background in cfg.LAYERS['background']:
			background.move((scrollObj.relativeDrag().x/10, scrollObj.relativeDrag().y/10))

		for entity in cfg.LAYERS['middleground']:
			entity.move((scrollObj.relativeDrag().x, scrollObj.relativeDrag().y))

		for entity in cfg.LAYERS['foreground']:
			entity.move((scrollObj.relativeDrag().x, scrollObj.relativeDrag().y))

		for entity in cfg.LAYERS['buttons']:
			entity.move((scrollObj.relativeDrag().x, scrollObj.relativeDrag().y))

	pygame.mouse.get_rel() 	# Update where we last dragged from

def makeSystem():
	"""Makes a little planet system."""
	P = []
	for _ in xrange(4):
		planet = classes.Planet(pygame.Rect((random.randint(50, 600), random.randint(50, 400)),(40, 40)))
		P.append(planet)
	return P

def draw():
	"""Draw phase of the game."""
	# Draws the game from the back to the front
	# beginning with the backgroundk3
	for background in cfg.LAYERS['background']:
		background.draw()
	# Draw the mdidleground, planets, stars etc
	for entity in cfg.LAYERS['middleground']:
		entity.draw()
	# Draw the foreground, ships etc.
	for entity in cfg.LAYERS['foreground']:
		entity.draw()
	# Draw the UI, buttons, textboxes etc.
	for box in cfg.LAYERS['buttons']:
		box.draw()

def setUpLayers():
	# MAKE SOME SPACE
	# Add the background
	cfg.LAYERS['background'] = [classes.Background(cfg.IMAGESDICT['space'])]
	# Add some planets
	cfg.LAYERS['middleground'] = makeSystem()

	# Add one ship
	ship = classes.Ship()
	ship.destinations = [] # No destinations yet
	ship.currentDestination = 0

	# Add the ship to the foreground
	cfg.LAYERS['foreground'] = [ship]

	# Add a button
	button = classes.Button((40, 40), (400, 400))

	cfg.LAYERS['buttons'] = [button]

def main():
	fpsClock = pygame.time.Clock()

	# Initialize pygame modules
	u.initializeModules()

	# Make some general instances of stuff
	scrollObj = uC.MouseScroll() # Make a mouse-scroll instance

	u.clearScreen() # Shitty way to clear cmd

	u.playMusic('.\\music\\weightlessness.mp3')

	setUpLayers()

	while True:
		# Main game loop
		pygame.event.pump() # Get stuff from keyboard and stuff
		mouseButtonsPressed = pygame.mouse.get_pressed() # Which mouse buttons are pressed
		keysPressed = pygame.key.get_pressed() # Get which keys are currently pressed

		# Terminate if we should
		u.checkTermination(keysPressed)

		for event in pygame.event.get():
			# Firstly, handle what happens to the selected object
			if cfg.SELOBJ is not None:
				cfg.SELOBJ.action(event)
			if event.type is QUIT:
			    # Quit the game
			    u.terminate()

			if event.type is MOUSEBUTTONDOWN:
				# If we press the mouse and we are not scrolling,
				# make a rect object to check what we clicked
				if event.button is 1: # Left click
					None

				if event.button is 3: # Right click
					cfg.LAYERS['foreground'][0].nextDest()

			if event.type is MOUSEBUTTONUP:
				if event.button is 1 and not scrollObj: # Left click release
					cfg.SELOBJ =  u.click(event.pos)

				if event.button is 2:
					cfg.SELOBJ = None # Deselect the selected object

		# Handle scrolling
		handleScrolling(mouseButtonsPressed, scrollObj)

		# ________UPDATE GAME STATE________
		cfg.LAYERS['foreground'][0].moveToEndPoint()

		# ________DRAW PHASE________
		draw()
		if cfg.SELOBJ is not None:
			pygame.draw.rect(cfg.DISPLAYSURF, (255, 0, 0), cfg.SELOBJ.rect, 3)
		#________LAST PART OF CYCLE________

		pygame.display.update()
		fpsClock.tick(cfg.FPS)

if __name__ == '__main__':
	main()
