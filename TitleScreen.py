import pygame
from Config import *
from pygame.locals import *

Y_OFFSET = 40
Y_START = SCREEN_PIXEL_HEIGHT/3.0

class TitleScreen():
    def __init__(self):
        # setup display screen
        self.bg = pygame.image.load(TITLE_BG).convert()
        self.bgimg = self.bg.subsurface((0,0, 640, 480))
        self.font = pygame.font.Font(OPTIONS_FONT,TITLE_FONT_SIZE)
        self.optionList = ["Start Game", "Options", "Exit"]

    # called by the gameengine, draws the state of Title Screen
    def draw(self, screen):
        # fill screen with darkness
        screen.fill((0,0,0))
        screen.blit(self.bgimg, (0, 0))
        self.drawText(screen)
        # update the display
        pygame.display.flip()

    def drawText(self, screen):
        y = Y_START
        for string in self.optionList:
            text = self.font.render(string, True, OPTIONS_FONT_COLOR)
            textpos = text.get_rect()
            textpos.centerx = self.bg.get_rect().centerx
            textpos.y = y
            screen.blit(text, textpos)
            y += Y_OFFSET
