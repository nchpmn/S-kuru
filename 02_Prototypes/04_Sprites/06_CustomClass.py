import pygame

class Ball():
    def __init__(self, pos, speed):
        self.position = pos
        self.movement = speed

        self.image = pygame.image.load("Ball1.png")

    def update(self, 
