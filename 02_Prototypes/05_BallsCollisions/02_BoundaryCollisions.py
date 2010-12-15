import pygame, random, math

## INIT -------------------------------------------------

class Ball():
    def __init__(self, (x,y), size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0,128,255)
        self.thickness = 1
        self.speed = 0.01
        self.angle = math.pi/2
    
    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def bounce(self):
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
        
        
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("01_BallsClass.py")
running = True
balls = []
FPSClock = pygame.time.Clock()

for n in range(0,5):
    size = 30
    x = random.randint(size, 600 - size)
    y = random.randint(size, 400 - size)
    newBall = Ball((x,y), size)
    newBall.speed = random.randint(1,4)
    newBall.angle = random.uniform(0, math.pi*2)

    print newBall.speed
    
    balls.append(newBall)

## MAIN ---------------------------------------------------
    
while running == True:
    FPSClock.tick(60)
    screen.fill((33,33,33))

    for b in balls:
        b.move()
        b.bounce()
        b.display()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                
    pygame.display.flip()
