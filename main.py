# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import (SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        
        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
