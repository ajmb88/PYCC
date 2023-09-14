class Settings:
    """ A class to stoer and manage all settings for the game."""

    def __init__(self):
        """ Initiatize the games static settings."""
        
        # Screen settings.
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_colour = (100, 190, 240)

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 22
        self.bullet_height = 22
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 4
        
        # Alien settings
        self.fleet_drop_speed = 10.0
        

        # How quickly the games speed increases each level.
        self.ship_speedup_scale = 1.13
        self.bullet_speedup_scale = 1.3
        self.alien_speedup_scale = 1.17

        # Score increase value
        self.score_scale = 1.2

        self._initialize_dynamic_settings()


    def _initialize_dynamic_settings(self):
        """ Initializing the dynamic settings of the game."""
        # Speed settings.
        self.ship_speed = 5.2
        self.bullet_speed = 5.5
        self.alien_speed = 3

        # Direction settings.
        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings.
        self.alien_points = 25

    def _increase_speed(self):
        """ Increase speed setting and alien point value."""
        self.ship_speed *= self.ship_speedup_scale
        self.bullet_speed *= self.bullet_speedup_scale
        self.alien_speed *= self.alien_speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)