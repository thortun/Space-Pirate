# Utilities
import pygame, sys
from pygame.locals import *
import random

import cfg


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
	r = random.randint(0, fileLength)
	fileID.seek(0) # Go back to the start of the file
	# Find the line corresponding to r
	for i, line in enumerate(fileID):
		if i == r:
			return line.replace('\n', '')
	return 'NONAME'