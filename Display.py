import pygame
from Config import *

class Display():
    def __init__(self):
        # set display's dimension
        self.dimension = DISPLAY_DIMENSION
        # setup display
        self.display = None
        self.setupDisplay()

    # setup new display, or update dimension
    def setupDisplay(self):
        # returns a surface
        self.display = pygame.display.set_mode(self.dimension)

    # set new dimension
    def setDimension(self, (width, height)):
        self.dimension = (width, height)

    # update display
    def updateDisplay(self):
        pygame.display.flip()

    def getWidth(self):
        return self.dimension[0]

    def getHeight(self):
        return self.dimension[1]




