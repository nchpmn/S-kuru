#!/usr/bin/env python
#encoding: UTF-8

# --- IMPORT MODULES --------------------------------------
import math
import pygame
import graphics
import physicsEngine
import text

# --- VARIOUS VARIABLES -----------------------------------
gravity = (math.pi, 0.1) # The vector for gravity
drag = .999
elasticity = 0.5

# --- CLASSES ---------------------------------------------
class Ball():
    def __init__(self, x, y, size, colourID, screen):
        self.x = x
        self.y = y
        self.radius = size
        self.colour = setBallColour(colourID)
        self.colourID = colourID
        self.surface = screen
        
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
            pygame.draw.circle(self.surface, self.colour, (int(self.x), int(self.y)), self.radius, self.thickness)
            
class Circle():
    def __init__(self, x, y, size, colourID, screen):
        self.pos = (int(x),int(y))
        self.x = x
        self.y = y
        self.radius = size
        self.colour = setCircleColour(colourID)
        self.colourID = colourID
        self.surface = screen
        self.radius = size
        
        # Some default parameters
        self.thickness = 0
        # The next two are needed for collision detection against the balls
        self.angle = 0
        self.speed = 0
    
    def update(self):
        pygame.draw.circle(self.surface, self.colour, self.pos, self.radius)

class Exit():
    def __init__(self, x, y, size, colourID, screen):
        self.x = x
        self.y = y
        # Remember that the circle (collisions) size is **radius** - so half the self.size of the square
        self.size = size*2 # The square's "size" (side length) is twice the circle's radius
        self.radius = size # The circle's "size"
        self.colour = setBallColour(colourID)
        self.surface = screen

    def update(self):
        pygame.draw.rect(self.surface, self.colour, (self.x, self.y, self.size, self.size))


# --- FUNCTIONS -------------------------------------------
def updateObjects(screen, texts, circles, userCircles, balls, exits, hintRect):
    for c in circles:
        c.update()
    
    for c in userCircles:
        c.update()
    
    for e in exits:
        e.update()
    
    for i, b in enumerate(balls):
        b.update()
        # Collision Detection against other Balls
        for ball2 in balls[i+1:]:
            if physicsEngine.collideTest(b, ball2):
                physicsEngine.exteriorCircleBounce(b, ball2)
        tempCircles = []
        for c in circles:
            tempCircles.append(c)
        for c in userCircles:
            tempCircles.append(c)
        physicsEngine.collideCircleTest(b, tempCircles)
        for e in exits:
            if physicsEngine.collideTest(b, e):
                b.exited = True
    
    hintRect.update()
    
    for t in texts:
        t.update()
    
    text.updateDynamicText((800-15-text.calculateTextSize(2, "Circles: " + str(len(userCircles)))[0]), 10, "Circles: " + str(len(userCircles)), 2, 2, screen)

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

def winCheck(balls, userCircles, levelData):
    levelType, levelGoal = levelData[0], levelData[1]
    if int(levelType) == 1:
        pass
    elif int(levelType) == 2:
        # If levelType is Circles
        winFlag = True
        loseFlag = False
        for b in balls:
            # For each ball
            if b.exited == False:
                # If the ball hasn't exited, break
                winFlag = False
                break
        if winFlag == True:
            # If all the balls have exited, check the number of circles
            if len(userCircles) <= levelGoal:
                # If we've used less than the right number of circles
                return winFlag, loseFlag
            else:
                loseFlag = True
                return winFlag, loseFlag
        else:
            # Continue the Level
            winFlag, loseFlag = False, False
            return winFlag, loseFlag
    elif int(levelType) == 3:
        # If levelType is Selected Coloured Balls Only
        winFlag = True
        loseFlag = False
        for b in balls:
            if b.colourID == int(levelGoal) and b.exited == False:
                # The ball is of the correct colour but has not exited
                winFlag = False
                break
            elif b.colourID != int(levelGoal) and b.exited == True:
                # An exited ball is of the wrong colour
                winFlag = False
                loseFlag = True
                break
        return winFlag, loseFlag
    else:
        print "ERROR - WINCHECK FUNCTION IN SINGLELEVEL MODULE"

# --- MAIN LOOP -------------------------------------------
def singleLevel(levelData, playerData, screen):
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
    userCircleObj = []
    
    # The vector for gravity
    gravity = (math.pi, 0.1)
    # Slow the bounce some amount
    drag = .999
    # Elasticity - so balls bounce back apart again
    elasticity = 0.5

    # --- LEVEL INIT --------------------------------------
    # Set up extra bits of the level
    levelClock = pygame.time.Clock() # Limit the FPS during the level
    runningLevel = True # Let us exit the level once completed
    mouseIsDown = False
    r = 10
    currentColourID = 0
    winner, loser = False, False
    
    # --- Set the text variables
    # textData = [LevelName, HintText, [WinType, WinCondition]]
    
    # Level Name
    newText = text.StaticText(15, 10, textData[0], 2, 2, screen)
    textObj.append(newText)

    # Hint Text
    newText = text.StaticText(5, 570, textData[1], 2, 4, screen)
    textObj.append(newText)
    hintRect = graphics.SimpleBox(0, 560, 800, 40, (128, 128, 128), screen)
    
    # Goal Text
    # Game Types: 1 ==> Timed; 2 ==> Circles; 3 ==> Selective
    goalTextX, goalTextY = 635, 65
    if int(textData[2][0]) == 1:
        pass
    elif int(textData[2][0]) == 2:
        circleGoal = textData[2][1]
        newText = text.StaticText(goalTextX, goalTextY, "Goal: < " + str(circleGoal), 2, 3, screen)
        textObj.append(newText)
    elif int(textData[2][0]) == 3:
        selectiveColourID = textData[2][1]
        if selectiveColourID == 0:
            colourText = "White"
        elif selectiveColourID == 1:
            colourText = "Red"
        elif selectiveColourID == 2:
            colourText = "Green"
        elif selectiveColourID == 3:
            colourText = "Blue"
        else:
            colourText = "ERROR"
        newText = text.StaticText(goalTextX, goalTextY, "Colour: " + colourText, 2, 3, screen)
        
    # --- Set up game objects - balls, circles and exits
    print circleData
    for cir in circleData: # Create objects from the list
        newCircle = Circle(cir[0], cir[1], cir[2], cir[3], screen)
        circleObj.append(newCircle)
    
    print ballData
    for ba in ballData:
        newBall = Ball(ba[0], ba[1], ba[2], ba[3], screen)
        ballObj.append(newBall)
    
    print exitData
    for ex in exitData:
        newExit = Exit(ex[0], ex[1], ex[2], ex[3], screen)
        exitObj.append(newExit)
    
    # --- MAIN GAME LOOP ----------------------------------
    while runningLevel:
        levelClock.tick(60)
        
        # Start with a clean frame
        screen.fill((146,146,146))
        
        # Update & Blit Objects to Surface
        updateObjects(screen, textObj, circleObj, userCircleObj, ballObj, exitObj, hintRect)
        
        # Event Handling & User Interaction
        
        # Grow Circle if user is holding mouse down
        if mouseIsDown == True:
            pygame.draw.circle(screen, setCircleColour(currentColourID), circleCentre, r, 2)
            if r < 150:
                r += 1
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningLevel = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                circleCentre = pygame.mouse.get_pos()
                mouseIsDown = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouseIsDown = False
                newCircle = Circle(circleCentre[0], circleCentre[1], r, currentColourID, screen)
                userCircleObj.append(newCircle)
                r = 10
            elif event.type == pygame.KEYDOWN:
                currentKey = event.key
                if currentKey == pygame.K_1:
                    currentColourID = 0
                elif currentKey == pygame.K_2:
                    currentColourID = 1
                elif currentKey == pygame.K_3:
                    currentColourID = 2
                elif currentKey == pygame.K_4:
                    currentColourID = 3
                else:
                    pass
        
        print textData[2]
        if len(userCircleObj) > 0:
            winner, loser = winCheck(ballObj, userCircleObj, textData[2])
            if winner == True and loser == False:
                # User has won level and not lost
                runningLevel = False
                return True
            elif loser == True:
                # User did not finish level but did lose level
                runningLevel = False
                return false
        
        pygame.display.flip()

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