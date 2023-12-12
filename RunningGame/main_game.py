




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
    #500 is best for race accuracy, and so that one has to pace
    #But 100 is best to not get bored
    RACE_LENGTH = 100
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
        #Get start time
        self.start_time = time.time()
        while running:
            # Set fps to 120
            self.dt += self.clock.tick(120)

            #End condition
            if self.player1.distance >= self.RACE_LENGTH:
                #Different messages depending on outcome of race
                if self.player1.rect.x > self.player2.rect.x:
                    win_message = "You Win!"
                elif self.player1.rect.x < self.player2.rect.x:
                    self.text_color = (255, 0, 0)
                    win_message = "The AI Wins..."
                else:
                    win_message = "Tie"
                
                #Displays end message
                self.text = self.font.render(win_message, True, self.text_color) 
                self.textRect = self.text.get_rect()
                self.textRect.center = (self.WIDTH // 2, self.HEIGHT // 4)
                self.screen.blit(self.text, self.textRect)
                pygame.display.flip()
                pygame.time.wait(3000)
                #exits game loop
                break
            # Handle closing the window
            for event in pygame.event.get():
                #Checks if the keys are pressed
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == KEYDOWN:                        
                    if event.key == K_LEFT:
                        #Passes key into FSM
                        self.player1.update("left")
                        #For counting number of times keys are pressed in a certain amount of time (to change speed)
                        self.player1.lastsecond += 1
                        self.key_left_tapped = True
                    elif event.key == K_RIGHT:
                        self.player1.update("right")
                        self.player1.lastsecond += 1
                        self.key_right_tapped = True
            
            # Check for key release
            #Makes sure holding a key doesn't cause an error or the character to fall
            keys = pygame.key.get_pressed()
            if not keys[K_LEFT]:
                self.key_left_tapped = False
            if not keys[K_RIGHT]:
                self.key_right_tapped = False

            #Moves the players every interval, updates their speed
            self.current_time = time.time() - self.start_time
            #Every time more than self.current_second has passes
            if(self.current_time//self.SPEED_UPDATE_RATE != self.current_second):
                #Move both players
                self.player1.move()
                self.player2.move()
                self.current_second = self.current_time//self.SPEED_UPDATE_RATE
                #Number of times the arrow keys were pressed in the last 5 seconds
                self.player1.fivesectotal.append(self.player1.lastsecond)
                self.player1.lastsecond = 0
                #Keeps the length of the list to 5 for more dynamic speed changes
                if len(self.player1.fivesectotal) >= 5:
                    self.player1.fivesectotal.pop(0)
            #Updates speed
            self.player1.update_speed(self.SPEED_UPDATE_RATE)
            
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            #Displays countdown
            if self.RACE_LENGTH - self.player1.distance > 0:
                self.text = self.font.render('Distance Left: ' + str(self.RACE_LENGTH - self.player1.distance), True, self.text_color) 
                self.textRect = self.text.get_rect()
                self.textRect.center = (self.WIDTH // 2, self.HEIGHT // 3)
                self.screen.blit(self.text, self.textRect)

            # Update display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(self.FPS)
            #If the player has fallen, wait a bit, then update image
            if self.player1.pause == True:
                pygame.time.wait(300)
                self.player1.image = self.player1.fall2
                self.all_sprites.update()
                self.all_sprites.draw(self.screen)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    #This instance of the game
    pm = main_game()
    pm.run()
