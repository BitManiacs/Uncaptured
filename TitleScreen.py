import pygame
from pygame.locals import *
    
class TitleScreen():
    def __init__(self):
        # setup display screen
        self.bg = pygame.image.load("img/TitleScreen2.png").convert()
        self.bgimg = self.bg.subsurface((0,0, 640, 480))    

    def draw(self, screen):
        # fill screen with darkness
        screen.fill((0,0,0))
        screen.blit(self.bgimg, (0, 0))
        # update the display
        pygame.display.flip()

