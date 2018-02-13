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
		# We are going to scroll, scroll
		cfg.OFFSETX += scrollObj.relativeDrag().x
		cfg.OFFSETY += scrollObj.relativeDrag().y

def makeSystem():
	"""Makes a little planet system."""
	return [classes.Planet(pygame.Rect((random.randint(50, 600), random.randint(50, 400)), cfg.IMAGESDICT['earth'].get_rect().size)),
			classes.Planet(pygame.Rect((random.randint(50, 600), random.randint(50, 400)), cfg.IMAGESDICT['earth'].get_rect().size))]
			#classes.Planet(pygame.Rect((random.randint(50, 600), random.randint(50, 400)), cfg.IMAGESDICT['earth'].get_rect().size)),
			#classes.Planet(pygame.Rect((random.randint(50, 600), random.randint(50, 400)), cfg.IMAGESDICT['earth'].get_rect().size))]

def draw():
	"""Draw phase of the game."""
	cfg.DISPLAYSURF.blit(cfg.IMAGESDICT['space'], pygame.Rect((0 + cfg.OFFSETX/20, 0 + cfg.OFFSETY/20), (100, 100))) # Get a smooth backdrop
	# Draw center of screen
	pygame.draw.circle(cfg.DISPLAYSURF, (255, 0, 0), cfg.SCREENCENTER, 2)
	# cfg.DISPLAYSURF, self.color, drawPosition, int(cfg.ZOOM*self.rect.width/2)

def initializeModules():
	"""Initiazlises the modules we are going to use."""
	pygame.init() # Initialize the game
	pygame.font.init() # Initialize fonts
	if not pygame.font.get_init():
		print 'pygame.font failed to initialize'

def clearScreen():
	"""Clear the screen xD"""
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

def main():
	# Global camera offset

	fpsClock = pygame.time.Clock()

	# Initialize pygame modules
	initializeModules()

	# Make some general instances of stuff
	scrollObj = uC.MouseScroll() # Make a mouse-scroll instance

	clickRect = uC.ClickRect() # Rect to check what we are clicking

	planets = makeSystem()
	clickObj = uC.Clickable(planets)

	clickedObject = None
	textBox = uC.TextBox()

	clearScreen() # Shitty way to clear cmd

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
					None
					# clickedObject = clickObj.click(event.pos)
				if event.button is 3: # Right click
					cfg.ZOOM = 1
					clickedObj = None
					cfg.OFFSETX, cfg.OFFSETY = 0, 0

				# Button 4 is scrolling backwards
				# Button 5 is scrolling forwards
				if event.button is 4:
					# Zoom the camera
					cfg.ZOOM = cfg.ZOOM*1.2
					# Move the planets
					for planet in clickObj.objectList:
						moveVector = pygame.math.Vector2(cfg.SCREENCENTER[0] - planet.rect.center[0] - cfg.OFFSETX, cfg.SCREENCENTER[1] - planet.rect.center[1] - cfg.OFFSETX)
						moveVector.normalize()
						planet.move(moveVector)

				if event.button is 5:
					# Zoom the camera
					cfg.ZOOM = cfg.ZOOM/1.2
					# Move the planets


			if event.type is MOUSEBUTTONUP:
				if event.button is 1 and not scrollObj: # Left click release
					clickedObject = clickObj.click(event.pos)

		# Handle scrolling
		handleScrolling(mouseButtonsPressed, scrollObj)

		# ________UPDATE GAME STATE________
		pygame.mouse.get_rel() 	# Update scroll object
		if clickedObject is not None:
			clickedObject.click()
		# Reset the click
		clickedObject = None

		# ________DRAW PHASE________
		draw()

		for planet in planets:
			if (not clickRect.rect.collidelist([planet])) and clickRect:
				textBox = uC.TextBox(planet.name, pygame.Rect(planet.rect))
				clickedObject = planet
		
			planet.draw() # Draw all the planets

		# Draw lines from center to planet
		# line(Surface, color, start_pos, end_pos, width=1)
		for planet in clickObj.objectList:
			pygame.draw.line(cfg.DISPLAYSURF, (255, 0, 0), (cfg.SCREENCENTER[0] , cfg.SCREENCENTER[1] )\
				, (planet.rect.center[0] + cfg.OFFSETX, planet.rect.center[1] + cfg.OFFSETY), 2)


		# Draw info box
		# clickedObject = None

		textBox.draw()
		#________LAST PART OF CYCLE________
		# Reset the click

		clickRect.isActive = False

		pygame.display.update()
		fpsClock.tick(cfg.FPS)

if __name__ == '__main__':
    main()
