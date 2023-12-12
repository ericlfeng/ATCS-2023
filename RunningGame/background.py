import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        #Creates background with image, centers and scales it
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.bg_image = pygame.image.load("pixel_game_track_background.jpeg")
        self.bg_x = 0
        self.bg_image = pygame.transform.scale(self.bg_image, (width, height))

    def update(self):
        if self.bg_x <= -self.bg_image.get_width():
            self.bg_x = 0

        self.image.blit(self.bg_image, (self.bg_x, 0))
