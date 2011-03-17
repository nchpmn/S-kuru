#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING -----------------------------------
import pygame
import random
import math
import Module_text
import module_fileHandling

gravity = (math.pi, 0.1) # The vector for gravity
drag = .999
elasticity = 0.5
balls = []
circles = []
## CLASSES ----------------------------------------------

class Ball():
	def __init__(self, (x,y), size, colourID):
		"""Setting up the new instance"""
		self.x = x
		self.y = y
		self.size = size
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

	def display(self, screen):
		"""Draw the ball"""
		# pygame.gfxdraw.aacircle(screen,cx,cy,new_dist,settings['MINIMAP_RINGS'])
		pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

	def move(self):
		"""Move the ball according to angle and speed"""
		self.x += math.sin(self.angle) * self.speed
		self.y -= math.cos(self.angle) * self.speed
		(self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
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


## FUCNTIONS --------------------------------------------
def addVectors((angle1, length1), (angle2, length2)):
	"""Take two vectors and find the resultant"""
	x = math.sin(angle1) * length1 + math.sin(angle2) * length2
	y = math.cos(angle1) * length1 + math.cos(angle2) * length2
	length = math.hypot(x,y)
	angle = 0.5 * math.pi - math.atan2(y,x)
	return (angle, length)

def collideBalls(b1, b2):
	"""Check for collision between two balls"""
	dx = b1.x - b2.x
	dy = b1.y - b2.y

	distance = math.hypot(dx, dy)

	if distance < b1.size + b2.size: # If they have collided
		tangent = math.atan2(dy, dx) # Find the tangent of the point
		angle = 0.5 * math.pi + tangent # We use this later on
		b1.angle = 2*tangent - b1.angle # Alter angles
		b2.angle = 2*tangent - b2.angle
		(b1.speed, b2.speed) = (b2.speed, b1.speed) # Swap speeds
		b1.speed *= elasticity # Reduce speed due to elasticity
		b2.speed *= elasticity

		b1.x += math.sin(angle) # Move particles away from each other
		b1.y -= math.cos(angle)
		b2.x -= math.sin(angle)
		b2.y += math.cos(angle)

def collideCircle(ball):
	"""Check for collision between a ball and a circle"""

	hit = False
	closestDist = 0

	for c in circles:
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
		dx = hit.x - ball.x
		dy = hit.y - ball.y

		tangent = math.atan2(dy, dx)
		ball.angle = 2 * tangent - ball.angle
		ball.speed *= elasticity + 0.251

		distance = math.hypot(dx, dy)
		reboundFactor = (hit.size - ball.size) - distance
		# reboundFactor must be more than 1

		angle = 0.5 * math.pi + tangent
		ball.x += math.sin(angle) * -reboundFactor
		ball.y -= math.cos(angle) * -reboundFactor

def spawnBall(position, balls):
	newBall = Ball(position, 15)
	newBall.speed = 2
	newBall.angle = -(random.randint(1, 3) * random.random() * 3.1415927)
	balls.append(newBall)

def Play(screen):
    # INIT ------------------------------------------------
    FPSClock = pygame.time.Clock() # FPS Limiter
    
    print "PLAY THE GAME"
    levelNumb = 001
    loadText, loadCircles, loadBalls = module_fileHandling.loadLevel(levelNumb)
    
    # loadText = [LevelName, HintText, [WinType, WinCondition]
    # loadCircles = [ [List Per Circle --> [PosX, PosY], CircleSize, [R, G, B] ] ]
    # load Balls = [ [List Per Ball --> [PosX, PosY], BallSize, BallColourID] ] ]
    
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
