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

    def bounce(self):
        """Test for collisions between ball and window"""
        # This works by testing if ball is outside window and
        # adjusting angle and x / y value accordingly to
        # simulate a bounce.
        
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = self.angle * -1
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = self.angle * -1

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
        
## INIT -------------------------------------------------

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("01_BallsClass.py")
running = True
balls = []
FPSClock = pygame.time.Clock() # FPS Limiter

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
    screen.fill((33,33,33)) # Background colour

    for b in balls: # For each ball in the list, each frame
        b.move() # Move the ball
        b.bounce() # Check for window collision
        b.display() # Display the ball
    pygame.display.flip()

    for event in pygame.event.get(): # Check for quit
        if event.type == pygame.QUIT:
                running = False
                
    pygame.display.flip() # Display from frame buffer
