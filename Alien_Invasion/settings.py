class Settings():

    def __init__(self):

        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (2, 126, 243)

        # 飞船设置
        self.ship_speed_factor = 2

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 30