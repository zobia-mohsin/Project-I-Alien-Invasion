# Project-I-Alien-Invasion
Project I: Alien Invasion using PyGame

    alien_invasion.py: 
    The main file, alien_invasion.py, contains the AlienInvasion class. The main loop of the game, a while loop, is also stored in this module. The while loop calls _check_events(), ship.update(), and _update_screen().

    settings.py:
    The settings.py file contains the Settings class.

    ship.py:
    The ship.py file contains the Ship class. The Ship class has an __init__()
    method, an update() method to manage the ship’s position, and a blitme()
    method to draw the ship to the screen.

    bulltet.py:
    Firing and shooting bullets.

    alien.py:
    Creates all the aliens displayed on the main game screen.

    game_stats.py:
    Keeps track of game levels and score, resets the elements that are supposed
    restart when the game starts again.

    scoreboard.py:
    Keeps track of score when the game is running and remembers the high score.
    Actively compares current score to high score and updates accordingly.

    button.py:
    Creates and draws the play button in the center of the game screen.