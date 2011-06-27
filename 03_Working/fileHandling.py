#!/usr/bin/env python
#encoding: UTF-8

# --- IMPORT MODULES --------------------------------------
import pygame
import yaml
import os

# --- CLASSES ---------------------------------------------

# --- FUNCTIONS -------------------------------------------
def playerProfileLoad(playerName):
    fileName = os.path.abspath(os.path.join("04_players", "Plyr-" + str(playerName) + ".skp"))
    
    try:
        playerFile = open(fileName,'r')
        playerData = yaml.load(playerFile)
        playerFile.close()
    
    # The file doesn't exist, so let's create it and fill it with data
    except IOError as e:
        # Why am I bothering to print the error?
        print e
        playerFile = open(fileName, 'w')
        playerData = ["1","1"]
        yaml.dump(playerData, playerFile)
        playerFile.close()
        
    return playerData

def levelLoad(fileName):
    levelFile = open(fileName, 'r')
    loadData = yaml.load(levelFile)
    
    # This will appear in the sequence: Text, Circles, Balls, Exits
    
    return loadData

# If this module is run directly
if __name__ == '__main__':
    # When run directly, simulate input
    playerName = "NATHAN"
    print playerProfileLoad(playerName)
    pygame.quit()
    raw_input("Finished!")