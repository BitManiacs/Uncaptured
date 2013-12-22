import pygame

class Interactable():
    # @obj_type: the type of the interactable
    def __init__(self, obj_type, (x, y)):
        self.obj_type = obj_type
        # initalize position (x, y)
        self.pos = (x, y)

    # to set the position
    def setPos(self, (x, y)):
        self.pos = (x, y)


