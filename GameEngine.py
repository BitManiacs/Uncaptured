import pygame
from Config import *
from TitleScreen import TitleScreen
from pygame.locals import *

class GameEngine():
    def __init__(self):
        # initilialize pygame
        pygame.init()
        # setup display screen
        self.screen = pygame.display.set_mode(SCREEN_DIMENSION)
        self.bg = pygame.image.load("img/TitleScreen2.png").convert()
        self.bgimg = self.bg.subsurface((0,0, 640, 480))
        # state is the event the game is in
        self.state = None

    def draw(self):
        if ( self.state != None ):
            self.state.draw(self.screen)
            pygame.display.flip()

    def setState(self,state):
        self.state = state
