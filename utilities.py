# Utilities
import pygame, sys
from pygame.locals import *
import random

import cfg

def playMusic(filename):
	"""Plays the music from the path 'filename'.
	Plays 'weightlessness if we can not open the file.
	"""
	try:
		pygame.mixer.music.load(filename)
	except pygame.error:
		pygame.mixer.music.load('.\\music\\weightlessness.mp3')
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play()

def initializeModules():
	"""Initiazlises the modules we are going to use."""
	pygame.init() # Initialize the game
	pygame.font.init() # Initialize fonts
	if not pygame.font.get_init():
		print 'pygame.font failed to initialize'

def checkTermination(buttonsPressed):
	"""Checks if we should terminate the game based
	on which buttons are pressed."""
	if (buttonsPressed[K_LALT] and buttonsPressed[K_F4]) or buttonsPressed[K_ESCAPE]:
		terminate()

def terminate():
    pygame.quit()
    sys.exit()

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

def randomLineFromFile(filepath):
	"""Finds a random line from a file and returns it."""
	fileID = open(filepath)
	fileLength = 0 # Number of lines in the file
	# Find the number of lines in the file
	for line in fileID:
		fileLength += 1 # Iterate fileLength

	# Make a variable to pick a random line
	r = random.randint(0, fileLength - 1)
	fileID.seek(0) # Go back to the start of the file
	# Find the line corresponding to r
	for i, line in enumerate(fileID):
		if i == r:
			return line.replace('\n', '')
	return 'NONAME'

def clearScreen():
	"""Clear the screen xD"""
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'


def click(mousePosition):
	"""Handles clicking on any position on the screen."""
	clickRect = pygame.rect.Rect(mousePosition, (5, 5))
	# Start with foreground
	for thing in cfg.LAYERS['buttons']:
		if not clickRect.collidelist([thing]):
			# If we click it, click it
			thing.click()
			# Return which object we clicked
			return thing

	# Next is the foreground
	for thing in cfg.LAYERS['foreground']:
		if not clickRect.collidelist([thing]):
			# If we click it, click it
			thing.click()
			# Return which object we clicked
			return thing

	# Next is the middleground
	for thing in cfg.LAYERS['middleground']:
		if not clickRect.collidelist([thing]):
			# If we click it, click it
			thing.click()
			# Return which object we clicked
			return thing
			