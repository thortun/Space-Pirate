# Python classes for Space Pirate
import pygame
import random
from pygame.locals import *

import utilities as u
import utilityClasses as uC

import cfg # Global variables and stuff

class Entity():
	"""Abstract entity class."""
	def __init__(self, rect = pygame.rect.Rect(0, 0, 0, 0)):
		self.rect = rect # Entity has a rect associated with it
		# Need to store the position to be able to move object with more than integer precision
		self.position = pygame.math.Vector2(self.rect.topleft)
	def move(self, shift):
		"""Moves by the touple 'shift'."""
		self.position += pygame.math.Vector2(shift)
		self.rect.topleft = self.position # Set the position

	def getRect(self):
		"""Returns the rect for drawing."""
		return pygame.rect.Rect((int(self.position[0]), int(self.position[1])), self.rect.size)

	def action(self, event):
		"""Abstract function to handle events for selected object."""
		return None

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
		Entity.__init__(self, pygame.rect.Rect(0, 0, 0, 0))
		self.image = image

	def draw(self):
		cfg.DISPLAYSURF.blit(self.image, self.getRect())

class Ship(ClickableEntity):
	"""Ship class."""
	def __init__(self, rect = pygame.rect.Rect(0, 0, 30, 20)):
		Entity.__init__(self, rect)
		# More variables
		self.destinations = [] # List of object indicating destinations
		currentDestination = None # Index of current destination

	def addDest(self, dest):
		"""Sets the destination for the ship."""
		self.destinations.append(dest)

	def nextDest(self):
		"""Returns the next destination.
		Return the first destination if we are currently
		at the last."""
		if self.destinations:
			self.currentDestination = (self.currentDestination + 1) % len(self.destinations)
			return self.destinations[self.currentDestination]
		else:
			return None

	def moveToEndPoint(self):
		"""Moves the ship towards the object."""
		if self.destinations:
			direction = pygame.math.Vector2(-self.position.x + self.getDest().position.x, -self.position.y + self.getDest().position.y)
			if direction.length() < 1:
				self.nextDest()
				return
			else:
				direction = direction.normalize()
				self.move((direction.x, direction.y))

	def draw(self):
		"""Draws the ship."""
		pygame.draw.rect(cfg.DISPLAYSURF, (200, 60, 60), pygame.rect.Rect(self.position, (30, 20)))

	def getDest(self):
		"""Gets the current destination of the ship."""
		if self.destinations and self.currentDestination is not None:
			return self.destinations[self.currentDestination]
		else:
			return None

	def click(self):
		print "Clicked on ship"

	def action(self, event):
		"""Handles what happens to the ship given an event."""
		if event.type is MOUSEBUTTONDOWN:
			# Mouse 2 click: Add destination
			if event.button is 3:
				# Add whatever we clicked on to the list of destinations
				self.destinations.append(u.click(event.pos))

class Button(ClickableEntity):
	"""Clickable Button."""
	def __init__(self, size = (0, 0), position = (0, 0)):
		"""Makes a button."""
		Entity.__init__(self, pygame.rect.Rect(position, size))

	def setPosition(self, position):
		"""Sets the position of the button."""
		self.position = position # Set the position variable
		self.rect.topleft = position # Set the position of the rectangle variable

	def click(self):
		"""Clicks the button. This is where we need 
		to have a lot of flexibility of the button.
		"""
		print "Clicked on ", self

	def draw(self):
		"""Draws the button to the display."""
		pygame.draw.rect(cfg.DISPLAYSURF, (0, 200, 100), self.rect)