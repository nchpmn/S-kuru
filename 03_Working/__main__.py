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

# --- FUNCTIONS -------------------------------------------
# Update all objects with only one line during the MAINLOOP
def updateObjects(buttons, logo):
    logo.update()
    for b in buttons:
        b.update()
    
    
    
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
menuList = text.menuCreator(menuText, 200, 200, 100, 1, 2, screen)


# --- MAIN LOOP -------------------------------------------
# Loading screen
loadScreen.mainMenu(screen)

while mainRunning:
    mainClock.tick(60)
    
    # Clear the screen each frame
    screen.fill((146,146,146))
    
    # --- Set & Update Objects ---
    updateObjects(menuList, skuruLogo)
    
    # --- Event Catching & Handling ---
    for event in pygame.event.get():
        # Quit PyGame safely upon exit
        if event.type == pygame.QUIT:
            mainRunning = False
        # Make the buttons do actions
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            for button in menuList:
                X = button.getXPos()
                Y = button.getYPos()
                if X[0] < mousePos[0] < X[1] and Y[0] < mousePos[1] < Y [1]:
                    button.doAction(screen)
    
    pygame.display.flip()
    
pygame.quit()
