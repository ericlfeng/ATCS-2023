from player import Player
import math
import random

class AIPlayer(Player):
    def __init__(self, x, y, target_player, base_speed, screen_width):
        super().__init__(x, y, base_speed)
        self.target_player = target_player
        self.screen_width = screen_width

    def update(self):
        #AI player is updated when everything else is (as it is in a collection of all sprites that gets updated)
        #So this function has to exist (as leaving it in all_sprites makes other things easier)
        return

    def move(self):
        self.pause = False
        #Randomly adjusts speed from +5 to -5
        self.speed += (random.randint(0, 10) - 5)

        #Caps speed from being too fast or too slow
        if self.speed > 10:    
            self.speed -= 5
        elif self.speed < -10:
            self.speed += 5

        #Stops it from going off screen, generally steering to to the middle of the screen
        if self.rect.x >= self.screen_width:
            self.speed = -5
        elif self.rect.x <= 0:
            self.speed = 5
        if self.rect.x > self.screen_width // 3 * 2:
            self.speed -= 1
        elif self.rect.x < self.screen_width // 3:
            self.speed += 1
        
        #Switches images to make it look like its runnning
        if self.image == self.left1:
            self.image = self.right1
        elif self.image == self.right1:
            self.image = self.left1
        
        #Moves by speed
        self.rect.x += self.speed

