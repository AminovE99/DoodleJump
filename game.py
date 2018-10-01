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
        self.platforms = [[400, 500]]
        self.sprite_group = pygame.sprite.Group()  # не надо?
        self.platform = pygame.image.load("static/platform_mini.png").convert_alpha()
        self.player = pygame.image.load("static/dog_right.png")
        self.playerX = 600  # Связать с классом Doodler
        self.playerY = 600

    # это в класс Дудлер
    def jump(self, doodler):
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
        # if
        for p in self.platforms:
            a = random.randint(0, 700)
            self.win.blit(self.platform, (p[0], p[1]))
        self.platforms.append([a, self.platforms[-1][1] - 50])

    def updatePlatforms(self):
        for p in self.platforms:
            rect = pygame.Rect(p[0], p[1], self.platform.get_width(), self.platform.get_height())
            player = pygame.Rect(self.playerX, self.playerY, self.player.get_width() - 10,
                                 self.player.get_height())
            print(player.colliderect(rect))

    def main(self):
        platform = Platform()
        doodler = Doodler()
        while (self.run):
            # drawGrid()
            self.drawPlatforms()
            self.updatePlatforms()
            self.win.blit(doodler.image, [doodler.x, doodler.y])
            self.sprite_group.draw(self.win)
            doodler.update()
            self.jump(doodler)
            pygame.display.update()
            pygame.time.delay(50)
            self.win.fill((0, 220, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

    pygame.quit()


DoodleJump().main()
