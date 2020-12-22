import pygame
from pygame.sprite import Sprite
import random
class Alien(Sprite):
    def __init__(self,settings,screen,centerx):
        super().__init__()
        self.screen=screen
        self.settings=settings
        self.image=pygame.image.load('图像/外星人.bmp')
        self.rect=self.image.get_rect()
        self.rect.centerx=centerx
        self.rect.y=50
        self.y=float(self.rect.y)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def move(self):
        self.y+=self.settings.alien_speed
        self.rect.y=self.y
