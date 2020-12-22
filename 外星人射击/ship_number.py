import pygame.font
class Play_numer():
    def __init__(self,settings,screen,msg):
        self.screen=screen
        self.msg=msg
        self.screen_rect=screen.get_rect()
        self.text_color=(255,0,0)
        self.font=pygame.font.SysFont(None,36)
        self.prep_msg()
    def prep_msg(self):
        self.msg_image=self.font.render("ship number: "+str(self.msg),True,self.text_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.y=0
        self.msg_image_rect.x=0
    def draw_button(self):
        self.screen.blit(self.msg_image,self.msg_image_rect)
