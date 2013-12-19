import pygame
from Config import *
from GameEngine import GameEngine
from TitleScreen import TitleScreen
from pygame.locals import *

''' GLOBAL VARS '''

clock = pygame.time.Clock()
# need game engine to be changed by states
game_engine = None

def main():
    # make a GameEngine instance
    game_engine = GameEngine()
    # set state to title screen
    game_engine.setState(TitleScreen())
    # continuously update game_engine
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        # update and draw
        #game_engine.update()
        game_engine.draw()
        # set the fps
        clock.tick(30) # 30 FPS

# call main
if __name__ == '__main__': main()
