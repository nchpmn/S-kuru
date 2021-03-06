import pygame

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
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print "MouseDown", pygame.mouse.get_pos()
        circleCentre = pygame.mouse.get_pos()
        mouseIsDown = True
    elif event.type == pygame.MOUSEBUTTONUP:
        print "MouseUp", pygame.mouse.get_pos()
        mouseIsDown = False
        circles.append([circleCentre, r])
        r = 10

    print "------\n\n\n\nFramerate:", clock.get_fps(), "\n\nCircles:", len(circles)

    pygame.display.flip() # Shows drawn frame from buffer
