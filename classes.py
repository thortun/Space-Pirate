# Python classes for Space Pirate
import pygame
import random

import utilities as u
import utilityClasses as uC

import cfg # Global variables and stuff

class Entity():
	"""Abstract entity class."""
	def __init__(self, rect = pygame.rect.Rect(0, 0, 0, 0)):
		self.rect = rect # Entity has a rect associated with it
		# Need to store the position to be able to move object with more than integer precision
		self.position = pygame.math.Vector2(self.rect.left, self.rect.top)
	def move(self, shift):
		"""Moves by the touple 'shift'."""
		self.position += pygame.math.Vector2(shift)

	def getRect(self):
		"""Returns the rect for drawing."""
		return pygame.rect.Rect((int(self.position[0]), int(self.position[1])), self.rect.size)

class ClickableEntity(Entity):
	def __init__(self, rect = pygame.rect.Rect(0, 0, 0, 0)):
		Entity.__init__(self, rect)

class CelestialObject(ClickableEntity):
	"""Abstract class of celestial objects."""
	def __init__(self, rect = pygame.Rect(0, 0, 0, 0)):
		ClickableEntity.__init__(self, rect) # Use super-class init

class Planet(CelestialObject):
	"""Planet class."""
	def __init__(self, rect = pygame.Rect(0, 0, 0, 0)):
		CelestialObject.__init__(self, rect)
		self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
		self.name = u.randomLineFromFile('.\\names\\planets.txt') # Name of the Planet

	def __str__(self):
		return 'Planet: ' + self.name

	def draw(self):
		"""Draws the planet to the surface."""
		drawPosition = Entity.getRect(self).center
		pygame.draw.circle(cfg.DISPLAYSURF, self.color, drawPosition, int(cfg.ZOOM*self.rect.width/2))

	def click(self):
		"""Click on a planet."""
		print "Clicked on ", self

class Star(CelestialObject):
	"""Star class."""
	def __init__(self, rect = pygame.Rect(0, 0, 0, 0)):
		CelestialObject.__init__(self, rect)
		self.color = (random.randint(100, 255), 0, 0)
		self.name = u.randomLineFromFile('.\\names\\stars.txt') # Name of the Planet

	def __str__(self):
		return 'Star: ' + self.name

	def draw(self):
		"""Draws the planet to the surface."""
		drawPosition = Entity.getRect(self).center
		pygame.draw.circle(cfg.DISPLAYSURF, self.color, drawPosition, self.rect.width/2)

class Background(Entity):
	def __init__(self, image = None):
		Entity.__init__(self, image.get_rect())
		self.image = image

	def draw(self):
		cfg.DISPLAYSURF.blit(self.image, Entity.getRect(self))
