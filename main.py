from pygame.display import update
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
import pygame

def main():
    # initializing pygame
    pygame.init()
    # screen
    black = (0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # setting clock for fps
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill(black)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() # update display
        dt = clock.tick(60) / 1000 # limit to 60 fps

if __name__ == "__main__":
    main()
