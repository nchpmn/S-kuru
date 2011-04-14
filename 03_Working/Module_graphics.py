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
        self.surface = surface

        self.logo = pygame.image.load(imagePath).convert()


    def updateLogo(self):
        screen.blit(self.logo, self.pos) # This line does not work - having problems
                                          # with passing self.surface and accessing
                                          # the actual surface.

class simpleBox():
    def __init__(self, (x,y), width, height, colour, surface):
        self.pos = (x,y)
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(self.pos[0], self.pos[1], self.width, self.height)
        self.colour = colour
        self.surface = surface
    
    def update(self):
        pygame.draw.rect(self.surface, self.colour, self.rect)
        
# --- FUNCTIONS ------------------------------------------
def logoMaker((x,y), imagePath, surface):
    newGraphic = Logo((x,y), imagePath, surface)

    return newGraphic
