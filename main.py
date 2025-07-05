import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from circleshape import CircleShape, Shot
from asteroidfield import AsteroidField
from counter import Counter

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()
#asteroidfield = pygame.sprite.Group()

CircleShape.containers = (updatable, drawable)
Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable,)
Shot.containers = (updatable, drawable, bullets)

game_score_counter = None

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pygame.font.init()

    global game_score_counter
    game_score_counter = Counter(10, 10, 36, (255, 255, 255), updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, updatable, drawable)
    field = AsteroidField(updatable, drawable, asteroids)
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

        for asteroid in asteroids:
            if player.collition(asteroid):
                print("Game Over!")
                running =False
                break
        
        for bullet in bullets:
            for asteroid in asteroids:
                if bullet.collition(asteroid):
                    print("Asteroid hit!")
                    bullet.kill()
                    asteroid.split()
                    if game_score_counter:
                        game_score_counter.increment()
                    break

        pygame.display.flip()

        


    pygame.quit()


if __name__ == "__main__":
    main()
