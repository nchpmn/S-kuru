import pygame

class UpDownBox(pygame.sprite.Sprite):
    def __init__(self, color, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.down = True # Let's start it by going downwards
        self.next_update_time = 0 # No update() yet

    def update(self, current_time, bottom):
        if self.next_update_time < current_time:
            # At the bottom of the screen, swap direction
            if self.rect.bottom == bottom - 1:
                self.going_down = False
            elif self.rect.top == 0:
                self.going_down = True

            # Move up or down by one pixel
            if self.going_down:
                self.rect.top += 1
            else:
                self.rect.top -= 1

            self.next_update_time = current_time + 10

pygame.init()
running = True
screen = pygame.display.set_mode((800,600))
boxes = []
for color, location in [((225,0,0), (0,0)),
                         ((0,255,0), (100,100)),
                         ((0,0,255), (250,200))]:
    boxes.append(UpDownBox(color, location))

while running:
    for b in boxes:
        screen.blit(b.image, b.rect)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    pygame.display.flip()


# http://kai.vm.bytemark.co.uk/~piman/writing/sprite-tutorial.shtml
