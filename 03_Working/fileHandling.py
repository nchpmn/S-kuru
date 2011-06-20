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
        
    except IOError as e:
        print e
        playerFile = open(fileName, 'w')
        #playerFile.write(["001","001"])
        #playerFile.close
        playerData = ["1","1"]
    
    # These lines need to be fixed when YAML parsing is implemented.
    return ["1","1"]

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