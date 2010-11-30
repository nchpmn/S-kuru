import pygame
import random

# Init -------------------------------------------------------------
screen = pygame.display.set_mode((800,600))
FPSclock = pygame.time.Clock()

# Classes ----------------------------------------------------------
class Circle():
    def __init__(self, kind, pos, circleCentre, r):
        self.radius = r
        self.position = circleCentre
        if kind == 0:
            self.colour = (236,236,236)
        elif kind == 1:
            self.colour = (249,75,75)
        elif kind == 2:
            self.colour = (75,92,249)
        else:
            self.colour = (102,202,67)

    def grow(self, radius, position, colour):
        pygame.draw.circle(screen, colour, position, radius)
        radius += 3

    def update(self, colour, position, radius):
        pygame.draw.circle(screen, colour, position, radius)

# Main -------------------------------------------------------------
running = True
mouseIsDown = False
circleCentre = (0,0)
circles = []
kind = 0

while running:
    FPSclock.tick(60)
    screen.fill((92,92,92))

    for c in circles:
        c.update(c.colour, c.position, c.radius)
        screen.blit(c.colour, c.position, c.radius)

    if mouseIsDown == True:
        pygame.draw.circle(screen, (236,236,236), circleCentre, r)
        r += 3

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        circleCentre = pygame.mouse.get_pos()
        kind = random.randint(0,3)
        mouseIsDown = True
    elif event.type == pygame.MOUSEBUTTONUP:
        mouseIsDown = False
        circles.append(Circle(kind, circleCentre, r))
