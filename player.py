import pygame
from pygame import Vector2
from math import atan2

class Player:
    def __init__(self, pos):
        self.pos = pos
        self.speed = 300
        self.surface = pygame.Surface((50, 50))
        self.surface.fill((100, 200, 50))
        self.rect = self.surface.get_rect()

    def update(self):
        self.rect.centerx = int(self.pos.x)
        self.rect.centery = int(self.pos.y)

    def show(self, surf):
        surf.blit(self.surface, self.rect)

    def move_left(self, dt):
        self.pos.x -= self.speed * dt

    def move_right(self, dt):
        self.pos.x += self.speed * dt

    def move_up(self, dt):
        self.pos.y -= self.speed * dt

    def move_down(self, dt):
        self.pos.y += self.speed * dt

    def get_mouse_angle(self):
        mvec = Vector2(pygame.mouse.get_pos())
        return (mvec - self.pos).angle_to(Vector2(1, 0))
