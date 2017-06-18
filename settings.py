class Settings():
    #store all settings for Alien Invasion
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 200)
        self.ship_speed_factor = 1.5
        
        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
