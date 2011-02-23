#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING -----------------------------------
import pygame
import random

# --- CLASSES --------------------------------------------
class Logo(self):
    def __init__(self, (x,y), imagePath, surface):
        self.pos = (x,y)
        self.path = imagePath
        self.surface = surface

        logo = pygame.image.load(imagePath).convert()


    def updateLogo(self):
        pygame.blit(logo, surface)

# --- FUNCTIONS ------------------------------------------
def 
