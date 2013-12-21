import pygame, sys
from Config import *
import Mod
from pygame.locals import *
from Menu import Menu

Y_OFFSET = 40
Y_START = DISPLAY_PIXEL_HEIGHT/3.0
X_START = DISPLAY_PIXEL_WIDTH/5.0

class ControlsMenu(Menu):
    def __init__(self):
        Menu.__init__(self, OPTIONS_STATE1, X_START, Y_START, 
                                    OPTIONS_FONT_COLOR, SELECTED_OPTIONS_COLOR)
        # setup TitleScreen
        self.setBG(CONTROLS_BG) 
        optionsList = ["Directional Arrows", "WASD"]
        self.setList(optionsList+["Back"])

    def draw(self):
        Menu.draw(self)

        x = X_START
        y = Y_START
        text = self.font.render("Movement", True, OPTIONS_FONT_COLOR)
        textpos = text.get_rect()
        textpos.centerx = x
        textpos.y = y - Y_OFFSET
        self.game_display.display.blit(text, textpos)


    def select(self):
        selected = self.selected
        print self.optionList[self.selected]
        self.game_engine.setState(self.optionList[self.selected])
