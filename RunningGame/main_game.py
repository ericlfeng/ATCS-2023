import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT
from player import Player
from ai_player import AIPlayer
from background import Background

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 10
AI_SPEED = 10
BACKGROUND_SPEED = 2

# Initialize Pygame
pygame.init()

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two-Player Running Game")
clock = pygame.time.Clock()

# Create players and background
player1 = Player((255, 0, 0), WIDTH // 2, HEIGHT // 2, PLAYER_SPEED)
player2 = AIPlayer((0, 0, 255), 200, HEIGHT // 2, player1, AI_SPEED)
background = Background(BACKGROUND_SPEED)

all_sprites = pygame.sprite.Group()
all_sprites.add(background, player1, player2)

# Additional variables for key tapping
key_left_tapped = False
key_right_tapped = False

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT and not key_left_tapped:
                background.move(player1.speed)
                key_left_tapped = True
            elif event.key == K_RIGHT and not key_right_tapped:
                background.move(player1.speed)
                key_right_tapped = True

    # Check for key release
    keys = pygame.key.get_pressed()
    if not keys[K_LEFT]:
        key_left_tapped = False
    if not keys[K_RIGHT]:
        key_right_tapped = False

    # Update game state
    all_sprites.update()

    # Draw background and players
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
