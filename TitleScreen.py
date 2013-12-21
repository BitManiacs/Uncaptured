import pygame
from Config import *
import Mod
from pygame.locals import *
from GameState import GameState
from Display import Display

Y_OFFSET = 40
Y_START = DISPLAY_PIXEL_HEIGHT/3.0


class TitleScreen():
    def __init__(self):
        # setup TitleScreen
        self.bg = pygame.image.load(TITLE_BG).convert()
        self.bgimg = self.bg.subsurface((0,0, 640, 480))
        self.font = pygame.font.Font(OPTIONS_FONT,TITLE_FONT_SIZE)
        self.optionList = ["Start Game", "Options", "Exit"]
        self.rects = [None] * len(self.optionList)
        self.selected = 0
        self.counter = 0
        # have a Game Engine
        self.game_engine = Mod.GAME_ENGINE
        # have a Game display
        self.game_display = Mod.GAME_DISPLAY


    # called by the gameengine, draws the state of Title Screen
    def draw(self):
        # fill display with darkness
        self.game_display.display.fill((0,0,0))
        self.game_display.display.blit(self.bgimg, (0, 0))
        self.drawText()
        # update the display
        self.game_display.updateDisplay()


    def drawText(self):
        y = Y_START
        for index, string in enumerate(self.optionList):
            if (self.selected==index):
                fontColor = SELECTED_FONT_COLOR
            else:
                fontColor = TITLE_FONT_COLOR

            text = self.font.render(string, True, fontColor)
            textpos = text.get_rect()
            textpos.centerx = self.bg.get_rect().centerx
            textpos.y = y
            self.rects[index] = self.game_display.display.blit(text, textpos)
            y += Y_OFFSET


    def update(self):
        ret = TITLE_STATE

        event = pygame.event.poll()
        if(event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_RETURN):
                ret = self.select()
                return ret
        if(event.type == pygame.MOUSEMOTION):
             hover = Rect(event.pos, (0, 0)).collidelist(self.rects)
             if hover > -1:
                 self.selected = hover
                 self.hover = True
                 return ret
             else:
                 self.hover = False
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
        if selected == START_GAME_STATE:
            print "Start game"
            return 0
        elif selected == OPTIONS_STATE:
            print "Options"
            return OPTIONS_STATE
        elif selected == EXIT_STATE:
            print "Exit"
            return EXIT_STATE

    def setActive(self, active):
        self.active = active

