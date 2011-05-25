#!/usr/bin/env python
#encoding: UTF-8

# S-kuru is the brainchild of Nathan Chapman
# of Australia. Want to get in contact? Try
# job.nchapman+sakuru@gmail.com

# There is a GitHub repository of this
# project at the following URL:
# https://github.com/Crashdown/S-kuru

# --- MODULE IMPORTING ------------------------------------
import pygame
import random
import sys
sys.path.append("_00_modules")
import loadScreen

# --- INITIALISATION --------------------------------------
width = 800
height = 600
screen = pygame.display.set_mode((width, height)) # Create the screen
pygame.display.set_caption("S-kuru") # And give it a title

mainClock = pygame.time.Clock() # Clock to limit the FPS

mainRunning = True # Flag for the game loop

# --- MAIN LOOP -------------------------------------------
while mainRunning:
    loadScreen.main(screen)
        
pygame.quit()
