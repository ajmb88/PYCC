# High Score filepath and variable
filename = 'Alien_Invasion/High_Score.txt'

# Opens the file and assigns the contents onscreen as high score.
with open(filename, 'r') as high_score_data:
    high_score_number = high_score_data.readline()
    print(high_score_number)

class GameStats:
    """ Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """ Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = int(high_score_number)
        
        # Start Alien Invasion in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """ Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1