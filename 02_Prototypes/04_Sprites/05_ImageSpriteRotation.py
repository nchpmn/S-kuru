import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, speed, rotation):
        pygame.sprite.Sprite.__init__(self)

        self.position = pos
        self.movement = speed
        self.angle = 0
        self.amount = rotation
        
        self.image = pygame.image.load("Ball1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

    def update(self, rect, movement):
        rect[1] += movement
        print position, rect

    def rotate(self, amount):
        self.angle += amount
        self.image
        
    
screen = pygame.display.set_mode((800,600))
balls = []
running = True

for pos, speed, angle in [([0,0], 1, 20),
                   ([100,250], 1, -20),
                   ([375,100], -1, 15)]:
    balls.append(Ball(pos, speed, angle))


while running:
    screen.fill((33,33,33))

    for b in balls:
        b.update(b.rect, b.movement)
        b.rotate(b.rotation)
        screen.blit(b.image, b.rect, b.rotation)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False
        

    pygame.display.flip() # Shows drawn frame from buffer
