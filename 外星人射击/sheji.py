import pygame
from pygame.sprite import Sprite
class Bill(Sprite):
    '''一个对飞船所处位置创建子弹'''
    def __init__(self,settings,screen,ship):
        super().__init__()
        self.screen=screen
        #创建子弹，确定位置
        self.rect=pygame.Rect(0,0,settings.bill_width,settings.bill_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=settings.bill_color
        self.bill_speed=settings.bill_speed
    def move(self):
        self.y-=self.bill_speed
        self.rect.y=self.y
    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    
