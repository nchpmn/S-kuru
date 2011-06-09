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
import loadScreen
import graphics
import text

# --- INITIALISATION --------------------------------------
# Create the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height)) 
# And give it a title
pygame.display.set_caption("S-kuru") 

# Clock to limit the FPS in menu
mainClock = pygame.time.Clock() 

# Flag for the mainRunning loop
mainRunning = True

# --- Create Objects ---
# Logo Bitmap
skuruLogo = graphics.Bitmap(150, 75, '01_assets/menuLogo.jpg', screen)

# Menu Items
menuText = [["Play", 1],
            ["Editor", 2],
            ["Quit", 0]]


# --- MAIN LOOP -------------------------------------------
# Loading screen
loadScreen.mainMenu(screen)

while mainRunning:
    mainClock.tick(60)
    
    # Clear the screen each frame
    screen.fill((146,146,146))
    
    # --- Set & Update Objects ---
    skuruLogo.update()
    
    pygame.display.flip()
    
pygame.quit()
