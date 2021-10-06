import sys
import pygame


class AlienInvasion:
    '''Overall class to manage game assets and behavior'''

    def __init__(self):  # initializing the game through the self attribute
        pygame.init()  # "activating the pygame module"

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):  # Main loop of the game starts here
        while True:         # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
