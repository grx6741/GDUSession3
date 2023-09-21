import pygame

class Bullet:
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
        self.speed = 1000
        self.size = 10

    def update(self, dt):
        self.pos += self.speed * self.dir * dt

    def show(self, surf):
        pygame.draw.circle(surf, [200, 0, 0], self.pos, 10)
