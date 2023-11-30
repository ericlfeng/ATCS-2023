import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((800, 600))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.bg_image = pygame.image.load("background.jpg")  # Replace with your background image
        self.bg_x = 0
        self.speed = speed

    def update(self):
        #self.bg_x -= self.speed
        if self.bg_x <= -self.bg_image.get_width():
            self.bg_x = 0

        self.image.blit(self.bg_image, (self.bg_x, 0))
        self.image.blit(self.bg_image, (self.bg_x + self.bg_image.get_width(), 0))
    
    def move(self, amount):
        self.bg_x -= amount
        if self.bg_x <= -self.bg_image.get_width():
            self.bg_x = 0

        self.image.blit(self.bg_image, (self.bg_x, 0))
        self.image.blit(self.bg_image, (self.bg_x + self.bg_image.get_width(), 0))