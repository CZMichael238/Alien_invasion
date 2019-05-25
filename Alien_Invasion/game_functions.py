import  sys

import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    """响应 按键和鼠标操作"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #控制连续移动
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings, screen, ship,alien,bullets):
    # 每次循环重绘屏幕
    # screen.fill(ai_settings.bg_color)
    # 显示背景图片
    background = pygame.image.load('images/space.jpg').convert()

    screen.blit(background, (0, 0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示飞船
    ship.blitme()
    # alien.blitme()
    alien.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    #更新子弹的位置
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
def creat_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen )
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width
    number_aliens_x = int(available_space_x/alien_width)

    for alien_number in range (number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x =  alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
