import pygame
from pygame.sprite import Sprite
class Aline(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.setting=ai_game.setting

        self.image=pygame.image.load('images/vf.png')
        self.image=pygame.transform.scale(self.image,(90,90))
        self.rect=self.image.get_rect()
        #start each aline top the corner left
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        
        self.x=float(self.rect.x)

    def check_edges(self):
        screen_rect=self.screen.get_rect()

        if self.rect.right>=screen_rect.right or self.rect.left<=0:
            return True

    def update(self):
        self.x+=(self.setting.aline_speed*
                 self.setting.fleet_direction)
        self.rect.x=self.x
        