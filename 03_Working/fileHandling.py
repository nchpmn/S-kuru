#!/usr/bin/env python
#encoding: UTF-8

# --- IMPORT MODULES --------------------------------------
import pygame
import yaml
import os

# --- CLASSES ---------------------------------------------

# --- FUNCTIONS -------------------------------------------
def playerProfileLoad(playerName):
    fileName = os.path.abspath(os.path.join("04_players", "Plr-" + str(playerName) + ".skp"))
    
    try:
        # This code does not work. I am trying to create the playerFile if it doesn't exist.
        playerFile = open(fileName,'r')
        playerData = yaml.load(playerFile)
        playerFile.close()
        
    except IOError as e:
        playerFile = open(fileName, 'w')
        playerFile.write("001")
        playerFile.close
        playerData = "001{><}001"
    
    return playerData
