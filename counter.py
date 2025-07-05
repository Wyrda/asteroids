import pygame


class Counter(pygame.sprite.Sprite):
    def __init__ (self, x, y, font_size, color, *groups):
        super().__init__(*groups)
        self.count = 0
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.position = pygame.Vector2(x, y)
        self.image = None
        self.rect = None
        self.update_image()

    def increment(self, amount=1):
        self.count += amount
        self.update_image()

    def update_image(self):
        self.image = self.font.render(f"Score: {self.count}", True, self.color)
        self.rect = self.image.get_rect(topleft=(self.position.x, self.position.y))

    def draw(self, screen):
        if self.image and self.rect:
            screen.blit(self.image, self.rect)

    def update(self, dt):
        pass