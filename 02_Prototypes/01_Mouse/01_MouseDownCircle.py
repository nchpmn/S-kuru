# Meta -----------------------------------------------------------------------
import pygame

screen = pygame.display.set_mode((800,600))

running = True
r = 20
mousedown = 0

# Functions ------------------------------------------------------------------
def paintCircle():
    pygame.draw.circle(screen, (236,236,236), pygame.mouse.get_pos(), r)
##    pygame.gfxdraw.aacircle(screen, pos[0], pos[1], 50, (236,236,236))


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

    if event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = 1
        print "MouseDown"
        
    while mousedown == 1:
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = 0
            print "MouseUp"
        print "Drawing", r
        paintCircle()
        r += 1
    

    pygame.display.flip() # Shows drawn frame from buffer
