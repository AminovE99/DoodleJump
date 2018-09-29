import pygame

import Doodler


class Platform(pygame.sprite.Sprite):
	start = (0, 0)
	end = (0, 0)
	doodler = 9

	def __init__(self, start, end, doodler):
		super(Platform, self).__init__()
		self.image = pygame.image.load('static/platform.png')
		self.start = start
		self.end = end
		self.doodler = doodler
		self.rect = self.image.get_rect()
