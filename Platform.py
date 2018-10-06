import pygame

import Doodler


class Platform(pygame.sprite.Sprite):
    start = (0, 0)
    end = (0, 0)
    doodler = 9
    image = 0;

    def __init__(self):
        super(Platform, self).__init__()
        self.image = pygame.image.load('static/platform.png')
        self.rect = self.image.get_rect()
