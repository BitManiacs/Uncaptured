import pygame, sys
from Config import *
import Mod
from pygame.locals import *
from Menu import Menu
from ControlsMenu import ControlsMenu

Y_OFFSET = 40
Y_START = DISPLAY_PIXEL_HEIGHT/4.0
X_START = DISPLAY_PIXEL_WIDTH/3.5

class OptionsMenu(Menu):
    def __init__(self):
        Menu.__init__(self, OPTIONS_STATE1, X_START, Y_START, 
                                    OPTIONS_FONT_COLOR, SELECTED_OPTIONS_COLOR)
        # setup TitleScreen
        self.setBG(OPTIONS_BG)
        optionsList = ["Controls", "Filler"]
        self.setList(optionsList + ["Back"])
        self.game_engine.addState("Controls", ControlsMenu() )

    def select(self):
        selected = self.selected
        print self.optionList[self.selected]
        self.game_engine.setState(self.optionList[self.selected])
