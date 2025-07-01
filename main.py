import pygame
from constants import *
from player import Player
from circleshape import CircleShape

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    CircleShape.containers = (updatable, drawable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, updatable, drawable)

    dt = 0
    clock = pygame.time.Clock()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000.0

        screen.fill("black")

        for object in drawable:
            object.draw(screen)
        updatable.update(dt)

        pygame.display.flip()

        


    pygame.quit()


if __name__ == "__main__":
    main()
