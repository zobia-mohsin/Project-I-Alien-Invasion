import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet.
    Pygame group method to automatically draw the aliens"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width  # top left corner of the screen
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position. (speed)
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right."""
        # update an alien’s position, we move it to the right by alien_speed.
        # We track the alien’s exact position with the self.x attribute
        self.x += self.settings.alien_speed
        # update the position of the alien’s rect by self.x
        self.rect.x = self.x
