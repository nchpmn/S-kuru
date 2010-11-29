import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        pygame.sprite.Sprite.__init__(self)

        self.position = pos
        self.movement = speed
        
        self.image = pygame.image.load("Ball1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

    def update(self, rect, position, movement):
        rect[1] += movement
        print position, rect
        
    
screen = pygame.display.set_mode((800,600))
balls = []
running = True

for pos, speed in [([0,0], 1),
                   ([100,250], 1),
                   ([375,100], -1)]:
    balls.append(Ball(pos, speed))


while running:
    screen.fill((33,33,33))

    for b in balls:
        b.update(b.rect, b.position, b.movement)
        screen.blit(b.image, b.rect)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False
        

    pygame.display.flip() # Shows drawn frame from buffer
