import pygame
from FSM import FSM
from background import Background
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()

        #Player images
        self.right1 = pygame.image.load("right1.png")
        self.right2 = pygame.image.load("right2.png")
        self.left1 = pygame.image.load("left1.png")
        self.left2 = pygame.image.load("left2.png")
        self.fall1 = pygame.image.load("fall1.png")
        self.fall2 = pygame.image.load("fall2.png")
        self.fall3 = pygame.image.load("fall3.png")
        

        self.speed = speed
        self.image = self.right1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pause = False
        self.distance = 0
        self.lastsecond = 0
        self.fivesectotal = []
        self.counter = 0

        self.clock = pygame.time.Clock()
        self.dt = 0

        #Starting state = right foot forwards
        self.fsm = FSM("right")
        self.init_fsm()


    def init_fsm(self):
        #Adding FSM transitions
        self.fsm.add_transition("right", "right", self.fall, "fall")
        self.fsm.add_transition("right", "left", self.right, "right")
        self.fsm.add_transition("left", "right", self.left, "left")
        self.fsm.add_transition("left", "left", self.fall, "fall")

        self.fsm.add_transition("right", "fall", self.right, "right")
        self.fsm.add_transition("left", "fall", self.left, "left")

        self.fsm.add_transition(None, "left", None, "left")
        self.fsm.add_transition(None, "right", None, "right")
        self.fsm.add_transition(None, "fall", None, "fall")

    #Left step
    def left(self):
        self.image = self.left1
        self.pause = False
        self.distance += 1
        self.lastsecond += 1
    #Right step
    def right(self):
        self.image = self.right1
        self.pause = False
        self.distance += 1
        self.lastsecond += 1
    #Players falls
    def fall(self):
        self.image = self.fall1
        self.pause = True
        
    def update(self, input=None):
        #Use the finite state machine to process input
        #Logic for pausing player, making them unable to keep running, if they have tripped
        if self.pause == True and input != None:
            self.image = self.fall2
            self.speed = -15
            self.counter += 1
            if self.counter >= 20:
                self.fsm.process(input)
                self.counter = 0
                self.pause = False
            return
        self.fsm.process(input) 
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))

    def update_speed(self, SPEED_UPDATE_RATE):
        average = sum(self.fivesectotal)/5
        #Change the location based on speed of clicking
        #Average is extimated to be between 20 and 10 divided by SPEED_UPDATE_RATE
        #Log scale, so that super fast and super slow don't have too much of an impact on the game,
        #but there are faster speed changes near 15 cps
        #Math is adjusted to not have domain errors
        normalized_average = average/SPEED_UPDATE_RATE - 15
        self.speed = abs(normalized_average) / normalized_average * 30 * math.log10(abs(normalized_average) +1)

    #Moves player by speed
    def move(self):
        self.rect.x += self.speed
        


