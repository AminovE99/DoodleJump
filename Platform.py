import pygame


class Platform(pygame.sprite.Sprite):
	x = 500
	y = 550

	def __init__(self):
		super(Platform, self).__init__()
		self.image = pygame.image.load('static/platform.png')
		self.rect = self.image.get_rect()
