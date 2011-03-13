#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING ------------------------------------
import pygame
import random
import math
import yaml

## FUNCTIONS ----------------------------------------------

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
    
    return text, circles, balls