import pygame
from pygame.sprite import collide_rect

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
platforms = []
cameray = 0
sprite_group = pygame.sprite.Group()




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


def generatePlatforms():
	on = 600
	while on > -100:
		x = random.randint(0, 700)
		platform = random.randint(0, 1000)
		if platform < 800:
			platform = 0
		elif platform < 900:
			platform = 1
		else:
			platform = 2
		platforms.append([x, on, platform, 0])
		on -= 50


def drawPlatforms():
	for p in platforms:
		check = platforms[1][1] - cameray
		if check > 600:
			platform = random.randint(0, 1000)
			if platform < 800:
				platform = 0
			elif platform < 900:
				platform = 1
			else:
				platform = 2

			platforms.append([random.randint(0, 700), platforms[-1][1] - 50, platform, 0])
			coords = platforms[-1]
			check = random.randint(0, 1000)
			platforms.pop(0)
			win.blit(doodler.image, (p[0], p[1] - cameray))





def drawGrid():
	for x in range(80):
		pygame.draw.line(win, (222, 222, 222), (x * 12, 0), (x * 12, 600))
		pygame.draw.line(win, (222, 222, 222), (0, x * 12), (800, x * 12))


doodler = Doodler()
generatePlatforms()

while run:
	# drawGrid()
	win.blit(doodler.image, [doodler.x, doodler.y])
	generatePlatforms()
	drawPlatforms()
	sprite_group.draw(win)
	doodler.update()
	jump()
	pygame.display.update()

	pygame.time.delay(50)
	win.fill((255, 255, 255))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

pygame.quit()
