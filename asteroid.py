from circleshape import *
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, *groups):
        super().__init__(x, y, radius, *groups)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt