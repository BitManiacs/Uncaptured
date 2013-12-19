import pygame
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

    def draw(self):
        # fill screen with darkness
        self.screen.fill((0,0,0))
        # update the display
        pygame.display.flip()

