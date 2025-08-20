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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        screen.fill(black)
        player.draw(screen)
        pygame.display.flip() # update display
        dt = clock.tick(60) / 1000 # limit to 60 fps

if __name__ == "__main__":
    main()
