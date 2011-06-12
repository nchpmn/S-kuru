#!/usr/bin/env python
#encoding: UTF-8

# Import required modules
import yaml
import pygame
import random
import time
import text

# If we're loading the main game and main menu
def mainMenu(screen):
    """Load the game from first run"""
    
    # YAML.load the list of load items
    f = open("01_assets/loadScreen.skt", 'r')
    newList = yaml.load(f)
    
    # PyGame Load Loop Flag
    loadLoop = True
    
    # List for phrases we've already used
    usedPhraseIndex = []
    # List of class objects
    renderText = []
    
    # Make the screen black to begin
    screen.fill((0,0,0))
    
    # PyGame Loop
    while loadLoop and len(usedPhraseIndex) != len(newList):

        # Get out of the loadLoop eventually
        if random.randint(0,4) == 2:
            loadLoop = False
        
        # Show a random number of messages each time
        for i in range(0,random.randint(1,3)):
            
            # If we've already used every message
            if len(usedPhraseIndex) == len(newList):
                break
            
            # If usedPhraseIndex has items, check for duplicates
            if len(usedPhraseIndex) != 0:
                # Create a flag to 'ok' each load message with
                usedFlag = True
                
                while usedFlag:
                    usedFlag = False
                    # Pick a message
                    messageIndex = random.randint(0,(len(newList)-1))
                    # Check that the message hasn't already been said
                    for index in usedPhraseIndex:
                        # If it has, break and pick a new message
                        if messageIndex == index:
                            usedFlag = True
                            
            # No items, just use any phrase!
            else:
                messageIndex = random.randint(0,(len(newList)-1))
            
            # Display the phrase on the surface
            newMessage = text.renderFont(3, 1, newList[messageIndex])
            textPos = ((20, (10+(len(usedPhraseIndex)*30))))
            screen.blit(newMessage, textPos)
            pygame.display.flip()
            
            # Append index so phrase is not reused.
            usedPhraseIndex.append(messageIndex)
            # And wait...
            time.sleep(0.1)
        
        # Sleep my pretty.... sleep...
        time.sleep(0.75)
    
    time.sleep(1.5)
    return

# If this module is run directly
if __name__ == '__main__':
    # When run directly, create the PyGame surface and window
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height)) # Create the screen
    pygame.display.set_caption("S-kuru") # And give it a title
    mainMenu(screen)
    pygame.quit()
    raw_input("Finished!")
