import pygame, random, math

class Ball():
    def __init__(self, (x,y), size):
        self.x = x # Separate X
        self.y = y # and Y Values
        self.size = size
        self.colour = (0,128,255)
        self.thickness = 1
        self.speed = 0.01
        self.angle = math.pi/2 # We use radians, not degrees!
    
    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

## MAIN ---------------------------------------------------

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("01_BallsClass.py")
running = True
balls = []

for n in range(0,5):
    size = 30
    x = random.randint(size, 600 - size)
    y = random.randint(size, 400 - size)
    newBall = Ball((x,y), size)
    newBall.speed = random.random()
    newBall.angle = random.uniform(0, math.pi*2)
    
    balls.append(newBall)
    
while running == True:
    screen.fill((33,33,33))

    for b in balls:
        b.move()
        b.display()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                
    pygame.display.flip()
