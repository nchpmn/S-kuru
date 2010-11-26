import pygame

class Box(pygame.sprite.Sprite):
    def __init__(self, color, pos):
        pygame.sprite.Sprite.__init__(self)

        # Create the image that will be displayed and colour it
        self.image = pygame.Surface((50,50))
        self.image.fill(color)

        # Make to top-left the anchor point
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

pygame.init()
running = True
screen = pygame.display.set_mode((800,600))
boxes = []
for color, location in [((225,0,0), (0,0)),
                         ((0,255,0), (0,100)),
                         ((0,0,255), (25,200))]:
    boxes.append(Box(color, location))

while running:
    for b in boxes:
        screen.blit(b.image, b.rect)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    pygame.display.flip()


# http://kai.vm.bytemark.co.uk/~piman/writing/sprite-tutorial.shtml
