#!/usr/bin/env python
#encoding: UTF-8

# --- IMPORT MODULES --------------------------------------
import math
import pygame
import graphics
import physicsEngine

# --- CLASSES ---------------------------------------------
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


# --- FUNCTIONS -------------------------------------------

# --- MAIN LOOP -------------------------------------------
def singleLevel(levelData, screen):
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
    
    
    # --- LEVEL INIT --------------------------------------
    # Set up extra bits of the level
    levelClock = pygame.time.Clock() # Limit the FPS during the level
    runningLevel = True # Let us exit the level once completed
    
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
    for cir in circleData: # Create objects from the list
        newCircle = Circle()
        circleObj.append(newCircle)
    
    # --- MAIN GAME LOOP ----------------------------------
    while runningLevel:
        levelClock.tick(60)
        
        # Start with a clean frame
        screen.fill((146,146,146))
        
        # Update & Blit Objects to Surface
        updateObjects(screen, textObj, circleObj, userCircles, ballObj, exitObj, hintRect)
    
        pygame.display.flip()

def updateObjects(screen, text, circles, userCircles, balls, exits, hintRect):
    for c in circles:
        c.update
    
    for c in userCircles:
        c.update
    
    for b in balls:
        b.update
    
    hintRect.update()
    
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