import pygame
from Config import *
from TitleScreen import TitleScreen
from pygame.locals import *

class GameEngine():
    def __init__(self):
        # initilialize pygame
        pygame.init()
        # initialize the game clock
        self.clock = pygame.time.Clock()
        # setup display screen
        self.screen = pygame.display.set_mode(SCREEN_DIMENSION)
        # state is the event the game is in
        self.state = None

    # draws the current state of the game to the screen
    def draw(self):
        if ( self.state != None ):
            self.state.draw(self.screen)
            pygame.display.flip()

    # sets the current state of the game
    def setState(self,state):
        self.state = state

    # controls the framerate of the whole game
    def FPS(self, framerate):
        self.clock.tick(framerate)
