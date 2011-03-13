#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING -----------------------------------
import pygame
import random
import math
import Module_text # Custom module for handling text functions
import Module_graphics # Module for handling raster graphics
import playGame # Play the game!

# --- FUNCTIONS ------------------------------------------
def updateLogo(newLogo):
    screen.blit(newLogo.logo, newLogo.pos)

# --- CLASSES --------------------------------------------


# --- PROGRAM INIT ---------------------------------------
width = 800
height = 600
screen = pygame.display.set_mode((width, height)) # Create the screen
pygame.display.set_caption("S-kuru") # And give it a title

FPSClock = pygame.time.Clock() # FPS Limiter

running = True # Flag for the game loop

# Create the menu buttons
buttonTextList = ["Play Game", "Edit Level", "Quit"] # Items in the menu

# Follows this pattern: (Menu Items, menuX, menuY, menuSpacer, size, colour, surface)
buttons = Module_text.menuCreator(buttonTextList, 275, 200, 85, 125, (100,100,100), screen)

# Show the game logo
newLogo = Module_graphics.Logo((200,0), "01_assets/logo.jpg", screen)

# --- GAME LOOP ------------------------------------------
while running == True:
    FPSClock.tick(60)

    screen.fill((146,146,146))

    # Update Everything
    for u in buttons:
        u.checkOver()
        u.updateText()

    updateLogo(newLogo)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mousePos = pygame.mouse.get_pos()
            for item in buttons:
                X = item.getXPos()
                Y = item.getYPos()
                if X[0] < mousePos[0] < X[1] and Y[0] < mousePos[1] < Y [1]:
                    item.mouseOver()
                else:
                    item.notMouseOver()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            for item in buttons:
                X = item.getXPos()
                Y = item.getYPos()
                if X[0] < mousePos[0] < X[1] and Y[0] < mousePos[1] < Y [1]:
                    item.action(screen)
                    

    pygame.display.flip()

pygame.quit()
