
class Setting:
    def __init__(self):
        self.screen_width=1024
        self.screen_height=800
        self.bg_color=(20,20,20)

      #  self.ship_speed=1
        self.ship_limit=3
        #bulle
       # self.bullet_speed=1.5
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(250,0,0)
        self.bullets_allow=10
        

      #  self.aline_speed=1
        self.fleet_drop_speed=10
        self.fleet_direction=1
        
        #speed_up_game
        self.speedup_scale = 1.1
        
        self.score_scale = 1.5

        self.initialize_dynmic_settings()
    def initialize_dynmic_settings(self):
        self.ship_speed=1.5
        self.bullet_speed=3.0
        self.aline_speed=1.0
        self.fleet_direction=1
        self.aline_point=50

    def _incres_speed(self):
        self.ship_speed *= self.speedup_scale
        self.aline_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.aline_point = int(self.aline_point * self.score_scale)
        print(self.aline_point)