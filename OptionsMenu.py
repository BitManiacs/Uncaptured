import pygame, sys
from Config import *
import Mod
from pygame.locals import *


Y_OFFSET = 40
Y_START = DISPLAY_PIXEL_HEIGHT/4.0
X_START = DISPLAY_PIXEL_WIDTH/3.5
BACK = 0
OPTIONS = 1
BACK = 2


class OptionsMenu:
    def __init__(self):
        # setup display screen
        self.bg = pygame.image.load(OPTIONS_BG).convert()
        self.bgimg = self.bg.subsurface((0,0, 640, 480))
        self.font = pygame.font.Font(OPTIONS_FONT,OPTIONS_FONT_SIZE)
        self.optionList = ["Controls", "Filler", "Back"]
        self.rects = [None] * len(self.optionList)
        self.selected = 0
        self.counter = 0
        # have a Game Engine
        self.game_engine = Mod.GAME_ENGINE
        # have a Game display
        self.game_display = Mod.GAME_DISPLAY
        self.hover = False


    # called by the gameengine, draws the state of Title Screen
    def draw(self):
        # fill screen with darkness
        self.game_display.display.fill((0,0,0))
        self.game_display.display.blit(self.bgimg, (0, 0))
        self.drawText()
        # update the display
        self.game_display.updateDisplay()

    def drawText(self):
        y = Y_START
        x = X_START
        for index, string in enumerate(self.optionList):
            if (self.selected==index):
                fontColor = SELECTED_OPTIONS_COLOR
            else:
                fontColor = OPTIONS_FONT_COLOR

            text = self.font.render(string, True, fontColor)
            textpos = text.get_rect()
            textpos.centerx = X_START
            textpos.y = y
            self.rects[index] = self.game_display.display.blit(text, textpos)
            y += Y_OFFSET

    def update(self):
        ret = OPTIONS_STATE

        hover = Rect(pygame.mouse.get_pos(), (0, 0)).collidelist(self.rects)
        if hover > -1:
            self.selected = hover
            self.hover = True
        else:
             self.hover = False

        event = pygame.event.poll()
        if(event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_RETURN):
                ret = self.select()
                return ret
        elif(event.type == pygame.MOUSEBUTTONUP and self.hover):
            return self.select()

        if self.counter >= 3:
            self.counter = 0

            key = pygame.key.get_pressed()
            if (key[K_DOWN]):
                self.selected = (self.selected+1) % len(self.optionList)
            elif (key[K_UP]):
                self.selected = (self.selected-1) % len(self.optionList)
        self.counter += 1
        return ret


    def select(self):
        selected = self.selected
        if selected == len(self.optionList)-1:
            print "Back"
            return -1
        return OPTIONS_STATE
