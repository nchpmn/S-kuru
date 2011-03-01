#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING -----------------------------------
import pygame
import random

# --- CLASSES --------------------------------------------
class Logo():
    def __init__(self, (x,y), imagePath, surface):
        self.pos = (x,y)
        self.path = imagePath
        self.surface= surface

        self.logo = pygame.image.load(imagePath).convert()


    def updateLogo(self):
        screen.blit(self.logo, self.pos) # This line does not work - having problems
                                          # with passing self.surface and accessing
                                          # the actual surface.
        
# --- FUNCTIONS ------------------------------------------
def logoMaker((x,y), imagePath, surface):
    newGraphic = Logo((x,y), imagePath, surface)

    return newGraphic
