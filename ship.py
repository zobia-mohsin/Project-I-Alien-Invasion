import pygame
# treat all elements like rectangles
# class to manage the ship and have it in the game


class Ship:
    def __init__(self, ai_game):  # reference to instance of AlienInvasion
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen  # assign screen to attribute of ship
        # settings attribute for Ship, so we can use it in update()
        self.settings = ai_game.settings
        # get method to place ship in right location
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')  # ship given image
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)  # to accept the decimal speed in ships.py
        # Movement flags
        self.moving_right = False
        self.moving_left = False
    # Moves the ship right if the flaf is true, not a helper method

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect.

        # the value of self.x is adjusted by the amount stored in settings.ship_speed
        # SHIP STOPS MOVING AT EDGES AND in IF CLAUSE
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # NEW IF STATEMENT TO HAVE LEFT AND RIGHT EQUAL PRIORITY
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            # self.rect.x -= 1  # minus one
        # Update rect object from self.x.
        # controls the position of the ship
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
