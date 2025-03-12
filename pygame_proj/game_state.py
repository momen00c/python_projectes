class GameStats:
    def __init__(self,ai_game):
        self.setting=ai_game.setting
        self.reset_setats()
        self.game_active=False
        self.high_score=0
    def reset_setats(self):
        self.ship_left=self.setting.ship_limit
        self.score=0
        self.level=0