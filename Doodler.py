import pygame



class Doodler(pygame.sprite.Sprite):
    jumpCount = 10
    x = 600
    y = 600
    isJump = False
    speed = 25  # скорость дудлера по горизонтали
    def __init__(self):
        super(Doodler, self).__init__()
        self.image = pygame.image.load('static/dog_right.png')
        self.rect = self.image.get_rect()
        self.jump = 0
        self.gravity = 0
        self.cameray = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
            self.image = pygame.image.load('static/dog_left.png')
        if keys[pygame.K_RIGHT] and self.x < 600:
            self.x += self.speed
            self.image = pygame.image.load('static/dog_right.png')

        if not self.jump:
            self.y += self.gravity
            self.gravity +=1
        elif self.jump:
            self.y -= self.jump
            self.jump -= 1
        if self.y - self.cameray <= 200:
            self.cameray -= 10
