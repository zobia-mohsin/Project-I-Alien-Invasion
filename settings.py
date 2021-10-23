class Settings:
    '''A class to store all settings for Alien Invasion. Modification easier'''

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings (SPEED)
        self.ship_speed = 1.5  # deciaml so make modificatin to int of ship.py
        self.ship_limit = 3  # the number of ships the player starts with.

        # Bullet settings
        # dark gray bullets with a width of 3 pixels and a height of 15 pixels.
        self.bullet_speed = 1.75
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3  # three bullets at a time.

        # Alien settings, update implemented to alien file(fleet moves)
        self.alien_speed = 1.0
        # fleet move down the screen and to the left
        # when it hits the right edge of the screen.
        self.fleet_drop_speed = 10  # how quickly fleet drops

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    # method sets the initial values for the ship, bullet, and alien speeds
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring for shooting down each alien
        self.alien_points = 50

    # To increase speed of each element in each level
    def increase_speed(self):
        """Increase speed settings:multiplying by speedup_scale.
        Increase alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        # increase the point value by integers of each hit
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
