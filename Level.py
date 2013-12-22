import pygam
from pygame.locals import *

class Level():
    # @level: has to be a loaded json file.
    def __init__(self,level):
        # level has reference to data
        self.data = level
