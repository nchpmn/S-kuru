#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING -----------------------------------
import pygame
import random
import math
import Module_text # Custom module for handling text functions
import Module_graphics # Module for handling raster graphics

# --- FUNCTIONS ------------------------------------------


# --- CLASSES --------------------------------------------

        
# --- PROGRAM INIT ---------------------------------------
width = 800
height = 600

screen = pygame.display.set_mode((width, height)) # Create the screen
pygame.display.set_caption("S-kuru") # And give it a title

FPSClock = pygame.time.Clock() # FPS Limiter

running = True # Flag for the game loop

# Create the menu buttons
buttonTextList = ["Play Game", "Edit Level", "Quit"]
buttons = Module_text.menuCreator(buttonTextList, 200, 400, 75, 125, (64, 64, 64), screen)

# Show the game logo
newLogo = Module_graphics.

# --- GAME LOOP ------------------------------------------
while running == True:
    FPSClock.tick(60)

    screen.fill((92,92,92))

    # Update Everything
    for u in buttons:
        u.checkOver()
        u.updateText()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
