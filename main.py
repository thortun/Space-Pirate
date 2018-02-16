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
	if mouseButtonsPressed[0]:
		scrollObj.update(pygame.math.Vector2(pygame.mouse.get_rel()))
	else:
		scrollObj.reset()

	if scrollObj:
		# We are going to scroll move all entities
		for entity in cfg.ENTITIES:
			# Move planets:
			if isinstance(entity, classes.CelestialObject):
				entity.move((scrollObj.relativeDrag().x, scrollObj.relativeDrag().y))
			# Move background
			if isinstance(entity, classes.Background):
				entity.move((scrollObj.relativeDrag().x/10, scrollObj.relativeDrag().y/10))

			if isinstance(entity, classes.Ship):
				entity.move((scrollObj.relativeDrag().x, scrollObj.relativeDrag().y))

def makeSystem():
	"""Makes a little planet system."""
	P = []
	for _ in xrange(4):
		planet = classes.Planet(pygame.Rect((random.randint(50, 600), random.randint(50, 400)),(40, 40)))
		P.append(planet)
	return P

def draw():
	"""Draw phase of the game."""
	# Draw all entities
	for entity in cfg.ENTITIES:
		entity.draw()

def main():
	
	fpsClock = pygame.time.Clock()

	# Initialize pygame modules
	u.initializeModules()

	# Make some general instances of stuff
	scrollObj = uC.MouseScroll() # Make a mouse-scroll instance

	clickRect = uC.ClickRect() # Rect to check what we are clicking


	# MAKE SOME SPACE
	# Add the background
	cfg.ENTITIES = [classes.Background(cfg.IMAGESDICT['space'])]
	# Add some planets
	for planet in makeSystem():
		cfg.ENTITIES.append(planet)

	clickObj = uC.Clickable(cfg.ENTITIES)

	clickedObject = None
	textBox = uC.TextBox()

	ship = classes.Ship()
	ship.destinations = cfg.ENTITIES[1:]
	ship.currentDestination = 0
	cfg.ENTITIES.append(ship)

	u.clearScreen() # Shitty way to clear cmd



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
				if event.button is 1: # Left click
					clickObj.click(event.pos)

				if event.button is 3: # Right click
					ship.nextDest()

				# Button 4 is scrolling backwards
				# Button 5 is scrolling forwards
				if event.button is 4:
					# Zoom the camera
					cfg.ZOOM = cfg.ZOOM*1.2
					# Move the planets
					for ent in cfg.ENTITIES[1:]:
						moveVector = pygame.math.Vector2( ent.position.x - cfg.SCREENCENTER[0], ent.position.y - cfg.SCREENCENTER[1])
						moveVector = moveVector.normalize()
						moveVector.length()
						ent.move(10*moveVector)

				if event.button is 5:
					# Zoom the camera
					cfg.ZOOM = cfg.ZOOM/1.2
					for ent in cfg.ENTITIES[1:]:
						moveVector = pygame.math.Vector2( ent.position.x - cfg.SCREENCENTER[0], ent.position.y - cfg.SCREENCENTER[1])
						moveVector = moveVector.normalize()
						ent.move(-10*moveVector)

			if event.type is MOUSEBUTTONUP:
				if event.button is 1 and not scrollObj: # Left click release
					clickedObject = clickObj.click(event.pos)

			if event.type is KEYDOWN:
				if event.key is K_UP:
					# Zoom in
					cfg.ZOOM = cfg.ZOOM*1.2

				if event.key is K_DOWN:
					# Zoom out
					None

		# Handle scrolling
		handleScrolling(mouseButtonsPressed, scrollObj)

		# ________UPDATE GAME STATE________
		pygame.mouse.get_rel() 	# Update scroll object
		# Click on the entity if it is clickable
		if clickedObject is not None and isinstance(clickedObject, classes.ClickableEntity):
			clickedObject.click()

		# Reset the click
		clickedObject = None
		ship.moveToEndPoint()
		# ________DRAW PHASE________
		draw()
		#________LAST PART OF CYCLE________
		# Reset the click

		clickRect.isActive = False

		pygame.display.update()
		fpsClock.tick(cfg.FPS)

if __name__ == '__main__':
    main()
