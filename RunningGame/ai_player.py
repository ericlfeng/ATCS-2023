from player import Player

class AIPlayer(Player):
    def __init__(self, color, x, y, target_player, speed):
        super().__init__(color, x, y, speed)
        self.target_player = target_player

    def update(self):
        distance = self.target_player.rect.x - self.rect.x
        if distance > 0:
            self.rect.x += min(self.target_player.speed, distance)
        elif distance < 0:
            self.rect.x -= min(self.target_player.speed, abs(distance))
