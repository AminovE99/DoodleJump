import pygame


class Doodler(pygame.sprite.Sprite):
    jumpCount = 10
    x = 600
    y = 600
    isJump = False
    speed = 25 #скорость дудлера по горизонтали
    image = 0

    def __init__(self):
        super(Doodler, self).__init__()
        self.image = pygame.image.load('static/dog_right.png')
        image = self.image
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.image = pygame.image.load('static/dog_left.png')
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.image = pygame.image.load('static/dog_right.png')
