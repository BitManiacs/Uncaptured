import pygame, gc
from Config import *
import Mod
from TitleScreen import TitleScreen
from OptionsMenu import OptionsMenu
from pygame.locals import *

class GameEngine():
    def __init__(self):
        # initilialize pygame
        pygame.init()
        # initialize the game clock
        self.clock = pygame.time.Clock()
        # state is the event the game is in
        self.state = None
        self.states = {}

    # draws the current state of the game to the screen
    def draw(self):
        if ( self.state != None ):
            self.state.draw()

    def update(self):
        if (self.state==None):
            self.state=TitleScreen()
            self.states["Title"] = self.state
            return 

        self.state.update()

    # sets the current state of the game
    def setState(self,stateName):
        prev = self.state
        self.state = self.states[stateName]
        self.states["Back"] = prev

    def addState(self,stateName,stateInstance):
        self.states[stateName] = stateInstance

    # controls the framerate of the whole game
    def FPS(self, framerate):
        self.clock.tick(framerate)

    def exit(self):
        quit = pygame.event.Event(pygame.QUIT,{})
        pygame.event.post(quit)
