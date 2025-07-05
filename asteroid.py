from circleshape import *
import random
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, *groups):
        super().__init__(x, y, radius, *groups)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)
            p_rotation = self.velocity.rotate(random_angle)
            n_rotation = self.velocity.rotate(-random_angle)
            new_asteroid_p = Asteroid(self.position.x, self.position.y, self.new_radius, *Asteroid.containers)
            new_asteroid_n = Asteroid(self.position.x, self.position.y, self.new_radius, *Asteroid.containers)
            new_asteroid_p.velocity = p_rotation * 1.2
            new_asteroid_n.velocity = n_rotation * 1.2


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt