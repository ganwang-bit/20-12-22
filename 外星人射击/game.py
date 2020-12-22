import sys
import pygame
import random
from ship import Ship
from waixingren import Alien
from sheji import Bill
from time import sleep
class GameStats():
    def __init__(self,settings):
        self.settings=settings
        self.game_active=False
        self.reset_stats()
    def reset_stats(self):
        self.ship_number=self.settings.ship_number
def check_down(event,ship,setting,screen,bills):
    if event.key==pygame.K_RIGHT:
        ship.moving_r=True
    if event.key==pygame.K_LEFT:
        ship.moving_l=True
    if event.key==pygame.K_DOWN:
        ship.moving_down=True
    if event.key==pygame.K_UP:
        ship.moving_up=True
    if event.key==pygame.K_SPACE:
        ship.sheji(ship,bills,setting,screen)
    if event.key==pygame.K_q:
        sys.exit()
def check_up(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_r=False
    if event.key==pygame.K_LEFT:
        ship.moving_l=False
    if event.key==pygame.K_DOWN:
        ship.moving_down=False
    if event.key==pygame.K_UP:
        ship.moving_up=False
def check_play(stats,play_button,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.game_active=True
        stats.reset_stats()
def check(ship,setting,screen,bills,stats,play_button):
    #监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_down(event,ship,setting,screen,bills)
        elif event.type==pygame.KEYUP:
            check_up(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play(stats,play_button,mouse_x,mouse_y)
def bill_move(bills,waixingrens):
    for bill in bills.sprites():
        bill.move()
    for bill in bills.copy():
        if bill.rect.bottom<=0:
            bills.remove(bill)
    collisions=pygame.sprite.groupcollide(bills,waixingrens,True,True)
def creat_w(screen,settings,waixingrens):
    flag=0
    if len(waixingrens)<settings.alien_number:
        centerx=random.randint(0,settings.screen_height)      
        for alien in waixingrens.sprites():
            if (centerx<(alien.rect.centerx+alien.rect.width) and centerx>(alien.rect.centerx-alien.rect.width)) or centerx+alien.rect.width/2>800 or centerx-alien.rect.width/2<0:
                flag=1
        if flag!=1:
            new_waixingren=Alien(settings,screen,centerx)
            waixingrens.add(new_waixingren)
def waixingren_move(waixingrens):
    for alien in waixingrens.sprites():
        alien.move()
def fail(waixingrens,ship,stats,bills,settings):
    if pygame.sprite.spritecollideany(ship,waixingrens):
        stats.ship_number-=1
        waixingrens.empty()
        bills.empty()
        ship.center_ship()
        sleep(1)
    for alien in waixingrens.sprites():
        if alien.rect.bottom>=settings.screen_width:
            stats.ship_number-=1
            waixingrens.empty()
            bills.empty()
            ship.center_ship()
            sleep(1)
            break
    if stats.ship_number==0:
        stats.game_active=False
def rescreen(screen_setting,screen,ship,bills,waixingrens,play_button,stats,play_number):
    #每次循环都重绘屏幕
    screen.fill(screen_setting.bg_color)
    ship.biltme()
    for bill in bills.sprites():
        bill.draw()
    for alien in waixingrens.sprites():
        alien.blitme()
    if not stats.game_active:
        play_button.draw_button()
    play_number.draw_button()
    #让最近绘制的屏幕可见
    pygame.display.flip()
