import pygame
from TitleScreen import TitleScreen
from pygame.locals import *

SCREEN_PIXEL_WIDTH = 640
SCREEN_PIXEL_HEIGHT = 480
SCREEN_DIMENSION = (SCREEN_PIXEL_WIDTH, SCREEN_PIXEL_HEIGHT)

class GameEngine():
    def __init__(self):
        # initilialize pygame
        pygame.init()
        # setup display screen
        self.screen = pygame.display.set_mode(SCREEN_DIMENSION)
        self.bg = pygame.image.load("img/TitleScreen2.png").convert()
        self.bgimg = self.bg.subsurface((0,0, 640, 480))
        self.state = None

    def draw(self):
        self.state.draw()
        pygame.display.flip()

    def setState(self,state):
        self.state = state

    def getScreen(self):
        return self.screen

