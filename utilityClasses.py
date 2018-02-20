# Utility Classes
import pygame

# Local modules
import cfg

class MouseScroll():
	"""Class to scroll the camera."""
	def __init__(self, threshold = 35):
		self.dragged = pygame.math.Vector2(0.0, 0.0) # How far we have dragged the mouse while holding down mouse1
		self.activationThreshold = threshold # How far we need to drag the mouse to start scrolling
		self.lastDragged = pygame.math.Vector2(0.0, 0.0) # The last position of the mouse, to help scroll
		self.distanceDragged = 0

	def __nonzero__(self):
		"""Bool to check if we should start scrolling.
		Returns TRUE if we have scrolled far enough while
		mouse1 is pressed.
		"""
		return self.distanceDragged > self.activationThreshold

	def __str__(self):
		return 'MouseScroll instance'

	def reset(self):
		"""Resets the scroll."""
		self.lastDragged = pygame.math.Vector2(0.0, 0.0)
		self.dragged = pygame.math.Vector2(0.0, 0.0)
		self.distanceDragged = 0

	def update(self, vector):
		"""Updates how far the mouse has scrolled."""
		self.lastDragged = pygame.math.Vector2(self.dragged) # Update the previous drag
		self.dragged += vector # Update how far we scrolled
		self.distanceDragged += self.relativeDrag().length()

	def relativeDrag(self):
		"""Returns how far we have scrolled since last update."""
		return self.dragged - self.lastDragged

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
		self.text = text.split('\n')
		self.font = pygame.font.Font(None, 25) # Font
		self.pos = pos

	def __nonzero__(self):
		pass

	def draw(self):
		"""Draws the textbox to the surface."""
		textSize = [0, 0]
		numLines = 0
		# Find the largest text size
		for line in self.text:
			if self.font.size(line)[0] > textSize[0]:
				textSize[0] = self.font.size(line)[0]
			if self.font.size(line)[1] > textSize[1]:
				textSize[1] = self.font.size(line)[1]
			numLines += 1

		backRect = pygame.rect.Rect(self.pos.topleft, (textSize[0], textSize[1]*numLines)) # Make the background rectangle
		pygame.draw.rect(cfg.DISPLAYSURF, (255, 255, 255), backRect) # Blit the white background
		pygame.draw.rect(cfg.DISPLAYSURF, (0, 0, 255), pygame.rect.Rect(self.pos[0] - 3, self.pos[1] - 3, textSize[0] + 6, textSize[1]*numLines + 6), 5)
		for i, line in enumerate(self.text):
			cfg.DISPLAYSURF.blit(self.font.render(line, 0, (200, 200, 0)), (self.pos.x, self.pos.y + 18*i)) # Blits the text to the surface

class Layer():
	"""Layer class. Each layer should contain
	a set of entities. When the player interacts with 
	the game, we search through layers to make sure that
	we do not interact with object behind stuff.
	"""
	def __init__(self, layerNumber):
		"""Initiazlies the layer."""
		self.layerNumber = layerNumber