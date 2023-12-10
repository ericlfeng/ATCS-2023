from player import Player
import math
import random

class AIPlayer(Player):
    def __init__(self, x, y, target_player, base_speed, screen_width):
        super().__init__(x, y, base_speed)
        self.target_player = target_player
        self.screen_width = screen_width

    def update(self):
        # distance = self.target_player.rect.x - self.rect.x
        # self.speed += math.log(abs(distance) +1) * 0.01
        # self.rect.x += self.speed
        return

    def move(self):
        self.pause = False
        self.speed += (random.randint(0, 10) - 5)
        if self.speed > 10:    
            self.speed -= 5
        elif self.speed < -10:
            self.speed += 5
        
        if self.rect.x >= self.screen_width:
            self.speed = -5
        elif self.rect.x <= 0:
            self.speed = 5

        if self.rect.x > self.screen_width // 3 * 2:
            self.speed -= 1
        elif self.rect.x < self.screen_width // 3:
            self.speed += 1
        
        if self.image == self.left1:
            self.image = self.right1
        elif self.image == self.right1:
            self.image = self.left1

        self.rect.x += self.speed

