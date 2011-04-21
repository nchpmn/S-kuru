#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING -----------------------------------
import pygame
import random
import playGame

pygame.font.init()
# Several 'imports' of PowerGrid required because each size must be separate
menuFont = pygame.font.Font("01_assets/PowerGrid.ttf", 125)
hintFont = pygame.font.Font("01_assets/PowerGrid.ttf", 45)
levelFont = pygame.font.Font("01_assets/PowerGrid.ttf", 100)
goalFont = pygame.font.Font("01_assets/PowerGrid.ttf", 30)

# --- CLASSES --------------------------------------------
class Button():
    def __init__(self, (x,y), text, size, colour, surface, action):
        self.pos = (x,y)
        self.content = text
        self.size = size
        self.originalColour = colour
        self.colour = colour
        self.colour2 = (180,180,180)
        self.surface = surface
        self.actionNumb = action

    def checkOver(self):
        mousePos = pygame.mouse.get_pos()
    
    def getXPos(self):
        XPosition = [self.pos[0], (self.pos[0] + menuFont.size(self.content)[0])]
        return XPosition
    
    def getYPos(self):
        YPosition = [self.pos[1], (self.pos[1] + menuFont.size(self.content)[1])]
        return YPosition
    
    def mouseOver(self):
        self.colour = self.colour2
    
    def notMouseOver(self):
        self.colour = self.originalColour
        
    def action(self, passedSurface):
        if self.actionNumb == 1:
            playGame.Play(passedSurface)
        elif self.actionNumb == 2:
            pass
        elif self.actionNumb == 3:
            running = False
            pygame.quit()
        
    def updateText(self):
        text = menuFont.render(self.content, 1, self.colour)
        textPos = self.pos
        self.surface.blit(text, textPos)

class basicText():
    """This is for text that does not have an action; i.e. static text"""
    def __init__(self, (x,y), text, textType, surface):
        self.pos = (x,y)
        self.content = text
        self.ID = textType
        self.colour = setTextColour(textType)      
        self.surface = surface
    
    def updateText(self):
        if self.ID == 2:
            text = levelFont.render(self.content, 1, self.colour)
        elif self.ID == 3:
            text = goalFont.render(self.content, 1, self.colour)
        elif self.ID == 4:
            text = hintFont.render(self.content, 1, self.colour)
        elif self.ID == 1:
            text = menuFont.render(self.content, 1, self.colour)
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

def updateWelcomeText(surface):
    welcome = basicText((300,400), "Welcome to the Game!", 3, surface)
    welcome.updateText()

def calculateSize(content, sizeID):
    if sizeID == 1:
        size = menuFont.size(content)
    elif sizeID == 2:
        size = levelFont.size(content) 
    elif sizeID == 3:
        size = hintFont.size(content)
    elif sizeID == 4:
        size = goalFont.size(content)
    
    return size

def setTextColour(textID):
    if textID == 1: # Menu
        colour = (225,0,0)
    elif textID == 2: # Level
        colour = (0,225,0)
    elif textID == 3: # Goal
        colour = (0,0,225)
    elif textID == 4: # Hint
        colour = (225,0,225)
    return colour
            
def updateDynamic(content, textID, pos, passedSurface):
    if textID == 2:
        text = levelFont.render(str(content), 1, setTextColour(textID))
    elif textID == 3:
        text = goalFont.render(str(content), 1, setTextColour(textID))
    elif textID == 4:
        text = hintFont.render(str(content), 1, setTextColour(textID))
    elif textID == 1:
        text = menuFont.render(str(content), 1, setTextColour(textID))
    textPos = pos
    passedSurface.blit(text, textPos)