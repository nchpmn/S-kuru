#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING -----------------------------------
import pygame
import random
import playGame

pygame.font.init()
powerGrid = pygame.font.Font("01_assets/PowerGrid.ttf", 100)

# --- CLASSES --------------------------------------------
class Button():
    def __init__(self, (x,y), text, size, colour, surface, action):
        self.pos = (x,y)
        self.content = text
        self.size = size
        self.colour = colour
        self.surface = surface
        self.actionNumb = action

    def checkOver(self):
        mousePos = pygame.mouse.get_pos()
    
    def getXPos(self):
        XPosition = [self.pos[0], (self.pos[0] + powerGrid.size(self.content)[0])]
        return XPosition
    
    def getYPos(self):
        YPosition = [self.pos[1], (self.pos[1] + powerGrid.size(self.content)[1])]
        return YPosition
    
    def action(self, passedSurface):
        if self.actionNumb == 1:
            playGame.Play(passedSurface)
        
    def updateText(self):
        text = powerGrid.render(self.content, 1, self.colour)
        textPos = self.pos
        self.surface.blit(text, textPos)

# --- FUNCTIONS ------------------------------------------
def menuCreator(menuTextList, menuX, menuY, menuSpacer, size, colour, surface):
    n = 0
    menu = []
    for item in menuTextList:
        newButton = Button((menuX, (menuY + (menuSpacer * n))), item, size, colour, surface, (n+1))
        menu.append(newButton)
        n += 1

    return menu
