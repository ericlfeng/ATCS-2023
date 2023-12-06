




import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT
from player import Player
from ai_player import AIPlayer
from background import Background

class main_game:
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    PLAYER_SPEED = 10
    AI_SPEED = 10
    BACKGROUND_SPEED = 2
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.ghost_timer = 8000

        # Initialize Pygame screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Two-Player Running Game")
        self.clock = pygame.time.Clock()

        # Create players and background
        self.player1 = Player((255, 0, 0), self.WIDTH // 2, self.HEIGHT // 2, self.PLAYER_SPEED)
        self.player2 = AIPlayer((0, 0, 255), 200, self.HEIGHT // 2, self.player1, self.AI_SPEED)
        self.background = Background(self.BACKGROUND_SPEED)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.background, self.player1, self.player2)

        # Additional variables for key tapping
        key_left_tapped = False
        key_right_tapped = False


    def run(self):
        # Main Game Loop
        running = True
        while running:
            # Set fps to 120
            self.dt += self.clock.tick(120)

            # Handle closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.player1.update("left")
                        #TODO:Need work here
                        self.player1.draw()
                    elif event.key == K_RIGHT:
                        self.player1.update("right")


                    # if event.key == K_LEFT and not key_left_tapped:
                    #     self.background.move(self.player1.speed)
                    #     key_left_tapped = True
                    # elif event.key == K_RIGHT and not key_right_tapped:
                    #     self.background.move(self.player1.speed)
                    #     key_right_tapped = True
            
            # Check for key release
            keys = pygame.key.get_pressed()
            if not keys[K_LEFT]:
                key_left_tapped = False
            if not keys[K_RIGHT]:
                key_right_tapped = False


            # Only update every 120 fps
            # if self.dt > 120:
            # self.dt = 0
            self.all_sprites.update()

            # Draw to the screen
            self.screen.fill((255, 255, 255))
            self.all_sprites.draw(self.screen)

            # Update display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(self.FPS)

        # Quit the game
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pm = main_game()
    pm.run()
