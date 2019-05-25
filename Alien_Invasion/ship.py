import pygame

class Ship():
    def __init__(self,ai_settings,screen):

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/banana.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        #把每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerX = float(self.rect.centerx)
        self.centerY = self.rect.centery
    #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):

    #更新飞船center值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerX += self.ai_settings.ship_speed_factor
            #self.rect.centerx +=1
        if self.moving_left and self.rect.left > 0 :
            self.centerX -= self.ai_settings.ship_speed_factor
            #self.rect.centerx -=1
        if self.moving_up and self.rect.top > 0 :
            self.centerY -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centerY += self.ai_settings.ship_speed_factor
    #更新飞船rect值
        self.rect.centerx = self.centerX
        self.rect.centery = self.centerY
    def blitme(self):

        self.screen.blit(self.image,self.rect)