#!/usr/bin/env python
#encoding: UTF-8

# --- IMPORT MODULES --------------------------------------
import pygame
import yaml
import text

# --- CLASSES ---------------------------------------------

# --- FUNCTIONS -------------------------------------------
def preGame(screen):
    # Three things to do:
    #   1. get player profile
    #   2. pick level type & level
    #   3. load level
    playerProfile(screen)
    levelChoose(screen)
    
def playerProfile(screen):
    pass

def levelChoose(screen):
    levelMText = [["Campaign", 3], ["Custom", 4]]
    levelMenu = text.menuCreator(levelMText, 200, 300, 100, 1, 2, screen)
    
    levelMenuRunning = True
    levelMenuClock = pygame.time.Clock()
    
    menuHeader = text.StaticText(100, 25, "Select Level Type:", 2, 1, screen)
    
    while levelMenuRunning:
        levelMenuClock.tick(60)
        
        screen.fill((146,146,146))
        
        # --- Update Objects
        for button in levelMenu:
            button.update()
        menuHeader.update()
        
        # --- Event Catching & Handling ---
        for event in pygame.event.get():
            # Quit PyGame safely upon exit
            if event.type == pygame.QUIT:
                levelMenuRunning = False
            # Make the buttons do actions
            if event.type == pygame.MOUSEBUTTONUP:
                mousePos = pygame.mouse.get_pos()
                for button in levelMenu:
                    X = button.getXPos()
                    Y = button.getYPos()
                    if X[0] < mousePos[0] < X[1] and Y[0] < mousePos[1] < Y [1]:
                        button.doAction(screen)
        
        pygame.display.flip()