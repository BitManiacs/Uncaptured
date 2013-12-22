import pygame
from pygame.locals import *
import Mod

class Level():
    # @level: has to be a loaded json file.
    def __init__(self,level):
        # level has reference to data
        self.data = level
        # set game_engine
        self.game_engine = Mod.GAME_ENGINE
        # add the ground blueprint and objects into engine
        self.game_engine.initGround()
        self.game_engine.initObjects()
        # set view
        self.game_display = Mod.GAME_DISPLAY

    # updates game_engine (model)
    def update(self):
        return None

    # updates display
    def draw(self):
        return None

    def drawGround(self):
        return None

    def drawObjects(self):
        return None
