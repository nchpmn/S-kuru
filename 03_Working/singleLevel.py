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
        self.radius = size
        self.colour = setCircleColour(colourID)
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
        self.size = size*2 # Because square, height and width are both self.size
        self.colour = setBallColour(colourID)
        self.surface = screen

    def update(self):
        pygame.draw.rect(self.surface, self.colour, (self.x, self.y, self.size, self.size))


# --- FUNCTIONS -------------------------------------------
def updateObjects(screen, text, circles, userCircles, balls, exits, hintRect):
    for c in circles:
        c.update()
    
    for c in userCircles:
        c.update()
    
    for i, b in enumerate(balls):
        b.update()
        # Collision Detection
        for ball2 in balls[i+1:]:
            if physicsEngine.collideTest(ball, ball2):
                physicsEngine.exteriorCircleBounce(ball, ball2)
    
    hintRect.update()
    
    for t in text:
        t.update()

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
    
    # --- Set the text variables
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
            r += 1
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningLevel = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                circleCentre = pygame.mouse.get_pos()
                mouseIsDown = True
            elif event.type == pygame.MOUSEBUTTONUP:
                print "MouseUp", pygame.mouse.get_pos()
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