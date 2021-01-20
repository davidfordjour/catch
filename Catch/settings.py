class Settings():
    """A class to store all settings for Catch."""

    def __init__(self):
        """Initialise the game's settings."""
        self.screen_width = 1200    # Screen settings
        self.screen_height = 800
        self.bg_colour = (230,230,230)
        self.hand_speed_factor = 10    # Hand settings

        self.ball_drop_factor = 10    # Ball settings
        self.ball_limit = 3
