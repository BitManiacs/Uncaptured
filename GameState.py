import pygame
from Config import *


### ILL MAKE INHERITANCE LATER
class GameState():
    def __init__(self):
        # set the GameState's display
        self.game_display = GAME_DISPLAY
        # this state has a game engine
        self.game_engine = GAME_ENGINE

