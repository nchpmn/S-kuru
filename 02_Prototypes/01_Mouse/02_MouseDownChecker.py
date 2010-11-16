import pygame

screen = pygame.display.set_mode((800,600))

running = True
mouseIsDown = False

while running:
    if mouseIsDown == True:
        print "MouseHeld!", pygame.mouse.get_pos()

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print "MouseDown", pygame.mouse.get_pos()
        mouseIsDown = True
    elif event.type == pygame.MOUSEBUTTONUP:
        print "MouseUp", pygame.mouse.get_pos()
        mouseIsDown = False

    screen.fill((92,92,92))
    pygame.display.flip() # Shows drawn frame from buffer
