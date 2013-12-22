import pygame, gc
from pygame.locals import *
from Config import *
import Mod
from TitleScreen import TitleScreen
from OptionsMenu import OptionsMenu
from Interactable import *

class GameEngine():
    def __init__(self):
        # initilialize pygame
        pygame.init()
        # initialize the game clock
        self.clock = pygame.time.Clock()
        # state is the event the game is in
        self.state = None
        self.states = {"Back":[]}
        self.wasd = False
        self.KEY_DOWN = pygame.K_DOWN
        self.KEY_LEFT = pygame.K_LEFT
        self.KEY_RIGHT = pygame.K_RIGHT
        self.KEY_UP = pygame.K_UP
        self.ground = None
        self.objects = None

    # draws the current state of the game to the screen
    def draw(self):
        if ( self.state != None ):
            self.state.draw()

    def update(self):
        if (self.state==None):
            self.state=TitleScreen()
            self.states["Title"] = self.state
            return

        self.state.update()

    # sets the current state of the game
    def setState(self,stateName):
        if stateName == "Back":
            self.state.reset()
            self.state = self.states["Back"].pop()
            return
        if self.states[stateName] != self.state:
            self.states["Back"].append(self.state)
            self.state.reset()
            self.state = self.states[stateName]

    def addState(self,stateName,stateInstance):
        self.states[stateName] = stateInstance

    # controls the framerate of the whole game
    def FPS(self, framerate):
        self.clock.tick(framerate)

    def exit(self):
        quit = pygame.event.Event(pygame.QUIT,{})
        pygame.event.post(quit)


    def getWasd(self):
        return self.wasd

    def setWasd(self, wasd):
        self.wasd = wasd
        if wasd:
            print "YES"
            self.KEY_DOWN = pygame.K_s
            self.KEY_LEFT = pygame.K_a
            self.KEY_RIGHT = pygame.K_d
            self.KEY_UP = pygame.K_w
        else:
            print "NO"
            self.KEY_DOWN = pygame.K_DOWN
            self.KEY_LEFT = pygame.K_LEFT
            self.KEY_RIGHT = pygame.K_RIGHT
            self.KEY_UP = pygame.K_UP

    ''' FOR LEVEL STATES '''
    def initGround(self):
        data = self.state.data
        # populate 2d array with 0's
        ground = [[0 for j in range(DISPLAY_WIDTH)] for i in range(DISPLAY_HEIGHT)]
        w = 0
        h = 0
        # scan the ground data
        for row in ground:
            for x in range(DISPLAY_WIDTH):
                row[x] = data['layers'][0]['data'][w + h]
                w += 1
            h += 1
            w = 0
        # normalize ground with 0 to ...(how many different types)
        ground_types = []
        normalizer = 0
        for row in ground:
            for x in range(DISPLAY_WIDTH):
                tile = ground[row][x]
                if tile not in ground_types:
                    ground_types.append(tile)
                    ground[row][x] = normalizer
                    normalizer += 1
                else:
                    ground[row][x] = ground_types.index(tile)
        # set new normalized ground blueprint
        self.ground = ground

    def initObjects(self):
        data = self.state.data
        # make a dictionary of objs
        obj_dict = {}
        for layer in data['layers']:
            objname = layer['name']
            if 'name' in layer and objname not in obj_dict:
                obj_dict[objname] = []
                for obj in layer['objects']:
                    x = obj['x']
                    y = obj['y']
                    obj_dict[objname].append(Interactable(objname,(x,y)))
        # set reference to object
        self.objects = obj_dict
    ''' END LEVEL STATES '''
