#!/usr/bin/env python
#encoding: UTF-8

import playGame_circles
import module_fileHandling

def parseLevel(screen):

    

    levelNumb = 001 # This will need to be changed
    loadText, loadCircles, loadBalls, loadExits = module_fileHandling.loadLevel(levelNumb)
    
    # loadText = [LevelName, HintText, [WinType, WinCondition]]

    if loadText[2][0] == 1:
        # Game Type is Timed
        pass
    elif loadText[2][0] == 2:
        # Game Type is Circles
        playGame_circles.play(loadText, loadCircles, loadBalls, loadExits, screen)