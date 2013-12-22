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
        self.controlsList = ["Directional Arrows", "Back"]
        self.setList(self.controlsList)
        self.dirKeysImg = pygame.image.load(DIR_KEYS_IMG)
        self.wasdImg = pygame.image.load(WASD_IMG)

    def draw(self):
        if (self.game_engine.getWasd()):
            img = self.wasdImg
            self.controlsList[0] = "WASD Keys"
        else:
            img = self.dirKeysImg
            self.controlsList[0] = "Directional Arrows"

        self.setList(self.controlsList)
        
        Menu.draw(self)

        x = X_START
        y = Y_START
        titleFont = pygame.font.Font(MENU_FONT, MENU_FONT_SIZE)
        titleFont.set_underline(True)
        text = titleFont.render("Movement", True, OPTIONS_FONT_COLOR)
        textpos = text.get_rect()
        textpos.centerx = x
        textpos.y = y - Y_OFFSET
            
        x = DISPLAY_PIXEL_HEIGHT/2.0
        y = Y_START 
        
        self.game_display.display.blit(img, (x,y))
        self.game_display.display.blit(text, textpos)


    def select(self):
        selected = self.optionList[self.selected]
        if selected == "Directional Arrows":
            self.game_engine.setWasd(True)
        elif selected == "WASD Keys":
            self.game_engine.setWasd(False)
        self.game_engine.setState(selected)
