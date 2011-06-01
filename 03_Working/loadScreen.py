#!/usr/bin/env python
#encoding: UTF-8

import yaml
import pygame


# If we're loading the main game and main menu
def mainMenu():
    # YAML.load the list of load items
    f = open('01_assets/loadScreenPhrases.skt', 'r')
    newList = yaml.load(f)
    print newList

# If this module is run directly
if __name__ == '__main__':
    mainMenu()
    raw_input("Finished!")
