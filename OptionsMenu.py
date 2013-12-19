import pygame, sys
from pygame.locals import *

def Options:
    def __init__(self):
        # setup display screen
        self.bg = pygame.image.load(OPTIONS_BG).convert()
        self.bgimg = self.bg.subsurface((0,0, 640, 480))    

