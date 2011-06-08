#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING ------------------------------------
import pygame

# --- CLASSES ---------------------------------------------
class Bitmap():
    def __init__(self, x, y, imagePath, passedSurface):
        # The position is an array as opposed to tuple so it can be changed.
        self.pos = [int(x),int(y)]
        # Surface to render to
        self.surface = passedSurface
        # Convert the image for use in PyGame
        self.bitmap = pygame.image.load(imagePath).convert()
    
    def update(self, position = None):
        # Position is an optional parameter, used to move Bitmap
        if position == None:
            self.surface.blit(self.bitmap, self.pos)
        else:
            self.surface.blit(self.bitmap, position)
            self.pos = position


# --- FUNCTIONS -------------------------------------------