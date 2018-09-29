import pygame
from pygame.sprite import collide_rect

from Doodler import Doodler
from Platform import Platform
import random

class DoodleJump:
	pygame.init()
	pygame.display.set_caption("Doodle Jump")
	platforms = [[400, 500]]  # координаты платформ


	def __init__(self):
		self.win = pygame.display.set_mode((700, 700))
		self.run = True
		self.platforms = [[400,500]]
		self.sprite_group = pygame.sprite.Group()# не надо?
		self.platform = pygame.image.load("static/platform.png").convert_alpha()
		self.playerX = 600 # Связать с классом Doodler
		self.playerY = 600

	# это в класс Дудлер
	def jump(self,doodler):
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


	def drawGrid(self):
		for x in range(80):
			pygame.draw.line(self.win, (222, 222, 222), (x * 12, 0), (x * 12, 600))
			pygame.draw.line(self.win, (222, 222, 222), (0, x * 12), (800, x * 12))


	def drawPlatforms(self):
		for p in self.platforms:
			a = random.randint(0, 700)
			self.win.blit(self.platform.image,(p[0], p[1]))
		self.platforms.append([a, self.platforms[-1][1] - 50])



	def updatePlatforms(self):
		for p in self.platforms:
			rect = pygame.Rect(p[0], p[1], self.platform.image.get_width(), self.platform.image.get_height())




	def main(self):
		platform = Platform()
		doodler = Doodler()
		while run:
			# drawGrid()
			self.win.blit(doodler.image, [doodler.x, doodler.y])
			self.drawPlatforms()
			self.updatePlatforms()
			self.sprite_group.draw(self.win)
			doodler.update()
			self.jump(doodler)
			pygame.display.update()

			pygame.time.delay(50)
			self.win.fill((255, 255, 255))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

	pygame.quit()

DoodleJump().main()