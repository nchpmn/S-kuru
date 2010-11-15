import pygame

screen = pygame.display.set_mode((800,600))

running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print "MouseDown", pygame.mouse.get_pos()
    elif event.type == pygame.MOUSEBUTTONUP:
        print "MouseUp", pygame.mouse.get_pos()

    screen.fill((92,92,92))
    pygame.display.flip() # Shows drawn frame from buffer
