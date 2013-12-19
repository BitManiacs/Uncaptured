import pygame
from pygame.locals import *

''' GLOBAL VARS '''
SCREEN_PIXEL_WIDTH = 640
SCREEN_PIXEL_HEIGHT = 480
SCREEN_DIMENSION = (SCREEN_PIXEL_WIDTH, SCREEN_PIXEL_HEIGHT)
clock = pygame.time.Clock()
#game_engine = None #maybe dont need this

class GameEngine():
    def __init__(self):
        # initilialize pygame
        pygame.init()
        # setup display screen
        self.screen = pygame.display.set_mode(SCREEN_DIMENSION)

    def draw(self):
        # fill screen with darkness
        self.screen.fill((0,0,0))
        # update the display
        pygame.display.flip()

def main():
    # make a GameEngine instance
    game_engine = GameEngine()
    # continuously update game_engine
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        # update and draw
        #game_engine.update()
        #game_engine.draw()
        # set the fps
        clock.tick(30) # 30 FPS

# call main
if __name__ == '__main__': main()
