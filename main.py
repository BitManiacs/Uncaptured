import pygame

''' GLOBAL VARS '''

#game_engine = None #maybe dont need this

def main():
    # intlialize the game engine
    #game_engine = makeGameEngine()

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
