#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING -----------------------------------
import pygame
import random
import math

pygame.font.init()
powerGrid = pygame.font.Font("01_assets/PowerGrid.ttf", 100)

# --- FUNCTIONS ------------------------------------------


# --- CLASSES --------------------------------------------
class Button():
    def __init__(self, (x,y), text, size, colour):
        self.pos = (x,y)
        self.content = text
        self.size = size
        self.colour = colour

    def updateText(self):
        text = powerGrid.render(self.content, 1, self.colour)
        textPos = text.get_rect(centerx = screen.get_width()/2)
        screen.blit(text, textPos)

        
# --- PROGRAM INIT ---------------------------------------
width = 800
height = 600

screen = pygame.display.set_mode((width, height)) # Create the screen
pygame.display.set_caption("S-kuru") # And give it a title

FPSClock = pygame.time.Clock() # FPS Limiter

running = True # Flag for the game loop

buttons = []

newButton = Button((200,300), "New Level", 125, (64,64,64))
buttons.append(newButton)


# --- GAME LOOP ------------------------------------------
while running == True:
    FPSClock.tick(60)

    screen.fill((92,92,92))

    # Update Everything
    for u in buttons:
        u.updateText()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
