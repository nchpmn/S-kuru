#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING ------------------------------------
import pygame
import random
import math
import yaml

## LEVELS -------------------------------------------------

def loadLevel(levelNumb):
    fileName = "03_Levels\Lvl-" + str(levelNumb).zfill(3) + ".skl"
    print fileName
    
    levelFile = open(fileName, 'r')
    loadData = yaml.load(levelFile)
    
    print "Loaded..."
    
    print loadData
    
    text = loadData[0]
    circles = loadData[1]
    balls = loadData[2]
    exits = loadData[3]
    
    return text, circles, balls, exits

## PLAYER PROFILES ----------------------------------------

def loadPlayer(playerName):
    fileName = "02_Players\Plyr-" + str(playerName) + ".skp"
    
    try:
        # This code does not work. I am trying to create the playerFile if it doesn't exist.
        playerFile = open(fileName,'r')
        playerData = yaml.load(playerFile)
        playerFile.close()
        
    except IOError as e:
        playerFile = open(fileName, 'w')
        playerFile.write("001")
        playerFile.close
        playerData = "001"
    
    return playerData
