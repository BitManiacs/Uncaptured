'''
Title: Config
Description: This file holds all the global variables that can be accessed/read only by other modules.
'''
import pygame
from pygame import *
import json

pygame.init()

DISPLAY_PIXEL_WIDTH = 640
DISPLAY_PIXEL_HEIGHT = 480
DISPLAY_DIMENSION = (DISPLAY_PIXEL_WIDTH, DISPLAY_PIXEL_HEIGHT)

DISPLAY_WIDTH = 20
DISPLAY_HEIGHT = 15

TITLE_BG = "img/TitleScreen2.png"
OPTIONS_BG = "img/OptionsMenu.png"
CONTROLS_BG = "img/ControlsMenu.png"

DIR_KEYS_IMG = "img/dirKeys.png"
WASD_IMG = "img/wasd.png"

MENU_FONT = "fonts/mksanstallx.ttf"
MENU_FONT_SIZE = 30
TITLE_FONT_SIZE = 30
TITLE_FONT_COLOR = (34, 34, 41)
OPTIONS_FONT_COLOR = (255, 255, 255)
SELECTED_OPTIONS_COLOR = (100, 135, 135)
SELECTED_TITLE_COLOR = (194,150,101)

Y_OFFSET = 40

START_GAME_STATE = 0
OPTIONS_STATE1 = 1
EXIT_STATE = 2
TITLE_STATE = -1
STATES = {0:"Game", 1:"Options", 2:"Exit", 3: "Title", 4:"Controls"}

# different json file levels
LVL_TUT = json.loads(open("tiled/tutorial.json").read())

''' TILESETS '''
GROUND_TILESET = []
# loading whole tile set
GTS = pygame.image.load("img/Tiles Set.png")
TUT_GRND_TS = []
TUT_GRND_TS.append(GTS.subsurface(0, 64, 32, 32))
TUT_GRND_TS.append(GTS.subsurface(160, 32, 32, 32))

''' OBJECTS '''
WALLIMG = GTS.subsurface(96, 32, 32, 32)
GOALIMG = GTS.subsurface(32, 64, 32, 32)
PLAYERIMG = pygame.image.load("img/Bulbasaur.png")
BOULDERIMG = pygame.image.load("img/Boulder.png")
GRASSIMG = pygame.image.load("img/Grass.png")
ENEMYIMG = pygame.image.load("img/Rocket.png")
