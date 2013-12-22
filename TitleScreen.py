import pygame
from Config import *
import Mod
from pygame.locals import *
from GameState import GameState
from Display import Display
from Menu import Menu
from OptionsMenu import OptionsMenu

Y_START = DISPLAY_PIXEL_HEIGHT/3.0
X_START = DISPLAY_PIXEL_WIDTH/2.0   


class TitleScreen(Menu):
    def __init__(self):
        Menu.__init__(self, TITLE_STATE, X_START, Y_START, TITLE_FONT_COLOR, SELECTED_TITLE_COLOR)
        # setup TitleScreen
        self.setBG(TITLE_BG)
        self.setList(["Start Game", "Options", "Exit"])
        self.game_engine.addState("Options", OptionsMenu())

    def select(self):
        selected = self.selected
        print self.optionList[self.selected]
        if selected == len(self.optionList)-1:
            self.game_engine.exit()
        self.game_engine.setState(self.optionList[self.selected])
        

