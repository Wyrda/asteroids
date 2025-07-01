import pygame


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

