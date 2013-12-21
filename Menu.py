import pygame
from Config import *
import Mod
from pygame.locals import *
from GameState import GameState
from Display import Display
from abc import ABCMeta, abstractmethod

class Menu(object):
    def __init__(self, stateID, centerX, y, fontColor, selectedColor):
        # setup display screen
        self.font = pygame.font.Font(MENU_FONT,MENU_FONT_SIZE)
        self.fontColor = fontColor
        self.selectedColor = selectedColor
        
        self.stateID = stateID

        self.centerX = centerX
        self.y = y

        self.selected = 0
        self.counter = 0
        self.hover = False

        # have a Game Engine
        self.game_engine = Mod.GAME_ENGINE
        # have a Game display
        self.game_display = Mod.GAME_DISPLAY

    def setList(self, list):
    # called by the gameengine, draws the state of Title Screen
        self.optionList = list
        self.rects = [None] * len(list)

    def setBG(self, bg):
        self.bg = pygame.image.load(bg).convert()
        self.bgimg = self.bg.subsurface((0,0, self.game_display.getWidth()
                                , self.game_display.getHeight()))

    def setCoords(self, centerX, y):
        self.centerX = centerX
        self.y = y

    def draw(self):
        # fill screen with darkness
        self.game_display.display.fill((0,0,0))
        self.game_display.display.blit(self.bgimg, (0, 0))
        self.drawText()
        # update the display

    def drawText(self):
        x = self.centerX
        y = self.y
        for index, string in enumerate(self.optionList):
            if (self.selected==index):
                fontColor = self.selectedColor
            else:
                fontColor = self.fontColor

            text = self.font.render(string, True, fontColor)
            textpos = text.get_rect()
            textpos.centerx = x
            textpos.y = y
            self.rects[index] = self.game_display.display.blit(text, textpos)
            y += Y_OFFSET

    def update(self):
        ret = self.stateID

        hover = Rect(pygame.mouse.get_pos(), (0, 0)).collidelist(self.rects)
        if hover > -1:
            self.hover = True
        else:
            self.hover = False

        event = pygame.event.poll()
        if(event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_RETURN):
                return self.select()

        elif(event.type == pygame.MOUSEMOTION and self.hover):
            self.selected = hover
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
        print self.optionList[self.selected]
        return self.stateID
