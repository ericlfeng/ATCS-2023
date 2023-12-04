from player import Player
import math

class AIPlayer(Player):
    def __init__(self, color, x, y, target_player, base_speed):
        super().__init__(color, x, y, base_speed)
        self.target_player = target_player

    def update(self):
        distance = self.target_player.rect.x - self.rect.x
        # if distance > 0:
        #     self.speed -= 0.1
        # elif distance > 1:
        #     self.speed -= 0.1
        # elif distance < 0:
        #     self.speed += 0.1
        # elif distance < 0:
        #     self.speed += 0.1
        self.speed += math.log(abs(distance)) * -0.01
        self.rect.x -= self.speed

    def init_fsm(self):
        self.fsm.add_transition(" ", "SOUTH", self.move_south, "SOUTH")
        self.fsm.add_transition(" ", "EAST", self.move_east, "EAST")
        self.fsm.add_transition(" ", "NORTH", self.move_north, "NORTH")
        self.fsm.add_transition(" ", "WEST", self.move_west, "WEST")

        self.fsm.add_transition("$", "SOUTH", self.move_south, "STOP")
        self.fsm.add_transition("$", "EAST", self.move_east, "STOP")
        self.fsm.add_transition("$", "NORTH", self.move_north, "STOP")
        self.fsm.add_transition("$", "WEST", self.move_west, "STOP")

        self.fsm.add_transition(None, "STOP", None, None)

    def move(self, speed):
        self.rect.x += self.speed

