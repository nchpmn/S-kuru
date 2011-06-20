#!/usr/bin/env python
#encoding: UTF-8

# Import required modules
import pygame
import playGame
import editLevel

# --- INITIALISATION --------------------------------------
pygame.font.init()

# Several 'imports' of PowerGrid required because each size must be separate
fontSize1 = pygame.font.Font("01_assets/PowerGrid.ttf", 125)
fontSize2 = pygame.font.Font("01_assets/PowerGrid.ttf", 100)
fontSize3 = pygame.font.Font("01_assets/PowerGrid.ttf", 55)
fontSize4 = pygame.font.Font("01_assets/PowerGrid.ttf", 45)


# --- CLASSES ---------------------------------------------
class Button():
    def __init__(self, x, y, text, sizeID, colourID, actionID, surface):
        self.pos = [int(x),int(y)]
        self.content = text
        self.size = sizeID
        self.colourID = colourID
        self.originalColourID = colourID
        self.actionID = actionID
        self.surface = surface
    
    # Check for mouseover, change the colour if needed and blit to surface
    def update(self):
        # Next section commented out - mouseOver different colouring. Broken Code!
        
        #mousePos = pygame.mouse.get_pos()
        ## Get the pixel width and height of the text at a specific size
        #textPixels = calculateTextSize(self.size, self.content)
        #
        ## If the mouse is within the block of text
        #if mousePos != None:
        #    if self.pos[0] < mousePos[0] < (self.pos[0] +  textPixels[0]) and self.pos[1] < mousePos[1] < (self.pos[1] + textPixels[1]):
        #        # Set self.colour to a 'mouseOver' colour
        #        self.colourID = 5
        #    elif self.colourID != self.originalColourID:
        #        self.colourID = self.originalColourID
        
        # Render the text to the screen
        text = renderFont(self.size, self.colourID, self.content)
        textPos = self.pos
        self.surface.blit(text, textPos)
    
    def getXPos(self):
        XPosition = [self.pos[0], (self.pos[0] + fontSize1.size(self.content)[0])]
        return XPosition
    
    def getYPos(self):
        YPosition = [self.pos[1], (self.pos[1] + fontSize1.size(self.content)[1])]
        return YPosition
    
    def doAction(self, screen):
        # Global >> Quit S-kuru
        if self.actionID == 0:
            # Unsure how to safely exit PyGame from submodule
            pass
        # MainMenu >> PlayGame
        elif self.actionID == 1:
            playGame.preGame(screen)
        # MainMenu >> EditLevel
        elif self.actionID == 2:
            editLevel.preEdit(screen)
        # PreGameLevel >> Campaign
        elif self.actionID == 3:
            print "CAMPAIGN BUTTON"
            return 0
        # PreGameLevel >> UserLevel
        elif self.actionID == 4:
            print "USERLEVELS BUTTON"
            return 1
        elif self.actionID == 5:
            pass

class StaticText():
    def __init__(self, x, y, content, colourID, sizeID, surface):
        self.pos = [int(x),int(y)]
        self.text = content
        self.colourID = colourID
        self.sizeID = sizeID
        self.surface = surface
    
    def update(self):
        text = renderFont(self.sizeID, self.colourID, self.text)
        textPos = self.pos
        self.surface.blit(text, textPos)

# --- FUNCTIONS -------------------------------------------

# Return an RGB Colour Value based on a colour ID
def textColour(colourID):
    # The colourIDs are as follows:
    # 0 - Black
    # 1 - White
    # 3 - Dark Grey
    # 4 - Medium Grey
    # 5 - Off-White
    colours = [(0,0,0),
               (255,255,255),
               (64,64,64),
               (92,92,92),
               (236,236,236)]
    return colours[colourID]

# Render a font ready for blitting to surface
def renderFont(sizeID, colourID, content):
    if sizeID == 1:
        finalText = fontSize1.render(content, 1, textColour(colourID))
    elif sizeID == 2:
        finalText = fontSize2.render(content, 1, textColour(colourID))
    elif sizeID == 3:
        finalText = fontSize3.render(content, 1, textColour(colourID))
    elif sizeID == 4:
        finalText = fontSize4.render(content, 1, textColour(colourID))
    
    return finalText

# Return the pixel height and width of a block of text
def calculateTextSize(sizeID, content):
    if sizeID == 1:
        pixelSize = fontSize1.size(content)
    elif sizeID == 2:
        pixelSize = fontSize2.size(content)
    elif sizeID == 3:
        pixelSize = fontSize3.size(content)
    elif sizeID == 4:
        pixelSize = fontSize4.size(content)
    return pixelSize

# Create a menu with specific spacing from a list of strings
def menuCreator(menuTextList, menuX, menuY, menuSpacer, sizeID, colourID, surface):
    n = 0
    menu = []
    for menuItem in menuTextList:
        # MenuItem is a two-element array, of a string - content - and an integer - actionID
        newButton = Button(menuX, (menuY + (menuSpacer * n)), menuItem[0], sizeID, colourID, menuItem[1], surface)
        menu.append(newButton)
        n += 1

    return menu

def updateDynamicText(x, y, content, sizeID, colourID, surface):
    safeContent = str(content)
    text = renderFont(sizeID, colourID, safeContent)
    textPos = (int(x), int(y))
    surface.blit(text, textPos)