import sys  # importing sys and pygame module
import pygame

from settings import Settings  # import settings module created
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    '''Overall class to manage game assets and behavior'''

    def __init__(self):
        # initializing the game through the self attribute:
        # background settings that Pygame needs to work properly

        pygame.init()  # "activating the pygame module" so the screen is avalible everywhere
        self.settings = Settings()
        # To run the game in fullscreen mode:
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        # created an instance of ship
        self.ship = Ship(self)
        # instance of bullet
        self.bullets = pygame.sprite.Group()
        # Set the background Color of the pygame
        self.bg_color = (230, 230, 230)
    # REFACTORING, manage events separtely by helper methods _
    # contains an event loop and code that manages screen updates
    '''To update all instances of the GAME as it is running'''

    def run_game(self):  # Main loop of the game starts here
        while True:         # Watch for keyboard and mouse events.
            self._check_events()
            # modify ship’s update()method on each pass through the loop:
            self.ship.update()
            self.bullets.update()

            '''Get rid of bullets that have disappeared of off the screen:
            we need to detect when the bottom value of a bullet’s rect has a value of 0'''
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            # counting the bullets that leave the screen, print slows downs
            # print(len(self.bullets))

            self._update_screen()

    def _check_events(self):  # manage events separate of the game
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # check what key
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    """Respond to keypresses."""

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:  # if right key then
            self.ship.moving_right = True  # TRIE IS RIGHT
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # PRESSING Q TO QUIT
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    """Respond to key releases."""

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        # Move the ship to the right every time key pressed
        # if any other key pressed, "False" movement

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)  # add new bullets to bullets

    def _update_screen(self):  # manage updating screen
        """Update images on the screen, and flip to the new screen."""
        # Redraw and fill the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # draw the ship on the screen
        self.ship.blitme()

        # To draw all fired bullets to the screen,
        # we loop through the sprites in bullets and call draw_bullet() on each one
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible, getting rid of previous
        # events and updating according to recent events
        pygame.display.flip()


# only runs if the file is called
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
