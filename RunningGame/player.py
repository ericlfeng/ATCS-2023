import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        # Move the player (arrow-controlled) based on speed
        pass  # You can add animation logic here if needed
