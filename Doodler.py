import pygame


class Doodler(pygame.sprite.Sprite):
	width = 10
	height = 5
	jumpCount = 10
	x = 600
	y = 600
	isJump = False
	speed = 5

	def __init__(self):
		super(Doodler, self).__init__()
		self.image = pygame.image.load('static/icon.png')
		self.rect = self.image.get_rect()
