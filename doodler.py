import pygame


class Doodler(pygame.sprite.Sprite):
    jumpCount = 10
    x = 600
    y = 600
    isJump = False
    speed = 25  # скорость дудлера по горизонтали

    def __init__(self):
        super(Doodler, self).__init__()
        self.image = pygame.image.load('static/corgi-small-left-new-eyes.png')
        self.rect = self.image.get_rect()
        self.jump = 5
        self.gravity = 0
        self.cameray = 0
        self.delta = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
            self.image = pygame.image.load('static/corgi-small-right-new-eyes.png')
        if keys[pygame.K_RIGHT] and self.x < 600:
            self.x += self.speed
            self.image = pygame.image.load('static/corgi-small-left-new-eyes.png')

        if not self.jump:
            self.y += self.gravity
            self.gravity +=1
        elif self.jump:
            self.y -= self.jump
            self.jump -= 1
        print('self.cameray: %s' % self.cameray)
        print('self.y: %s' % self.y)
        if self.y - self.cameray < 200:
            self.cameray -= 10
        delta = self.y-self.cameray
