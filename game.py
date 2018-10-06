import pygame
from pygame.sprite import collide_rect

from Doodler import Doodler
from Platform import Platform
import random


class DoodleJump:
    pygame.init()
    pygame.display.set_caption("Doodle Jump")
    platforms = []  # координаты платформ

    def __init__(self):
        self.win = pygame.display.set_mode((700, 700))
        self.run = True
        self.platforms = [[400, 700, 0, 0]]  # spritecollide and groupcollide
        self.sprite_group = pygame.sprite.Group()  # не надо?
        self.platform = pygame.image.load("static/platform_mini.png")
        self.player = pygame.image.load("static/dog_right.png")
        self.playerX = 600  # Связать с классом Doodler
        self.playerY = 600
        self.doodler = Doodler()
        self.minY = 0

    # это в класс Дудлер
    # def jump(self):
    #     self.doodler.isJump = True
    #     if self.doodler.jumpCount >= -10:
    #         if self.doodler.jumpCount < 0:
    #             self.doodler.y += int(self.doodler.jumpCount ** 2 / 2)
    #
    #         else:
    #             self.doodler.y -= int(self.doodler.jumpCount ** 2 / 2)
    #         self.doodler.jumpCount -= 1
    #     else:
    #         self.doodler.isJump = False
    #         self.doodler.jumpCount = 10

    def drawPlatforms(self):
        # if
        for p in self.platforms:
            a = random.randint(0, 700)
            self.win.blit(self.platform, (p[0], p[1]))
        self.platforms.append([a, self.platforms[-1][1] - 50, 0, 0])
        check = self.platforms[1][1] - self.doodler.cameray
        if check > 600:
            self.platforms.pop(0)
            self.platforms.append([random.randint(0, 700), self.platforms[-1][1] - 50, 0, 0])
            self.win.blit(self.platform, (p[0], p[1] - self.doodler.cameray))

    def updatePlatforms(self):
        player = pygame.Rect(self.doodler.x, self.doodler.y, self.player.get_width(), self.player.get_height() - 10)
        for p in self.platforms:
            rect = pygame.Rect(p[0], p[1], self.platform.get_width(), self.platform.get_height())
            if rect.colliderect(player) and self.doodler.gravity and self.doodler.y < p[1] - self.doodler.cameray:
                if p[2] != 2:
                    self.doodler.jump = 15
                    self.doodler.gravity = 0
                else:
                    p[-1] = 1
            if p[2] == 1:
                if p[-1] == 1:
                    p[0] += 5
                    if p[0] > 550:
                        p[-1] = 0
                else:
                    p[0] -= 5
                    if p[0] <= 0:
                        p[-1] = 1

    def main(self):
        platform = Platform()
        while (self.run):
            # drawGrid()
            self.drawPlatforms()
            self.updatePlatforms()
            self.win.blit(self.doodler.image, [self.doodler.x, self.doodler.y])
            # self.sprite_group.draw(self.win)
            self.doodler.update()
            self.playerX = self.doodler.x  # не должно находиться в main
            # self.jump()
            pygame.display.update()
            pygame.time.delay(25)
            self.win.fill((0, 220, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

    pygame.quit()


DoodleJump().main()
