import pygame, sys
from pygame.locals import *

class Options:
    def __init__(self):
        pygame.init() # initialize pygame modules
        self.screen = pygame.display.set_mode((640, 480))
        self.start = False # start game check
        self.bg = pygame.image.load("img/TitleScreen.png").convert()
        self.bgimg = self.bg.subsurface((0,0, 640, 480))
        self.myfont = pygame.font.SysFont("monospace", 15)
        self.label = self.myfont.render("Some text!", 1, (255,255,0))
        self.cursorimg = pygame.image.load("img/TitleCursor.png")
        self.cursorxy = [224, 288] # postion of start option

    def draw(self, screen):
        self.screen.fill((0,0,0))
        screen.blit(self.bgimg, (0, 0))
        screen.blit(self.label, (100, 100))
        screen.blit(self.cursorimg, (self.cursorxy[0], self.cursorxy[1]))
        pygame.display.flip()
        return

    def update(self):
        key = pygame.key.get_pressed()
        return

    def getScrn(self):
        return self.screen
