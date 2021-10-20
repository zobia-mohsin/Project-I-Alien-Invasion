import sys  # importing sys and pygame module
import pygame

from settings import Settings  # import settings module created
from ship import Ship


class AlienInvasion:
    '''Overall class to manage game assets and behavior'''

    def __init__(self):  # initializing the game through the self attribute: background settings that Pygame needs to work properly
        pygame.init()  # "activating the pygame module" so the screen is avalible everywhere
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # creates display window of game

        pygame.display.set_caption("Alien Invasion")
        # created an instance of ship
        self.ship = Ship(self)
        # Set the background Color of the pygame
        self.bg_color = (230, 230, 230)

    # contains an event loop and code that manages screen updates
    def run_game(self):  # Main loop of the game starts here
        while True:         # Watch for keyboard and mouse events.
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # check what key
                if event.key == pygame.K_RIGHT:  # if right key then
                    # Move the ship to the right.
                    self.ship.rect.x += 1  # pg238

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw and fill the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # draw the ship on the screen
        self.ship.blitme()
        # Make the most recently drawn screen visible, getting rid of previous
        # events and updating according to recent events
        pygame.display.flip()


# only runs if the file is called
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
