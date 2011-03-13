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
    
    newData = yaml.load(fileName)
    
    print "Loaded..."
    
    return newData