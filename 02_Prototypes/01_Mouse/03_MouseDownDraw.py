import pygame

screen = pygame.display.set_mode((800,600))

running = True
mouseIsDown = False
circleCentre = (0,0)
r = 10


while running:
    screen.fill((92,92,92))
    if mouseIsDown == True:
        print "MouseHeld!", pygame.mouse.get_pos(), circleCentre, r
        pygame.draw.circle(screen, (236,236,236), circleCentre, r)
        r += 1

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
        r = 10

    pygame.display.flip() # Shows drawn frame from buffer
