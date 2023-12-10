




import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT
from player import Player
from ai_player import AIPlayer
from background import Background
import time

class main_game:
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    PLAYER_SPEED = 10
    AI_SPEED = 0
    BACKGROUND_SPEED = 2
    RACE_LENGTH = 1000
    SPEED_UPDATE_RATE = 0.1

    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.clock = pygame.time.Clock()
        self.dt = 0

        # Initialize Pygame screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Two-Player Running Game")
        self.clock = pygame.time.Clock()

        # Create players and background
        self.player1 = Player(self.WIDTH // 2, self.HEIGHT // 2, self.PLAYER_SPEED)
        self.player2 = AIPlayer(self.WIDTH // 2, self.HEIGHT // 3 * 2, self.player1, self.AI_SPEED, self.HEIGHT)
        self.background = Background(self.WIDTH, self.HEIGHT)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.background, self.player1, self.player2)

        # Additional variables for key tapping
        self.key_left_tapped = False
        self.key_right_tapped = False
        self.current_second = 0

        self.text_color = (0, 255, 0)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        

    def run(self):
        # Main Game Loop
        running = True
        self.start_time = time.time()
        while running:
            # Set fps to 120
            self.dt += self.clock.tick(120)
            if self.player1.distance >= self.RACE_LENGTH:
                running = False
            # Handle closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == KEYDOWN:                        
                        #TODO:Need work here
                    if event.key == K_LEFT:
                        self.player1.update("left")
                        self.player1.lastsecond += 1
                        #self.background.move(10)
                        # self.key_left_tapped = True
                    elif event.key == K_RIGHT:
                        self.player1.update("right")
                        self.player1.lastsecond += 1
                        #self.background.move(10)
                        # self.key_right_tapped = True
            
            # Check for key release
            #keys = pygame.key.get_pressed()
            # if not keys[K_LEFT]:
            #     self.key_left_tapped = False
            # if not keys[K_RIGHT]:
            #     self.key_right_tapped = False


            # Only update every 120 fps
            # if self.dt > 120:
            #     self.dt = 0
            #print(self.clock.get_rawtime())
            self.current_time = time.time() - self.start_time
            if(self.current_time//self.SPEED_UPDATE_RATE != self.current_second):
                self.player1.move()
                self.player2.move()
                self.current_second = self.current_time//self.SPEED_UPDATE_RATE
                self.player1.fivesectotal.append(self.player1.lastsecond)
                self.player1.lastsecond = 0
                if len(self.player1.fivesectotal) >= 5:
                    self.player1.fivesectotal.pop(0)
            self.player1.update_speed(self.SPEED_UPDATE_RATE)
            
            self.all_sprites.update()
            

            
            # Draw to the screen
            #self.screen.fill((255, 255, 255))
            self.all_sprites.draw(self.screen)

            #Countdown
            self.text = self.font.render('Distance Left: ' + str(self.RACE_LENGTH - self.player1.distance), True, self.text_color) 
            self.textRect = self.text.get_rect()
            self.textRect.center = (self.WIDTH // 2, self.HEIGHT // 3)
            self.screen.blit(self.text, self.textRect)

            # Update display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(self.FPS)
            if self.player1.pause == True:
                pygame.time.wait(300)
                self.player1.image = self.player1.fall2
                self.all_sprites.update()
                self.all_sprites.draw(self.screen)


        print("Game Over")
        if self.player1.rect.x > self.player2.rect.x:
            print("You Win!")
        elif self.player1.rect.x < self.player2.rect.x:
            print("The AI Wins...")
        else:
            print("Tie")
        # Quit the game
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pm = main_game()
    pm.run()
