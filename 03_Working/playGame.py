#!/usr/bin/env python
#encoding: UTF-8

# --- IMPORT MODULES --------------------------------------
import pygame
import text
import string
import math
import physicsEngine
import fileHandling
import graphics

# --- UTILITY FUNCTIONS -----------------------------------
def setCircleColour(colourID):
    if colourID == 0:
        colour = (236,236,236)
    elif colourID == 1:
        colour = (255,0,0)
    elif colourID == 2:
        colour = (0,255,0)
    elif colourID == 3:
        colour = (0,0,255)
    else:
        colour = (0,0,0)
    return colour

def setBallColour(colourID):
    if colourID == 0:
        colour = (136,136,136)
    elif colourID == 1:
        colour = (135,0,0)
    elif colourID == 2:
        colour = (0,135,0)
    elif colourID == 3:
        colour = (0,0,135)
    else:
        colour = (255,255,255)
    return colour

# --- FUNCTIONS -------------------------------------------
def preGame(screen):
    # Three things to do:
    #   1. get player profile
    #   2. pick level type & level
    #   3. load level
    
    playerData = playerProfile(screen)
    levelChoose(screen, playerData)
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
    return fileHandling.playerProfileLoad(string.join(current_string,""))
    
def levelChoose(screen, playerData):
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
                        loadLevel(playerData, button.doAction(screen), screen)
        
        pygame.display.flip()

def loadLevel(playerData, levelSet, screen):
    # If playing the **campaign** levels...
    if str(levelSet) == "0":
        # Create the filename
        fileName = "02_levels\Lvl-" + str(playerData[0]).zfill(3) + ".skl"
        
        # This data is an array: Text, Circles, Balls, Exits
        levelData = fileHandling.levelLoad(fileName)
        
        playGame(screen, playerData, levelData)       
        
    # Otherwise, we must be playing the **user** levels...
    elif str(levelSet) == "1":
        print "COMING SOON...", playerData[1]

def playGame(screen, playerData, levelData):
    # Default data
    textData = levelData[0]
    circleData = levelData[1]
    ballData = levelData[2]
    exitData = levelData[3]
    
    # Level data - to be appended once Class() objects created
    textObj = []
    circleObj = []
    ballObj = []
    exitObj = []
    
    # And created data
    userCircles = []
    
    # The vector for gravity
    gravity = (math.pi, 0.1)
    # Slow the bounce some amount
    drag = .999
    # Elasticity - so balls bounce back apart again
    elasticity = 0.5
    
    # --- CLASSES -----------------------------------------
    class Ball():
        def __init__(self, x, y, size, colourID, screen):
            self.x = x
            self.y = y
            self.radius = size
            self.colour = setBallColour(colourID)
            self.screen = screen
            
            # And some default parameters
            self.exited = False
            self.thickness = 0
            self.speed = 0.01
            self.angle = math.pi/2
        
        # Calculate movement and blit the ball to the surface
        def update(self):
            # Check that the ball hasn't exited before doing calculations
            if self.exited != True:
                # Move x
                self.x += math.sin(self.angle) * self.speed
                # Move y
                self.y -= math.cos(self.angle) * self.speed
                # Add vectors to calculate speed and velocity
                (self.angle, self.speed) = physicsEngine.addVectors((self.angle, self.speed), gravity)
                # Multiply by drag to reduce speed due to "friction"
                self.speed *= drag
                # Blit to screen
                pygame.draw.circle(surface, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
                
    class Circle():
        def __init(self, x, y, size, colourID, screen):
            self.pos = (int(x),int(y))
            self.radius = size
            self.colour = setCircleColour(colourID)
            self.surface = screen
            
            # Some default parameters
            self.thickness = 0
            # The next two are needed for collision detection against the balls
            self.angle = 0
            self.speed = 0
        
        def update(self):
            pygame.draw.circle(self.surface, self.colour, self.pos, self.size)
    
    class Exit():
        def __init__(self, x, y, size, colourID):
            self.pos = (int(x), int(y))
            # Remember that the circle (collisions) size is **radius** - so half the self.size of the square
            self.size = size*2 # Because square, height and width are both self.size
            self.colour = setBallColour(colourID)

        def update(self):
            pygame.draw.rect(surface, self.colour, (self.x, self.y, self.size, self.size))
    
    # --- LEVEL INIT --------------------------------------
    # Set up extra bits of the level
    levelClock = pygame.time.Clock() # Limit the FPS during the level
    runningLevel = True # Let us exit the level once completed
    
    # Set the text variables
    # textData = [LevelName, HintText, [WinType, WinCondition]]
    
    # Level Name
    newText = text.StaticText(15, 5, textData[0], 2, 2, screen)
    textObj.append(newText)

    # Hint Text
    newText = text.StaticText(5, (585-text.calculateTextSize(textData[1], 4)), textData[1], 2, 4, screen)
    textObj.append(newText)
    hintRect = graphics.SimpleBox(0, 560, 800, 40, (225, 128, 0), screen)
    
    # Goal Text
    if textData[2][1] == 2:
        newText = text.StaticText((100,100), "Goal: < " + str(circleGoal), 3, screen)
        textObj.append(newText)
    
    # --- MAIN GAME LOOP ----------------------------------
    while runningLevel:
        levelClock.tick(60)
        
        # Start with a clean frame
        screen.fill((146,146,146))
        
        # Update & Blit Objects to Surface
        updateObjects(screen, textObj, circleObj, userCircles, ballObj, exitObj, hintRect)
    
        pygame.display.flip()

def updateObjects(screen, text, circles, userCircles, balls, exits, hintRect):
    for t in text:
        t.update()
    
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