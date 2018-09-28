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

	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.x -= self.speed
		if keys[pygame.K_RIGHT]:
			self.x += self.speed

	def collide(self,sprite):
		if pygame.sprite.spritecollide(sprite,sprite,False):
			#TODO: Дописать нормально столкновение


