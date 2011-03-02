#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING -----------------------------------
import pygame
import random

pygame.font.init()
powerGrid = pygame.font.Font("01_assets/PowerGrid.ttf", 100)

# --- CLASSES --------------------------------------------
class Button():
    def __init__(self, (x,y), text, size, colour, surface):
        self.pos = (x,y)
        self.content = text
        self.size = size
        self.colour = colour
        self.surface = surface

    def checkOver(self):
        mousePos = pygame.mouse.get_pos()
    
    def getXPos(self):
        XPosition = [self.pos[0], (self.pos[0] + powerGrid.size(self.content)[0])]
        return XPosition
    
    def getYPos(self):
        YPosition = [self.pos[1], (self.pos[1] + powerGrid.size(self.content)[1])]
        return YPosition
        
    def updateText(self):
        text = powerGrid.render(self.content, 1, self.colour)
        textPos = self.pos
        self.surface.blit(text, textPos)

# --- FUNCTIONS ------------------------------------------
def menuCreator(menuTextList, menuX, menuY, menuSpacer, size, colour, surface):
    n = 0
    menu = []
    for item in menuTextList:
        newButton = Button((menuX, (menuY + (menuSpacer * n))), item, size, colour, surface)
        menu.append(newButton)
        n += 1

    return menu
