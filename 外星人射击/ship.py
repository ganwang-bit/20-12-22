import pygame
from sheji import Bill
class Ship():

    def __init__(self,setting,screen):
        self.screen=screen
        self.moving_r=False
        self.moving_l=False
        self.moving_up=False
        self.moving_down=False
        self.settings=setting
        #加载飞船
        self.image=pygame.image.load(r'图像\飞机.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #将每艘新飞船放在屏幕底部
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.centery)
    def move(self):
        if self.moving_r and self.rect.right<self.screen_rect.right:
            self.centerx+=self.settings.ship_speed
        if self.moving_l and self.rect.left>0:
            self.centerx-=self.settings.ship_speed
        if self.moving_up and self.rect.top>50:
            self.centery-=self.settings.ship_speed
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.centery+=self.settings.ship_speed
        self.rect.centerx=self.centerx
        self.rect.centery=self.centery
    def sheji(self,ship,bills,settings,screen):
        if len(bills)<=settings.bill_number:
            new_bill=Bill(settings,screen,ship)
            bills.add(new_bill)
    def biltme(self):
        self.screen.blit(self.image,self.rect)    
    def center_ship(self):
        self.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.centery=self.rect.centery
