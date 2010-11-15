# Meta -----------------------------------------------------------------------
import pygame

screen = pygame.display.set_mode((800,600))

running = True
r = 1

# Functions ------------------------------------------------------------------
def paintCircle(pos):
    pygame.draw.circle(screen, (236,236,236), pos, 50)


# Main -----------------------------------------------------------------------
screen.fill((92,92,92)) # Sets BG colour of SURFACE "screen"

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
##    if event.type == pygame.MOUSEBUTTONDOWN:
##        pygame.draw.circle(screen, (236,236,236), pygame.mouse.get_pos(), r)
##        r += 1
##    if event.type != pygame.MOUSEBUTTONDOWN:
##        r = 1
    elif event.type == pygame.MOUSEBUTTONDOWN:
        paintCircle(pygame.mouse.get_pos())

    pygame.display.flip() # Shows drawn frame from buffer
