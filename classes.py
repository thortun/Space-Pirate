# Python classes for Space Pirate
import pygame
import utilities as u

import random

class Entity():
	"""Abstract entity class."""
	def __init__(self, rect = pygame.rect.Rect(0, 0, 0, 0)):
		self.rect = rect # Entity has a rect associated with it

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

	def draw(self, surface, OFFSETX, OFFSETY):
		"""Draws the planet to the surface."""
		drawPosition = (int(self.rect.center[0] + OFFSETX), int(self.rect.center[1] + OFFSETY))
		pygame.draw.circle(surface, self.color, drawPosition, self.rect.width/2)

class Star(CelestialObject):
	"""Star class."""
	def __init__(self, rect = pygame.Rect(0, 0, 0, 0)):
		CelestialObject.__init__(self, rect)
		self.color = (random.randint(0, 255), 0, 0)
		self.name = u.randomLineFromFile('.\\names\\stars.txt') # Name of the Planet

	def __str__(self):
		return 'Star: ' + self.name

	def draw(self, surface, OFFSETX, OFFSETY):
		"""Draws the planet to the surface."""
		drawPosition = (int(self.rect.center[0] + OFFSETX), int(self.rect.center[1] + OFFSETY))
		pygame.draw.circle(surface, self.color, drawPosition, self.rect.width/2)