#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING -----------------------------------
import pygame
import random
import math
import Module_text
import module_physicsEngine
import Module_graphics

balls = []
circles = []
exits = []
staticText = []

gravity = (math.pi, 0.1) # The vector for gravity
drag = .999
elasticity = 0.5

## CLASSES ----------------------------------------------

class Ball():
    def __init__(self, (x,y), size, colourID):
        """Setting up the new instance"""
        self.x = x
        self.y = y
        self.size = size
        self.exited = False
        self.colour = setColour(colourID)
        self.thickness = 0
        self.speed = 0.01
        self.angle = math.pi/2

    def display(self, surface):
        """Draw the ball"""
        # pygame.gfxdraw.aacircle(screen,cx,cy,new_dist,settings['MINIMAP_RINGS'])
        if self.exited != True:
            pygame.draw.circle(surface, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        """Move the ball according to angle and speed"""
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        (self.angle, self.speed) = module_physicsEngine.addVectors((self.angle, self.speed), gravity)
        self.speed *= drag

class Circle():
    def __init__(self, (x,y), size, colourID):
        """Set up the new instance of the Circle class"""
        self.x = x
        self.y = y
        self.size = size
        self.colour = setColour(colourID)
        self.thickness = 2
        self.angle = 0 # Needed for collision...
        self.speed = 0 # detection against balls

    def display(self, surface):
        """Draw the circle"""
        pygame.draw.circle(surface, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

class Exit():
    def __init__(self, (x,y), size, colourID):
        """Set up a new instance of the Exit class"""
        self.x = x
        self.y = y
        self.size = size # Because square, height and width are both self.size
        self.colour = setColour(colourID)

    def display(self, surface):
        """Draw the exit"""
        #pygame.draw.rect(surface, self.colour, (self.x, self.y, self.size, self.size))
        pygame.draw.circle(surface, self.colour, (int(self.x), int(self.y)), self.size)

## FUCNTIONS --------------------------------------------
def collideBalls(b1, b2):
    """Check for collision between two balls"""
    if module_physicsEngine.collideTest(b1, b2): # If they have collided
        module_physicsEngine.ballBounce(b1, b2)

def collideCircle(ball):
    """Check for collision between a ball and a circle"""

    hit = False
    closestDist = 0
    circleIndex = -1

    for c in circles:
        # Code cannot be replaced with physicsEngine.collideTest because it
        # is slightly differnt, testing if ball [ball] inside a circle [c]
        circleIndex += 1
        dx = c.x - ball.x
        dy = c.y - ball.y
        distance = math.hypot(dx, dy)

        if distance <= c.size:
            # If BALL inside any CIRCLE
            hit = False
            break
        else:
            # If we're outside of _this_ circle. --> Check if any part of the ball is inside another circle
            tempCircleList = circles[:]
            tempCircleList.pop(circleIndex)
            
            for temp in tempCircleList:
                dx = temp.x - ball.x
                dy = temp.y - ball.y
                tempDistance = math.hypot(dx, dy)
                
                if tempDistance <= temp.size:
                    hit = False
                    break
            
            if closestDist < c.size - (distance - ball.size):
                hit = c
                closestDist = (c.size - (distance - ball.size))

    if hit:
        module_physicsEngine.circleBounce(hit, ball)

def collideExit(ball):
    """Check for a ball exiting (colliding with exit)"""
    for e in exits:
        if module_physicsEngine.collideTest(ball, e):
            ball.exited = True

def setColour(colourID):
    if colourID == 0:
        colour = (0,0,0)
    elif colourID == 1:
        colour = (255,0,0)
    elif colourID == 2:
        colour = (0,255,0)
    elif colourID == 3:
        colour = (0,0,255)
    else:
        colour = 0
    return colour
    
# --- MAIN ------------------------------------------------

def play(loadText, loadCircles, loadBalls, loadExits, screen):
# loadText = [LevelName, HintText, [WinType, WinCondition]]
    # Level Name
    newText = Module_text.basicText((15, 5), loadText[0], 2, screen)
    staticText.append(newText)

    # Hint Text
    newText = Module_text.basicText((5, (585-Module_text.calculateSize(loadText[1], 4)[1])), loadText[1], 4, screen)
    staticText.append(newText)
    hintRect = Module_graphics.simpleBox((0, 560), 800, 40, (225, 128, 0), screen)
    
    circleGoal = loadText[2][1]
    newText = Module_text.basicText((100,100), "Goal: < " + str(circleGoal), 3, screen)
    staticText.append(newText)


# loadCircles = [ [List Per Circle --> [PosX, PosY], CircleSize, [R, G, B] ] ]
    for cir in loadCircles: # Create objects from the list
        print cir
        newCircle = Circle(cir[0], cir[1], cir[2])
        circles.append(newCircle)
    print "Circles parsed"

# load Balls = [ [List Per Ball --> [PosX, PosY], BallSize, BallColourID] ] ]
    for ba in loadBalls:
        newBall = Ball(ba[0], ba[1], ba[2])
        balls.append(newBall)
    print "Balls parsed"
    
# loadExits = [ [List Per Exit --> [PosX, PosY], Size, ExitColourID ] ]
    for ex in loadExits:
        newExit = Exit(ex[0], ex[1], ex[2])
        exits.append(newExit)
    print "Exits parsed"

# Set up variables
    levelClock = pygame.time.Clock() # Need new clock - new main loop
    runningLevel = True
    circleCentre = (0,0)
    mouseIsDown = False
    currentColourID = 0
    r = 10
    circleCount = 0
    
    # --- MAIN LOOP -----------------------------------------
    while runningLevel == True:
        levelClock.tick(60)

        screen.fill((146,146,146))

        # Draw objects to the screen
        for c in circles:
            c.display(screen)
        for b in balls:
            b.move()
            for i, ball in enumerate(balls):
                for ball2 in balls[i+1:]:
                    collideBalls(ball, ball2)
            collideCircle(b)
            collideExit(b)
            b.display(screen)
        for e in exits:
            e.display(screen)
        hintRect.update() # Draw static before dynamic
        for t in staticText:
            t.updateText()

        # Dynamic Text
        Module_text.updateDynamic("Circles: " + str(circleCount), 2, (50,50), screen)

        # User Interaction
        if mouseIsDown == True:
            pygame.draw.circle(screen, setColour(currentColourID), circleCentre, r, 2)
            r += 1

        # Get events and act upon them
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningLevel = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print "MouseDown", pygame.mouse.get_pos()
                circleCentre = pygame.mouse.get_pos()
                mouseIsDown = True
            elif event.type == pygame.MOUSEBUTTONUP:
                print "MouseUp", pygame.mouse.get_pos()
                mouseIsDown = False
                newCircle = Circle(circleCentre, r, currentColourID)
                circles.append(newCircle)
                circleCount += 1
                r = 10

        pygame.display.flip()
