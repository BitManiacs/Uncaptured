import pygame
from Config import *
from GameEngine import GameEngine
from TitleScreen import TitleScreen
from pygame.locals import *

''' GLOBAL VARS '''
# need game engine to be changed by states
game_engine = None

def main():
    # make a GameEngine instance
    game_engine = GameEngine()
    # set state to title screen
    game_engine.setState(TitleScreen())
    # continuously update game_engine
    while 1:
        if pygame.event.peek(QUIT):
            return
        # update and draw
        game_engine.update()
        game_engine.draw()
        # set the fps
        game_engine.FPS(30) # 30 FPS

# call main
if __name__ == '__main__': main()
