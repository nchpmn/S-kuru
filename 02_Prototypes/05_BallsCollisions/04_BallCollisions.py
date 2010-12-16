import pygame, random, math

## CLASSES ----------------------------------------------

class Ball():
    def __init__(self, (x,y), size):
        """Setting up the new instance"""
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0,128,255)
        self.thickness = 1
        self.speed = 0.01
        self.angle = math.pi/2
    
    def display(self):
        """Draw the ball"""
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        """Move the ball according to angle and speed"""
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        # Next, account for gravity
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        # Then, friction / drag
        self.speed *= drag

    def bounce(self):
        """Test for collisions between ball and window"""
  
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = self.angle * -1
            self.speed *= elasticity # Added to all to account for elasticity
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = self.angle * -1
            self.speed *= elasticity

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

## FUCNTIONS --------------------------------------------
def addVectors((angle1, length1), (angle2, length2)):
    """Take two vectors and find the resultant"""
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    length = math.hypot(x,y)
    angle = 0.5 * math.pi - math.atan2(y,x)
    return (angle, length)

def collide(b1, b2):
    dx = b1.x - b2.x
    dy = b1.y - b2.y

    distance = math.hypot(dx, dy)
    
    if distance < b1.size + b2.size: # If they have collided
        tangent = math.atan2(dy, dx) # Find the tangent of the point
        b1.angle = 2*tangent - b1.angle # Alter angles
        b2.angle = 2*tangent - b2.angle
        (b1.speed, b2.speed) = (b2.speed, b1.speed) # Swap speeds
        b1.speed *= elasticity # Reduce speed due to elasticity
        b2.speed *= elasticity

        b1.x += math.sin(angle) # Move particles away from each other
        b1.y -= math.cos(angle)
        b2.x -= math.sin(angle)
        b2.y += math.cos(angle)
## INIT -------------------------------------------------

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("01_BallsClass.py")
running = True
balls = []
FPSClock = pygame.time.Clock() # FPS Limiter

gravity = (math.pi, 0.2) # The vector for gravity
drag = .999
elasticity = 0.58

for n in range(0,5): # Create a whole bunch of new balls
    size = 30
    x = random.randint(size, 600 - size)
    y = random.randint(size, 400 - size)
    newBall = Ball((x,y), size)
    newBall.speed = random.randint(1,4)
    newBall.angle = random.uniform(0, math.pi*2)

    print newBall.speed
    
    balls.append(newBall) # Append the new ball to the list

## MAIN ---------------------------------------------------
    
while running == True:
    FPSClock.tick(60) # Set FPS here
    screen.fill((33,33,33))

    for b in balls:
        b.move()
        b.bounce()

        for i, ball in enumerate(balls):
            for ball2 in balls[i+1:]: # Not a full loop: we don't need to
                collide(ball, ball2)  # test every ball against every other
        b.display()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                
    pygame.display.flip() # Display from frame buffer
