import pygame

class Screen():
    def __init__(self):
        # set display's dimension
        self.dimension = SCREEN_DIMENSION
        # setup display screen
        self.display = None
        setupDisplay()

    # setup new display, or update dimension
    def setupDisplay(self):
        self.display = pygame.display.set_mode(self.dimension)

    # set new dimension
    def setDimension(self, (width, height)):
        self.dimension = (width, height)

