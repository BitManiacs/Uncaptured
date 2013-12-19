import pygame, sys
from pygame.locals import *

class Options:
    def __init__(self):
        pygame.init() # initialize pygame modules
        self.screen = pygame.display.set_mode((640, 480))
        self.start = False # start game check
        self.bg = pygame.image.load("img/TitleScreen.png").convert()
        self.bgimg = self.bg.subsurface((0,0, 640, 480))
        self.cursorimg = pygame.image.load("img/TitleCursor.png")
        self.cursorxy = [224, 288] # postion of start option
        self.text_to_screen(self.screen, "Option 1", 320, 240 )

    def draw(self, screen):
        self.screen.fill((0,0,0))
        screen.blit(self.bgimg, (0, 0))
        #screen.blit(self.label, (100, 100))
        screen.blit(self.cursorimg, (self.cursorxy[0], self.cursorxy[1]))
        self.text_to_screen(self.screen, "Option 1", 100, 100 )
        pygame.display.flip()
        return

    def text_to_screen(self, screen, text, x, y, size = 20,
            color = (255, 255, 255), font_type = 'mksanstallx.ttf'):

        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))


    def update(self):
        key = pygame.key.get_pressed()
        return

    def getScrn(self):
        return self.screen
