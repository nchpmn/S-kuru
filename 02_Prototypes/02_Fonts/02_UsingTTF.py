import pygame

pygame.font.init()

screen = pygame.display.set_mode((800,600))

running = True

powerGrid = pygame.font.Font("PowerGrid.ttf", 100)

while running:
    text = powerGrid.render("Hey, Some Text!", 1, (200,200,200))
    textpos = text.get_rect(centerx=screen.get_width()/2)
    screen.blit(text, textpos)
    
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    pygame.display.flip() # Shows drawn frame from buffer
