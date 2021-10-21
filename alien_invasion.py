from alien import Alien
from bullet import Bullet
from ship import Ship
from settings import Settings  # import settings module created
import pygame
import sys  # importing sys and pygame module
PGE 265


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
        self.aliens = pygame.sprite.Group()  # instance of alien
        self._create_fleet()  # helper method to add fleet of aliens
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
            self._update_bullets()
            self._update_aliens()  # update position of each alien
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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)   # limit 3 at a time
            self.bullets.add(new_bullet)  # add new bullets to bullets

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets. Get rid 
        of bullets that have disappeared of off the screen: We need to 
        detect when the bottom value of a bullet’s rect has a value of 0"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # counting the bullets that leave the screen, print slows downs

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)  # Make an alien by creating one instance of Alien.
        # to know its height and width use attribute size for rect
        alien_width, alien_height = alien.rect.size
        # horizontal space and # of aliens that can fit in that space
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        # avaliable space for rows
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        # The outer loop counts from 0 to the number of rows we want
        for row_number in range(number_rows):
            # The inner loop creates the aliens in one row.
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Each alien is pushed to the right one alien width from the left margin.
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        # we change an alien’s y-coordinate value when it’s not in the first row
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

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

        # to make alien appear on screen, draw
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible, getting rid of previous
        # events and updating according to recent events
        pygame.display.flip()


# only runs if the file is called
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
