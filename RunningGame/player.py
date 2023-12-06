import pygame
from FSM import FSM

class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y, speed):
        super().__init__()

        self.speed = speed
        self.right1 = pygame.image.load("right1.png")
        self.right2 = pygame.image.load("right2.png")
        self.left1 = pygame.image.load("left1.png")
        self.left2 = pygame.image.load("left2.png")
        self.fall1 = pygame.image.load("fall1.png")
        self.fall2 = pygame.image.load("fall2.png")
        self.fall3 = pygame.image.load("fall3.png")
        self.state = self.right1
        self.image = self.right1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clock = pygame.time.Clock()
        self.dt = 0

        self.fsm = FSM("right")
        self.init_fsm()


    def init_fsm(self):
        self.fsm.add_transition("right", "right", self.fall, "fall")
        self.fsm.add_transition("right", "left", self.left, "left")
        self.fsm.add_transition("left", "right", self.right, "right")
        self.fsm.add_transition("left", "left", self.fall, "fall")

        self.fsm.add_transition("right", "fall", self.right, "right")
        self.fsm.add_transition("left", "fall", self.left, "left")

        self.fsm.add_transition(None, "left", None, "left")
        self.fsm.add_transition(None, "right", None, "right")
        self.fsm.add_transition(None, "fall", None, "fall")

        #self.fsm.add_transition("end", "right", None, "end")
        #self.fsm.add_transition("end", "left", None, "end")

        #self.fsm.add_transition(None, "STOP", None, None)
    
    def left(self):
        self.image = self.left1
    def right(self):
        self.image = self.right1
    def fall(self):
        self.image = self.fall1
        pygame.time.wait(1000)
        
    def update(self, input=None):
        #Use the finite state machine to process input
        self.fsm.process(input) 
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))
