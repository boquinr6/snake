import pygame

from src.Game import Game


def main():
    display = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Anaconda')

    game = Game(display)
    game.loop()

if __name__ == '__main__':
    main()