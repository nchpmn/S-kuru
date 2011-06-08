#!/usr/bin/env python
#encoding: UTF-8

# Import required modules
import yaml
import pygame
import random
import fontRender


# If we're loading the main game and main menu
def mainMenu(screen):
    # YAML.load the list of load items
    f = open('01_assets/loadScreenPhrases.skt', 'r')
    newList = yaml.load(f)
    print newList

    # PyGame Load Loop Flag
    loadLoop = True
    
    # PyGame Loop
    while loadLoop:
        screen.fill((0,0,0))

        # Get out of the loadLoop eventually
        if random.randint(0,3) == 2:
            loadLoop = Fase
        
        
        

# If this module is run directly
if __name__ == '__main__':
    # When run directly, create the PyGame surface and window
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height)) # Create the screen
    pygame.display.set_caption("S-kuru") # And give it a title
    mainMenu()
    raw_input("Finished!")
