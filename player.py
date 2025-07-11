import pygame
import time
from circleshape import CircleShape, Shot
from constants import *

class Player(CircleShape):

    def __init__(self, x, y, *groups):
        super().__init__(x, y, PLAYER_RADIUS, *groups)
        self.rotation = 0
        self.shot_time = 0.0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_time <= 0:
            shot_position = pygame.Vector2(self.position)
            shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            new_shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS, *Shot.containers)
            new_shot.velocity = shot_velocity
            self.shot_time = PLAYER_SHOOT_COOLDOWN
            return True
        else:
            False

    def update(self, dt):
        if self.shot_time > 0:
            self.shot_time -= dt
            if self.shot_time < 0:
                self.shot_time = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_p]:
            self.shoot()

    

  