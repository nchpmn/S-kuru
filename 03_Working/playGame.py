#!/usr/bin/env python
#encoding: UTF-8

# --- IMPORT MODULES --------------------------------------
import pygame
import text
import string
import fileHandling
import singleLevel

# --- FUNCTIONS -------------------------------------------
def preGame(screen):
    # Three things to do:
    #   1. get player profile
    #   2. pick level type & level
    #   3. load level
    
    playerData, playerName = playerProfile(screen)
    levelChoose(screen, playerData, playerName)
    # loadLevel() is now called from within levelChoose()
    # loadLevel(playerData, levelSet)

# Get player Profile
def playerProfile(screen):
    textSize = text.calculateTextSize(1, "Player Name:")[0]
    title = text.StaticText((400 - textSize/2), 100, "Player Name", 3, 1, screen)
    playerName = ""
    current_string = []

    while 1:
        screen.fill((146,146,146))
        
        title.update()
        
        # --- Fetch & Handle Events ---
        event = pygame.event.poll()
        
        # Text entry handling
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
        
        # Render and display the textbox
        if len(current_string) != 0:
            content = string.join(current_string,"")
            text.updateDynamicText(((screen.get_width() / 2) - 100), ((screen.get_height() / 2) - 10), content, 2, 2, screen)        
        
        pygame.display.flip()
    
    # Final player Name
    return fileHandling.playerProfileLoad(string.join(current_string,"")), string.join(current_string, "")
    
def levelChoose(screen, playerData, playerName):
    levelMText = [["Campaign", 3], ["Custom", 4]]
    levelMenu = text.menuCreator(levelMText, 200, 300, 100, 1, 2, screen)
    
    levelMenuClock = pygame.time.Clock()
    levelChooseRunning = True
    
    menuHeader = text.StaticText(100, 25, "Select Level Type:", 2, 1, screen)
    
    while levelChooseRunning:
        levelMenuClock.tick(60)
        
        screen.fill((146,146,146))
        
        # --- Update Objects
        for button in levelMenu:
            button.update()
        menuHeader.update()
        
        # --- Event Catching & Handling ---
        for event in pygame.event.get():
            # Quit PyGame safely upon exit
            if event.type == pygame.QUIT:
                levelMenuRunning = False
            # Make the buttons do actions
            if event.type == pygame.MOUSEBUTTONUP:
                mousePos = pygame.mouse.get_pos()
                for button in levelMenu:
                    X = button.getXPos()
                    Y = button.getYPos()
                    if X[0] < mousePos[0] < X[1] and Y[0] < mousePos[1] < Y [1]:
                        levelChooseRunning = False
                        loadLevel(playerData, playerName, button.doAction(screen), screen)
        
        pygame.display.flip()

def loadLevel(playerData, playerName, levelSet, screen):
    # If playing the **campaign** levels...
    if str(levelSet) == "0":
        # Create the filename
        fileName = "02_levels\Lvl-" + str(playerData[0]).zfill(3) + ".skl"     
    # Otherwise, we must be playing the **user** levels...
    elif str(levelSet) == "1":
        print "COMING SOON...", playerData[1]
    
    # This data is an array: Text, Circles, Balls, Exits
    levelData = fileHandling.levelLoad(fileName)
    
    nextLevel = singleLevel.singleLevel(levelData, playerData, screen)
    
    postLevel(nextLevel, playerName, screen)

def postLevel(nextLevel, playerName, screen):
    if nextLevel == True:
        # User has won level and will progress
        newPlayerData = fileHandling.incrementProfileCampaignLevel(playerName)
        loadLevel(newPlayerData, playerName, 0, screen)
    else:
        # User has lost level - restart
        pass
    
# If this module is run directly
if __name__ == '__main__':
    # When run directly, create the PyGame surface and window
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height)) # Create the screen
    pygame.display.set_caption("S-kuru") # And give it a title
    preGame(screen)
    pygame.quit()
    raw_input("Finished!")