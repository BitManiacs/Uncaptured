import pygame
from pygame.locals import *
import Mod
from Config import *
from Interactable import *

class Level():
    # @level: has to be a loaded json file.
    def __init__(self,level):
        # level has reference to data
        self.data = level
        # set game_engine
        self.game_engine = Mod.GAME_ENGINE
        # add the ground blueprint and objects into engine
        self.ground = None
        self.objects = None
        self.initGround()
        self.initObjects()
        # set view
        self.game_display = Mod.GAME_DISPLAY

    # updates game_engine (model)
    def update(self):
        return None

    # updates display
    def draw(self):
        self.drawGround()
        self.drawObjects()

    # draw the ground
    def drawGround(self):
        ground = self.game_engine.ground
        for y, row in enumerate(ground):
            for x, tile in enumerate(row):
                self.game_display.display.blit(TUT_GRND_TS[tile], (x*32, y*32))


    # draw all the objects
    def drawObjects(self):
        objects = self.game_engine.objects
        objectimg = None
        for name in objects:
            if name == 'Wall':
                objectimg = WALLIMG
            elif name == 'Goal':
                objectimg = GOALIMG
            elif name == 'Player':
                objectimg = PLAYERIMG
            elif name == 'Boulder':
                objectimg = BOULDERIMG
            elif name == 'Grass':
                objectimg = GRASSIMG
            elif name == 'Enemy':
                objectimg = ENEMYIMG
            for interactable in objects[name]:
                self.game_display.display.blit(objectimg, interactable.getPos())

    def initGround(self):
        jsondata = self.data
        # populate 2d array with 0's
        ground = [[0 for j in range(DISPLAY_WIDTH)] for i in range(DISPLAY_HEIGHT)]
        w = 0
        h = 0
        # scan the ground data
        for row in ground:
            for x in range(DISPLAY_WIDTH):
                row[x] = jsondata['layers'][0]['data'][w]
                print row[x], #LOGGING
                w += 1
            print "\n" # LOGGING
        # normalize ground with 0 to ...(how many different types)
        ground_types = []
        normalizer = 0
        for row in ground:
            for x in range(DISPLAY_WIDTH):
                tile = row[x]
                if tile not in ground_types:
                    ground_types.append(tile)
                    row[x] = normalizer
                    normalizer += 1
                else:
                    row[x] = ground_types.index(tile)
        # set new normalized ground blueprint
        self.ground = ground
        self.game_engine.ground = ground

    def initObjects(self):
        jsondata = self.data
        # make a dictionary of objs
        obj_dict = {}
        for layer in jsondata['layers']:
            objname = layer['name']
            print "\n", objname, "\n" #LOGGING
            if 'name' in layer and objname != 'Ground' and objname not in obj_dict:
                obj_dict[objname] = []
                for obj in layer['objects']:
                    x = obj['x']
                    y = obj['y']
                    obj_dict[objname].append(Interactable(objname,(x,y)))
                    print x, y #LOGGING
        # set reference to object
        self.objects = obj_dict
        self.game_engine.objects = obj_dict
