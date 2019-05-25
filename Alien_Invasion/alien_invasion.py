import sys
import pygame
from ship import Ship

from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(ai_settings,screen)
    # 创造用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    gf.creat_fleet(ai_settings,screen,aliens)
    # alien = Alien(ai_settings,screen)



    # 开始游戏主循环
    while True:
#代码重构
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)



        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        # #print(len(bullets))
        gf.update_screen(ai_settings, screen, ship,aliens,bullets)




run_game()
