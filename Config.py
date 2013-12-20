'''
Title: Config
Description: This file holds all the global variables that can be modified
    or accessed by other modules.
'''

SCREEN_PIXEL_WIDTH = 640
SCREEN_PIXEL_HEIGHT = 480
SCREEN_DIMENSION = (SCREEN_PIXEL_WIDTH, SCREEN_PIXEL_HEIGHT)

TITLE_BG = "img/TitleScreen2.png"
OPTIONS_BG = "img/OptionsMenu.png"

OPTIONS_FONT = "fonts/mksanstallx.ttf"
OPTIONS_FONT_SIZE = 30
TITLE_FONT_SIZE = 30
TITLE_FONT_COLOR = (34, 34, 41)
OPTIONS_FONT_COLOR = (255, 255, 255)
SELECTED_OPTIONS_COLOR = (100, 135, 135)
SELECTED_FONT_COLOR = (194,150,101)

START_GAME_STATE = 0
OPTIONS_STATE = 1
EXIT_STATE = 2
TITLE_STATE = -1

