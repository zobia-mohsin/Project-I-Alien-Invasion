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

        # Bullet settings
        # dark gray bullets with a width of 3 pixels and a height of 15 pixels.
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3  # three bullets at a time.

        # Alien settings, update implemented to alien file(fleet moves)
        self.alien_speed = 1.0
