###############################################################################
#Pseudo Code layout
###############################################################################
#load tile map

#generate ID
# use a id_counter to make sure each id is unique

#GameEngine Class

# update
# for all the objects in the game call their update function

# draw
# for all the objects in the game call their draw function

# GameObject
# Template object for creating objects
# needs an up

###############################################################################
#Program start
###############################################################################
import pygame
from pygame.locals import *
from Player import Player
#from enemy import Enemy
import collisions
from Maps import Maps
from other_types import Boulder, Grass, Pit, Wall
from TitleScreen import TitleScreen
from options import Options

game_engine = None

#Returns an "unique" ID and increments id_counter
id_counter = 0
clock = pygame.time.Clock()

def generate_id():
    global id_counter
    return_id = str(id_counter)
    id_counter += 1
    return return_id

class GameEngine():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))
        self.typeList = {'player': Player,
                         'grass': Grass,
                         'boulder': Boulder,
                         'pit': Pit,
                         'wall': Wall # wall is not in json file as
                                      # an object
                        } #FILL IN THE BLANKS WITH PLAYER/ENEMY OBJECTS
        self.objectList = {} #TAKES TYPE AND ID
        self.mapfile = Maps("maps/testlevel.json")
        self.tilemap = self.mapfile.get_tilemap()
        for obj in self.mapfile.get_objectlist():
            obj_type,x,y,options = obj
            self.addObject(obj_type,x,y,options)

    def update(self):
        for objType in self.objectList:
            for obj in self.objectList[objType]:
                self.objectList[objType][obj].update()
                if ( objType == 'player'):
                    coll = self.checkByType( self.objectList[objType][obj].getX(),
                      self.objectList[objType][obj].getY(), "boulder" )
                    # wall detection
                    wall = self.checkByType( self.objectList[objType][obj].getX(),
                      self.objectList[objType][obj].getY(), "wall" )
                    if ( len( coll ) != 0 or len( wall ) != 0):
                        self.objectList[objType][obj].moveBack()

    def drawbg(self, screen, mapwall):
        pixelw = 32
        pixelh = 32
        floorRect = ( 0, 0, pixelw, pixelh)
        wallRect = ( 96, 32, pixelw, pixelh)
        wallImg = (self.mapfile.img).subsurface(wallRect)
        floorImg = (self.mapfile.img).subsurface(floorRect)
        tile_table = []
        for tile_x in range(len(mapwall)):
            line = []
            tile_table.append(line)
            for tile_y in range(len(mapwall[0])):
                # fill w/ wall or floor
                if (mapwall[tile_x][tile_y] == 0):
                    line.append(floorImg)
                else:
                    line.append(wallImg)
            # draw on screen
            for x, row in enumerate(tile_table):
                for y, tile in enumerate(row):
                    screen.blit(tile, (x*32, y*32))

    def draw(self):
        self.screen.fill((0,0,0))
        self.drawbg(self.screen, self.tilemap)
        for objType in self.objectList:
            for obj in self.objectList[objType]:
                self.objectList[objType][obj].draw(self.screen)
        pygame.display.flip()
###############################################################################
    def addObject(self,objType, x, y, optionList):
        new_id = generate_id()
        if objType not in self.objectList:
            self.objectList[objType] = {}
        self.objectList[objType][new_id] = self.typeList[objType](x,y,optionList)

    def getObjectList():
        return self.objectList
###############################################################################
    def checkByType(self, x,y,obj_type):
       return_list = []
       for obj in self.objectList[obj_type]:
           if x == self.objectList[obj_type][obj].getX() and y == self.objectList[obj_type][obj].getY():
               return_list.append(obj)
       return return_list

    def getScrn(self):
        return self.screen

def main():
    game_engine = GameEngine()
    titlescrn = TitleScreen()
    optionscrn = Options()
    # game_engine.addObject("player",100,100,{})
    # game_engine = GameEngine()
    title = True
    # title screen
    while (title):
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        titlescrn.update()
        titlescrn.draw(titlescrn.getScrn())
        print "TICK"
        while(titlescrn.getOptions()):
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            optionscrn.update()
            optionscrn.draw(titlescrn.getScrn())
            clock.tick(30)
        if (titlescrn.getStart()):
            title = False
        clock.tick(30)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        game_engine.update()
        game_engine.draw()
        clock.tick(30) # 30 FPS


if __name__ == '__main__': main()

#TESTING GIT FETCH -> MERGE
