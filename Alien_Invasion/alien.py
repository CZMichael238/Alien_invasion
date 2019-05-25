import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_settings,screen):
        """初始化外星人和其初始位置"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像，并设置其位置
        self.image = pygame.image.load('images/cxk.jpg')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width/10
        self.rect.y = self.rect.height/10

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)