import pygame
# treat all elements like rectangles
# class to manage the ship and have it in the game


class Ship:
    def __init__(self, ai_game):  # reference to instance of AlienInvasion
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen  # assign screen to attribute of ship
        # get method to place ship in right location
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')  # ship given image
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
