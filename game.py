import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Doodle Jump")
run = True


class Character:
	width = 10
	height = 5
	jumpCount = 10
	x = 100
	y = 400
	isJump = False
	speed = 5;


class Platform:
	start = 0
	end = 0

	def __init__(self, start, end):
		self.start = start
		self.end = end
		pygame.draw.line(win, (255, 255, 255), start, end, 3)


def jump():
	chr.isJump = True
	if (chr.jumpCount >= -10):
		if (chr.jumpCount < 0):
			chr.y += int(chr.jumpCount ** 2 / 3)
		else:
			chr.y -= int(chr.jumpCount ** 2 / 3)
		chr.jumpCount -= 1
	else:
		chr.isJump = False
		chr.jumpCount = 10


chr = Character()
while (run):
	platform = Platform(300, 400)
	keys = pygame.key.get_pressed()
	if (keys[pygame.K_LEFT]):
		chr.x -= chr.speed
	if (keys[pygame.K_RIGHT]):
		chr.x += chr.speed
	win.fill((0, 0, 0))
	pygame.draw.circle(win, (0, 0, 255), (chr.x, chr.y), chr.width, chr.height)
	jump()
	pygame.display.update()
	pygame.time.delay(50)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

pygame.quit()
