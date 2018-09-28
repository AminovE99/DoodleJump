import pygame
from Doodler import Doodler
import random

pygame.init()
win = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Doodle Jump")
run = True

WHITE = (255, 255, 255)
BLUE = (0, 0, 155)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BGCOLOR = BLUE


def jump():
	doodler.isJump = True
	if (doodler.jumpCount >= -10):
		if (doodler.jumpCount < 0):
			doodler.y += int(doodler.jumpCount ** 2 / 3)
		else:
			doodler.y -= int(doodler.jumpCount ** 2 / 3)
		doodler.jumpCount -= 1
	else:
		doodler.isJump = False
		doodler.jumpCount = 10


doodler = Doodler()

pygame.draw.line(win, BLUE, (doodler.x, doodler.y - 20), (doodler.x, doodler.y - 20))
while (run):
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		doodler.x -= doodler.speed
	if keys[pygame.K_RIGHT]:
		doodler.x += doodler.speed
	win.blit(doodler.image, [doodler.x, doodler.y])
	jump()
	pygame.draw.line(win, (255, 0, 0), [500,550], [600, 600], 10)
	
	pygame.display.update()
	pygame.time.delay(50)
	win.fill((255, 255, 255))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

pygame.quit()
