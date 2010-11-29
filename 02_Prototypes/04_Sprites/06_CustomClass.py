import pygame

# Classes -------------------------------------------------

class Ball(): # No PyGame sprite this time... let's see if it works!
    def __init__(self, pos, Xspeed, Yspeed):
        self.position = pos
        self.x = Xspeed
        self.y = Yspeed

        self.image = pygame.image.load("Ball1.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

    def update(self, rect, x, y):
        rect[0] += x
        rect[1] += y
        print self.position, rect


# Main ----------------------------------------------------

screen = pygame.display.set_mode((600,400))
balls = []
running = True

FPSclock = pygame.time.Clock() # Limit the FPS

for initialPos, xMove, yMove in [([20,30], 1, 0),
                                 [[45,126], 0, 1],
                                 ([200,85], 2, 1),
                                 ([500,4], 5, 8)]:
    balls.append(Ball(initialPos, xMove, yMove))

while running:
    FPSclock.tick(60) # Set the framerate here
    screen.fill((92,92,92))

    for b in balls:
        b.update(b.rect, b.x, b.y)
        screen.blit(b.image, b.rect)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False

    pygame.display.flip()
