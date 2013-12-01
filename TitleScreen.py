import pygame, sys
from pygame.locals import *

class TitleScreen:

    def __init__(self):
        pygame.init() # initialize pygame modules
        self.screen = pygame.display.set_mode((640, 480))
        self.start = False # start game check
        self.bg = pygame.image.load("img/TitleScreen.png").convert()
        self.bgimg = self.bg.subsurface((0,0, 640, 480))
        self.select = pygame.image.load("img/TitleStart.png"), \
                pygame.image.load("img/TitleOptions.png")
        # self.selectimg = self.select[0].subsurface(0, 0, 128, 32), \
          #      self.select[1].subsurface(0, 0, 160, 32)
        self.cursorimg = pygame.image.load("img/TitleCursor.png")
        self.cursorxy = [224, 288] # postion of start option

    def startGame(self):
        self.start = True
        return

    def getStart(self):
        return self.start

    def update(self):
        key = pygame.key.get_pressed()
        if (key[K_RETURN] and self.cursorxy[1] == 288):
            print "START GAME"
            self.startGame()
        elif (key[K_DOWN]):
            self.cursormove("down")
        elif (key[K_UP]):
            self.cursormove("up")
        return

    def draw(self, screen):
        self.screen.fill((0,0,0))
        # bg
        screen.blit(self.bgimg, (0, 0))
        # Start
        screen.blit(self.select[0], (256, 288))
        # Options
        screen.blit(self.select[1], (256, 320))
        # Cursor
        screen.blit(self.cursorimg, (self.cursorxy[0], self.cursorxy[1]))
        pygame.display.flip()
        return

    def cursormove(self, direction):
        if (direction == "up" and
                self.cursorxy[1] == 320):
            self.cursorxy[1] = 288
        elif (direction == "down" and
                self.cursorxy[1] == 288):
            self.cursorxy[1] = 320
        return

    def getScrn(self):
        return self.screen


