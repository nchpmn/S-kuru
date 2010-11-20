import pygame
import random

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

running = True
mouseIsDown = False
circleCentre = (0,0)
r = 10
circles = []


while running:
    clock.tick(60)
    screen.fill((92,92,92))

    for item in circles:
        pygame.draw.circle(screen, (236,236,236), item[0], item[1])
        
    if mouseIsDown == True:
        print "MouseHeld!", pygame.mouse.get_pos(), circleCentre, r
        pygame.draw.circle(screen, (236,236,236), circleCentre, r)
        r += 3

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    circles.append([(random.randint(0,800),random.randint(0,600)), random.randint(10,75)])

    print "------\n\n\n\nFramerate:", clock.get_fps(), "\n\nCircles:", len(circles)
    
    pygame.display.flip() # Shows drawn frame from buffer
