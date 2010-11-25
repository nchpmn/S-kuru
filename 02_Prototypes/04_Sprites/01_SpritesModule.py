import pygame

class Box(pygame.sprite.Sprite):
    # All sprite classes should extend pygame.sprite.Sprite. This
    # gives you several important internal methods that you probably
    # don't need or want to write yourself. Even if you do rewrite
    # the internal methods, you should extend Sprite, so things like
    # isinstance(obj, pygame.sprite.Sprite) return true on it.

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
b = Box((255,0,0), (0,0)) # Make a red box in the top left
        
while running:
    screen.blit(b.image, b.rect)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    pygame.display.flip()
