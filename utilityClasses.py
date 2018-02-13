# Utility Classes
import pygame

import cfg


class MouseScroll():
	"""Class to scroll the camera."""
	def __init__(self, threshold = 35):
		self.dragged = pygame.math.Vector2(0.0, 0.0) # How far we have dragged the mouse while holding down mouse1
		self.activationThreshold = threshold # How far we need to drag the mouse to start scrolling
		self.lastDragged = pygame.math.Vector2(0.0, 0.0) # The last position of the mouse, to help scroll

	def __nonzero__(self):
		"""Bool to check if we should start scrolling.
		Returns TRUE if we have scrolled far enough while
		mouse1 is pressed.
		"""
		return self.dragged.length() > self.activationThreshold

	def __str__(self):
		return 'MouseScroll instance'

	def reset(self):
		"""Resets the scroll."""
		self.lastDragged = pygame.math.Vector2(0.0, 0.0)
		self.dragged = pygame.math.Vector2(0.0, 0.0)

	def update(self, vector):
		"""Updates how far the mouse has scrolled."""
		self.lastDragged = pygame.math.Vector2(self.dragged) # Update the previous drag
		self.dragged += vector # Update how far we scrolled

	def relativeDrag(self):
		"""Returns how far we have scrolled since last update."""
		return self.dragged - self.lastDragged

class ClickRect():
	"""Class to see what we clicked."""
	def __init__(self, rect = pygame.Rect(0, 0, 0, 0)):
		self.isActive = False
		self.rect = rect

	def __nonzero__(self):
		return self.isActive

class Node():
	"""General Node class."""
	def __init__(self, instance):
		"""Makes a node object. The content of the node
		is an object instance of some sort.
		"""
		self.children = []
		self.content = instance

	def __str__(self):
		return 'Node containing a ' + str(self.content)

	def __iter__(self):
		"""Iterator."""
		None

class TextBox():
	"""Textbox class to display information."""
	def __init__(self, text = '', pos = pygame.Rect(0, 0, 0, 0)):
		self.text = text
		self.font = pygame.font.Font(None, 25) # Font
		self.pos = pos

	def draw(self):
		"""Draws the textbox to the surface."""
		drawPosition = (self.pos.x + cfg.OFFSETX, self.pos.y + cfg.OFFSETY) 
		cfg.DISPLAYSURF.blit(self.font.render(self.text, 0, (200, 200, 200)), drawPosition) # Blits the text to the surface

class Clickable():
	"""Class of clickable objects."""
	def __init__(self, objectList):
		self.objectList = objectList

	def click(self, mousePosition):
		"""Returns the object that we clicked on
		when clicking on mousePosition.
		 - mousePosition should be a touple
		 - Returns the object clicked, and None if nothing was clicked
		"""
		clickRect = ClickRect(pygame.Rect(mousePosition, (10, 10))) # Create a click object
		for obj in self.objectList:
			if not clickRect.rect.collidelist([obj.rect]):
				return obj
		return None

