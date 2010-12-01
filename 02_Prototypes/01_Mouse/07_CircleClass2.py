import pygame

# Init -------------------------------------------------------------
screen = pygame.display.set_mode((800,600))
FPSclock = pygame.time.Clock()

# Classes ----------------------------------------------------------
class Circle(self):
    def __init__(self, circleCentre, r):
        self.radius = r
        self.position = circleCentre

    def update(self, position, radius):
        pygame.draw.circle(screen, (236,236,236), position, radius)

# Main -------------------------------------------------------------
running = True
mouseIsDown = False
circleCentre = (0,0)
circles = []

while running:
    FPSclock.tick(60)
    screen.fill((92,92,92))

    for c in circles:
        c.update(c.position, c.radius)
        screen.blit(c.position, c.radius)

    if mouseIsDown == True:
        pygame.draw.circle(screen, (236,236,236), circleCentre, r)
        r += 3

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        circleCentre = pygame.mouse.get_pos()
        mouseIsDown = True
    elif event.type == pygame.MOUSEBUTTONUP:
        mouseIsDown = False
        circles.append(Circle(circleCentre, r))
