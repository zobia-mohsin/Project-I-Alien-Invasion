class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state. TRUE when 3
        # end the game when the player runs out of ships.
        self.game_active = False  # game inactive when it starts
        # High score should never be reset.
        self.high_score = 0

    # to reset some statistics each time the player starts a new game

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1  # level to restart game on
