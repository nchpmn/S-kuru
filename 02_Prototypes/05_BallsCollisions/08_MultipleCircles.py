import pygame, random, math

## CLASSES ----------------------------------------------

class Ball():
    def __init__(self, (x,y), size):
        """Setting up the new instance"""
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0,128,255)
        self.thickness = 0
        self.speed = 0.01
        self.angle = math.pi/2

    def display(self):
        """Draw the ball"""
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        """Move the ball according to angle and speed"""
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.speed *= drag

class Circle():
    def __init__(self, (x,y), size):
        """Set up the new instance of the Circle class"""
        self.x = x
        self.y = y
        self.size = size
        self.colour = (236, 236, 236)
        self.thickness = 2
        self.angle = 0 # Needed for collision...
        self.speed = 0 # detection against balls

    def display(self):
        """Draw the circle"""
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)        

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
        # How this will work:
        # FOR each BALL
        #     collide = True
        #     WHILE collide == True
        #         FOR each CIRCLE
        #             IF BALL inside CIRCLE
        #                 collide = False
        #         IF collide = True * Will only happen if outside all circles *
        #             [..Do the collision..]


    hit = False
    for c in circles:
        dx = c.x - ball.x
        dy = c.y - ball.y
        distance = math.hypot(dx, dy)

        if distance <= c.size - ball.size:
            # If BALL inside any CIRCLE
            hit = False
            break
        else:
            hit = c

    if hit:
        dx = hit.x - ball.x
        dy = hit.y - ball.y
            
        tangent = math.atan2(dy, dx)
        ball.angle = 2 * tangent - ball.angle
        ball.speed *= elasticity + 0.251

        angle = 0.5 * math.pi + tangent
        ball.x += math.sin(angle) + 1
        ball.y -= math.cos(angle) + 1
        
## INIT -------------------------------------------------

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("S-kuru")
running = True
balls = []
circles = []
FPSClock = pygame.time.Clock() # FPS Limiter

gravity = (math.pi, 0.1) # The vector for gravity
drag = .999
elasticity = 0.5

# Let's create a ball for testing.
newBall = Ball((100,100), 30)
newBall.speed = 3
newBall.angle = (math.pi/2)
balls.append(newBall)

newBall = Ball((200,100), 30)
newBall.speed = 2
newBall.angle = -(math.pi/3)
balls.append(newBall)

# Two circles for testing:
newCircle = Circle((150,150), 150)
circles.append(newCircle)

secondCircle = Circle((300,200), 150)
circles.append(secondCircle)

## MAIN ---------------------------------------------------
    
while running == True:
    FPSClock.tick(60)
    screen.fill((33,33,33))

    for c in circles:
        # For each circle, do this
        c.display()

    for b in balls:
        # For each ball...
        
        b.move()

        for i, ball in enumerate(balls):
            for ball2 in balls[i+1:]: # Not a full loop: we don't need to...
                collideBalls(ball, ball2)  # test every ball against every other

        collideCircle(b)
        
        b.display()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                
    pygame.display.flip() # Display from frame buffer
pygame.quit()
