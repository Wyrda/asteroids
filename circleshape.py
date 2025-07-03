import pygame
from constants import *

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, *groups):
        super().__init__(*groups)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius


    def draw(self, screen):
        # Sub_classes should override
        pass
    def update(self, dt):
        # sub_classes should override
        pass
    def collition(self, other):
        if self.position.distance_to(other.position) < self.radius + other.radius:
            return True
        return False

class Shot(CircleShape):
    def __init__(self, x, y, radius, *groups):
        super().__init__(x, y, radius, *groups)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

