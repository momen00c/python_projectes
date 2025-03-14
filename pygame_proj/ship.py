import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting=ai_game.setting

        self.image = pygame.image.load('images/ship.png')  # تأكد من أن المسار صحيح
        self.image=pygame.transform.scale(self.image,(80,80))
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom

        self.x=float(self.rect.x)

        self.moving_right=False
        self.moving_lift=False
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x +=self.setting.ship_speed
        if self.moving_lift and self.rect.left > 0:
            self.x-=self.setting.ship_speed
        self.rect.x = self.x
    def ship_center(self):
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)