import pygame
from pygame.sprite import collide_rect

from doodler import Doodler
from flying_platform import Platform
import random


class DoodleJump:
    pygame.init()
    pygame.display.set_caption("Doodle Jump")
    platforms = []  # координаты платформ

    def __init__(self):
        self.window = pygame.display.set_mode((700, 700))
        self.platforms = [[550, 680, 0, 0]]  # spritecollide and groupcollide
        # self.sprite_group = pygame.sprite.Group()  # не надо?
        self.platform = pygame.image.load("static/platform_mini.png")
        self.doodler = Doodler()
        self.curr_level = 50
        self.run = True

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

    def draw_platforms(self):
        for platform in self.platforms:
            self.window.blit(self.platform,
                             (platform[0], platform[1] - self.doodler.cameray))

        self.platforms.append([random.randint(0, 700),
                               self.platforms[-1][1] - 120,
                               0,
                               0])

        if self.platforms[1][1] - self.doodler.cameray > 900:
            self.platforms.pop(0)

    def update_platforms(self):
        player = pygame.Rect(self.doodler.x,
                             self.doodler.y,
                             self.doodler.image.get_width(),
                             self.doodler.image.get_height() - 10)

        for platform in self.platforms:
            rect = pygame.Rect(platform[0], platform[1],
                               self.platform.get_width(),
                               self.platform.get_height())

            if rect.colliderect(player) \
                    and self.doodler.gravity \
                    and self.doodler.y < platform[1] - self.doodler.cameray:

                if platform[2] != 2:
                    self.doodler.jump = 15
                    self.doodler.gravity = 0
                else:
                    platform[-1] = 1

            if platform[2] == 1:
                if platform[-1] == 1:
                    platform[0] += 5

                    if platform[0] > 550:
                        platform[-1] = 0

                else:
                    platform[0] -= 5
                    if platform[0] <= 0:
                        platform[-1] = 1

    def main(self):
        platform = Platform()

        while self.run:
            # drawGrid()
            self.draw_platforms()
            self.update_platforms()
            self.window.blit(self.doodler.image, [self.doodler.x, self.doodler.y - self.doodler.cameray])
            # self.sprite_group.draw(self.win)
            self.doodler.update()
            # self.playerX = self.doodler.x  # не должно находиться в main
            # self.jump()
            pygame.display.update()
            pygame.time.delay(30)
            self.window.fill((0, 220, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

    pygame.quit()


DoodleJump().main()
