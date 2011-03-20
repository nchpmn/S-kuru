#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING -----------------------------------
import pygame
import random
import math
import Module_text
import module_fileHandling
import module_physicsEngine

balls = []
circles = []
exits = []

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
        if colourID == 0:
            self.colour = (0,0,0)
        elif colourID == 1:
            self.colour = (255,0,0)
        elif colour == 2:
            self.colour = (0,255,0)
        elif colour == 3:
            self.colour = (0,0,255)
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
    def __init__(self, (x,y), size, colour):
        """Set up the new instance of the Circle class"""
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.thickness = 2
        self.angle = 0 # Needed for collision...
        self.speed = 0 # detection against balls

    def display(self, surface):
        """Draw the circle"""
        pygame.draw.circle(surface, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

class Exit():
    def __init__(self, (x,y), colourID, size):
        """Set up a new instance of the Exit class"""
        self.x = x
        self.y = y
        self.size = size # Because square, height and width are both self.size
        if colourID == 0:
            self.colour = (0,0,0)
        elif colourID == 1:
            self.colour = (255,0,0)
        elif colour == 2:
            self.colour = (0,255,0)
        elif colour == 3:
            self.colour = (0,0,255)
    
    def display(self, surface):
        """Draw the exit"""
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.size, self.size))

## FUCNTIONS --------------------------------------------
def collideBalls(b1, b2):
    """Check for collision between two balls"""
    if module_physicsEngine.collideTest(b1, b2): # If they have collided
        module_physicsEngine.ballBounce(b1, b2)

def collideCircle(ball):
    """Check for collision between a ball and a circle"""

    hit = False
    closestDist = 0

    for c in circles:
        # Code cannot be replaced with physicsEngine.collideTest because it
        # is slightly differnt, testing if ball [ball] inside a circle [c]
        dx = c.x - ball.x
        dy = c.y - ball.y
        distance = math.hypot(dx, dy)

        if distance <= c.size - ball.size:
            # If BALL inside any CIRCLE
            hit = False
            break
        else:
            # If we're outside of a circle.
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

def Play(screen):
    # INIT ------------------------------------------------
    FPSClock = pygame.time.Clock() # FPS Limiter
    
    print "PLAY THE GAME"
    levelNumb = 001
    loadText, loadCircles, loadBalls = module_fileHandling.loadLevel(levelNumb)
    
    # loadText = [LevelName, HintText, [WinType, WinCondition]
    # loadCircles = [ [List Per Circle --> [PosX, PosY], CircleSize, [R, G, B] ] ]
    # load Balls = [ [List Per Ball --> [PosX, PosY], BallSize, BallColourID] ] ]
    # loadExits = [ [List Per Exit --> [PosX, PosY], Size, ExitColourID
    
    for cir in loadCircles: # Create objects from the list
        print cir
        newCircle = Circle(cir[0], cir[1], cir[2])
        circles.append(newCircle)
    print "Circles parsed"
    
    for ba in loadBalls:
        newBall = Ball(ba[0], ba[1], ba[2])
        balls.append(newBall)
    print "Balls parsed"
    
    levelClock = pygame.time.Clock() # Need new clock - new main loop
    runningLevel = True
    
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
            b.display(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()
        

# --- GAME LOOP ------------------------------------------

#if __name__ = main
