import pygame

screen = pygame.display.set_mode((800,600))

running = True
r = 1


while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(screen, (236,236,236), pygame.mouse.get_pos(), r)
        r += 1
    if event.type != pygame.MOUSEBUTTONDOWN:
        r = 1
    screen.fill((92,92,92)) # Sets BG colour of SURFACE "screen"
    pygame.display.flip() # Shows drawn frame from buffer
