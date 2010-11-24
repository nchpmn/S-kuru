import pygame

screen = pygame.display.set_mode((800,600))

running = True
direction = -1
x = 400
y = 400

# Let's load this graphic!
graphic = pygame.image.load("Logo.jpg")


while running:
    screen.blit(graphic, (x,y))

    event = pygame.event.poll()

    y += direction

    if y == 0 or y == 400:
        direction *= -1

    print "X:", x, "\tY:", y

    if event.type == pygame.QUIT:
        running = False
        

    pygame.display.flip() # Shows drawn frame from buffer
