import pygame

screen = pygame.display.set_mode((800,600))

running = True

# Let's load this graphic!
graphic = pygame.image.load("Logo.jpg")

screen.fill((
screen.blit(graphic, (0,0))

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    pygame.display.flip() # Shows drawn frame from buffer
