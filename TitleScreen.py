import pygame
from Config import *
from pygame.locals import *

Y_OFFSET = 40
Y_START = SCREEN_PIXEL_HEIGHT/3.0
START_GAME = 0
OPTIONS = 1
EXIT = 2


class TitleScreen():
    def __init__(self):
        # setup display screen
        self.bg = pygame.image.load(TITLE_BG).convert()
        self.bgimg = self.bg.subsurface((0,0, 640, 480))
        self.font = pygame.font.Font(OPTIONS_FONT,TITLE_FONT_SIZE)
        self.optionList = ["Start Game", "Options", "Exit"]
        self.selected = 0
        self.counter = 0

    # called by the gameengine, draws the state of Title Screen
    def draw(self, screen):
        # fill screen with darkness
        screen.fill((0,0,0))
        screen.blit(self.bgimg, (0, 0))
        self.drawText(screen)
        # update the display
        pygame.display.flip()

    def drawText(self, screen):
        y = Y_START
        for index, string in enumerate(self.optionList):
            if (self.selected==index):
                fontColor = SELECTED_FONT_COLOR
            else:
                fontColor = OPTIONS_FONT_COLOR

            text = self.font.render(string, True, fontColor)
            textpos = text.get_rect()
            textpos.centerx = self.bg.get_rect().centerx
            textpos.y = y
            screen.blit(text, textpos)
            y += Y_OFFSET

    def update(self):
        '''
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if (event.key == pygame.K_DOWN):
                    self.selected = (self.selected+1) % len(self.optionList)
                elif (event.key == pygame.K_UP):
                    self.selected = (self.selected-1) % len(self.optionList)
                elif (event.key == pygame.K_RETURN):
                    self.select()'''
                    
        key = pygame.key.get_pressed()
        if (key[K_RETURN]):
            self.select()
        elif (key[K_DOWN] and self.counter >=3):
            self.selected = (self.selected+1) % len(self.optionList)
            self.counter = 0
        elif (key[K_UP] and self.counter >=3):
            self.selected = (self.selected-1) % len(self.optionList)
            self.counter = 0
        self.counter += 1
        return


    def select(self):
        print self.optionList[self.selected]
        selected = self.selected
        if selected == START_GAME:
            print "Start game"
        elif selected == OPTIONS:
            print "Options"
        elif selected == EXIT:
            print "Exit"
            quit = pygame.event.Event(pygame.QUIT,{})
            pygame.event.post(quit)
        return
