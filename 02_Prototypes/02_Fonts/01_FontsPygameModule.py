import pygame

pygame.font.init()

screen = pygame.display.set_mode((800,600))

running = True

Test = pygame.font.Font(None, 100)

while running:

    pygame.font.Font.render(Test, True, (100,100,100))
    
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    pygame.display.flip() # Shows drawn frame from buffer
