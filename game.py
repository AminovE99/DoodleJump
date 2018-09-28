import pygame
from Doodler import Doodler
from Platform import Platform
import random

pygame.init()
win = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Doodle Jump")
run = True

WHITE = (255, 255, 255)
BLUE = (0, 0, 155)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)


def jump():
	doodler.isJump = True
	if (doodler.jumpCount >= -10):
		if (doodler.jumpCount < 0):
			doodler.y += int(doodler.jumpCount ** 2 / 2)
		else:
			doodler.y -= int(doodler.jumpCount ** 2 / 2)
		doodler.jumpCount -= 1
	else:
		doodler.isJump = False
		doodler.jumpCount = 10


doodler = Doodler()
platform = Platform()

while run:
	win.blit(doodler.image, [doodler.x, doodler.y])
	win.blit(platform.image, [platform.x,platform.y])
	doodler.update()
	if pygame.sprite.spritecollide(doodler.image, platform.image,True):
		print('fdsa')
	jump()
	pygame.display.update()

	pygame.time.delay(50)
	win.fill((255, 255, 255))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

pygame.quit()
