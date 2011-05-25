#!/usr/bin/env python
#encoding: UTF-8

import playGame
import module_fileHandling
import Module_text
import pygame
import string

# --- TEXTBOX FUNCTIONS -----------------------------------

def textBoxDisplay(screen, message):
    """Display the text box"""
    # Use textID = 2 for textbox content
    if len(message) != 0:
        Module_text.updateDynamic(message, 2, ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10), screen)
        

# --- MAIN SECTION ----------------------------------------
def parseLevel(screen):

    title = Module_text.basicText(((400-(int(Module_text.calculateSize("Player Name", 1)[0])/2)),100), "Player Name", 1, screen)
    playerName = ""
    current_string = []
    screen.fill((146,146,146))
    while 1:
        screen.fill((146,146,146))
        title.updateText()
        
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            inkey = event.key
            if inkey == pygame.K_BACKSPACE:
                current_string = current_string[0:-1]
            elif inkey == pygame.K_RETURN:
                break
            elif inkey == pygame.K_MINUS:
                current_string.append("_")
            elif inkey <= 127:
                current_string.append(chr(inkey))
        else:
            pass
        
        textBoxDisplay(screen, string.join(current_string,""))
        
        pygame.display.flip()
    
    playerName = string.join(current_string,"")
    
    
    
    
    levelNumb = module_fileHandling.loadPlayer(playerName) # This will need to be changed
    loadText, loadCircles, loadBalls, loadExits = module_fileHandling.loadLevel(levelNumb)
    
    # loadText = [LevelName, HintText, [WinType, WinCondition]]

    playGame.play(loadText, loadCircles, loadBalls, loadExits, screen)
