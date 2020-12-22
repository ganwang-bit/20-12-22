import game
import pygame
from Setting import settings
from ship import Ship
from pygame.sprite import Group
from game import GameStats
from button import Button
from ship_number import Play_numer
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    screen_setting=settings()
    screen=pygame.display.set_mode((screen_setting.screen_height,screen_setting.screen_width))
    pygame.display.set_caption("外星人射击")
    ship = Ship(screen_setting,screen)
    stats=GameStats(screen_setting)
    bills=Group()
    waixingrens=Group()
    play_button=Button(screen_setting,screen,"play")
    play_number=Play_numer(screen_setting,screen,stats.ship_number)
    #开始游戏的主循环
    while True:
        game.check(ship,screen_setting,screen,bills,stats,play_button)
        play_number.msg=stats.ship_number
        play_number.prep_msg()
        if stats.game_active:
            ship.move()
            game.creat_w(screen,screen_setting,waixingrens)
            game.bill_move(bills,waixingrens)
            game.waixingren_move(waixingrens)
            game.fail(waixingrens,ship,stats,bills,screen_setting)
        game.rescreen(screen_setting,screen,ship,bills,waixingrens,play_button,stats,play_number)
run_game()
