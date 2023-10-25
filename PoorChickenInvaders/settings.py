class Settings:
    """A class to store all settings for ALien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1800
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 8  # default 5
        self.ship_limit = 3  # default 3

        # Alien settings
        self.alien_speed_factor = 2  # default 2
        self.fleet_drop_speed = 10  # default 10
        # fleet_direction of 1 represent right / -1 represent left
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed_factor = 8  # default 4
        self.bullet_width = 5  # default 3
        self.bullet_height = 25  # default 15
        self.bullet_color = 65, 65, 65
        self.bullets_allowed = 12  # default 4

        # Scoring
        self.alien_points = 10
