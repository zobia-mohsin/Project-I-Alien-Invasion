import pygame
import sys  # importing sys and pygame module
from alien import Alien
from bullet import Bullet
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from settings import Settings  # import settings module created
from time import sleep  # pause the game when ship is hit


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

        # Create an instance to store game statistics
        # and create a scoreboard
        self.stats = GameStats(self)  # after creating the game window
        self.sb = Scoreboard(self)

        # created an instance of ship
        self.ship = Ship(self)

        # instance of bullet
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()  # instance of alien
        self._create_fleet()  # helper method to add fleet of aliens
        # Set the background Color of the pygame
        self.bg_color = (230, 230, 230)
        # Make the Play button,INIT: we only need one play button
        self.play_button = Button(self, "Play")
    # REFACTORING, manage events separtely by helper methods _
    # contains an event loop and code that manages screen updates
    '''To update all instances of the GAME as it is running'''

    def run_game(self):  # Main loop of the game starts here
        while True:         # Watch for keyboard and mouse events.

            self._check_events()  # always have to check, q button, updating screen

            # check these events when game is active, game elements
            # modify ship’s update()method on each pass through the loop:
            if self.stats.game_active:
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
            # To monitor mouse events over the play button ONLY
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play. To check 
        whether the point of the mouse click overlaps the 
        region defined by the Play button’s rect"""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # the game will only start if the play button
        # is clicked and game is not currently active
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()

            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()  # start with zero score
            self.sb.prep_level()
            self.sb.prep_ships()  # how many ships left in game

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            # evertime you press the play button
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor false to set_visible
            pygame.mouse.set_visible(False)
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
        # counting the bullets that leave the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                # then alien’s value is added to the score
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            # increase the game’s tempo by calling increase_speed()
            self.settings.increase_speed()
            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

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

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        # call check_edges() on each alien, if TRUE fleet needs to drop
        for alien in self.aliens.sprites():
            # TRUE then change FLEET direction and break from loop
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        # loop thorugh all the aliens and dropeach alien once if touch edge
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        # not in loop because only want to drop fleet ONCE
        self.settings.fleet_direction *= -1

    # to check if alien hits bottom of screen, respond same way
    # as if hit ship
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()  # call ship_hit if hits bottom
                break

    # to manage the movement of the fleet
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        """Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        # Look for alien-ship collisions. No collisions-->NONE returned
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()  # replace print statement
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        # if player has atleast one ship left based on ship count then:
        if self.stats.ships_left > 0:

            # Decrement ships_left by one after alien hits ship
            # and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause afte updates but before changes execute for .5 seconds
            sleep(0.5)
        # if player has no ships left, FALSE, game not active, game ends
        else:
            self.stats.game_active = False
            # cursor visible again as soon as the game becomes inactive
            pygame.mouse.set_visible(True)

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

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        '''Button drawn after all elements and before the
        screen updates so it appears on top of elements in
        (if block) inactive mode of the game'''
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible, getting rid of previous
        # events and updating according to recent events
        pygame.display.flip()


# only runs if the file is called
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
