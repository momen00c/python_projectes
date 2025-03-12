import sys
from time import sleep
import pygame

from setting import Setting 
from game_state import GameStats
from botton import Botton
from ship import Ship
from bullet import Bullet
from aline import Aline
from scoreboard import Scoreboard

class AlineInvasion:
    def __init__(self):
       pygame.init()
       self.setting=Setting()
       
       self.screen=pygame.display.set_mode((self.setting.screen_width,
                                             self.setting.screen_height))
       pygame.display.set_caption('Aline game')
       self.stats=GameStats(self)
       self.ship=Ship(self)
       self.bullets=pygame.sprite.Group()
       self.alines=pygame.sprite.Group()
       self.stars=pygame.sprite.Group() 
       self.create_fleet()
       self.play_botton= Botton(self,'play')
       self.clock = pygame.time.Clock()
       self.sb = Scoreboard(self)

    def rungame(self):
        while True:   
            self._check_events()
            self.ship.update()
            self.bullets.update()
            if self.stats.game_active:
                self.clock.tick(240)
                
                self._update_alines()
                self.update_bullet()
            self._update_screen()

    def _check_events(self):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                   mouse_pos=pygame.mouse.get_pos()
                   self.check_play_botton(mouse_pos)

                elif event.type==pygame.KEYDOWN:
                    
                    if event.key==pygame.K_RIGHT:
                        self.ship.moving_right=True
                    elif event.key==pygame.K_LEFT:
                        self.ship.moving_lift=True
                    elif event.key==pygame.K_p:
                        self.stats.game_active=True
                    elif event.key==pygame.K_SPACE:
                         self.fire_bullet()
                    elif event.key==pygame.K_q:
                        sys.exit()
                         
                elif event.type==pygame.KEYUP:
                    if event.key==pygame.K_RIGHT:
                        self.ship.moving_right=False
                    if event.key==pygame.K_LEFT:
                        self.ship.moving_lift=False

    def check_play_botton(self,mouse_pos):
        button_click = self.play_botton.rect.collidepoint(mouse_pos)
        if  button_click and not self.stats.game_active:
            self.setting.initialize_dynmic_settings()
            self.stats.reset_setats()
            self.stats.game_active=True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            self.alines.empty()
            self.bullets.empty()
            self.create_fleet()
            self.ship.ship_center()
            pygame.mouse.set_visible(False)
       
    def _update_screen(self):
            self.screen.fill(self.setting.bg_color)
            
            self.ship.blitme()
            
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()     
            self.alines.draw(self.screen)
            self.sb.draw_score()
            if not self.stats.game_active:
                self.play_botton.draw_botton()
             
            pygame.display.flip()

    def update_bullet(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)
      
        self._bullet_aline_collisions()


    def _bullet_aline_collisions(self):
        collisions =pygame.sprite.groupcollide(self.bullets,
                                               self.alines, True, True)
        if collisions:
            for aline in collisions.values():
                self.stats.score += self.setting.aline_point * len(aline)
            self.sb.prep_score()
            self.sb.check_hight_score()

        if not self.alines:
             self.bullets.empty()
             self.create_fleet()
             self.setting._incres_speed()
             #increse_level
             self.stats.level +=1
             self.sb.prep_level()
        
    def fire_bullet(self):
        if len(self.bullets)<self.setting.bullets_allow:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)

    def create_fleet(self):
        aline=Aline(self)
        aline_widht,aline_hight=aline.rect.size
        available_space_x=(self.setting.screen_width-(2*aline_widht))
        number_aline_x=available_space_x//(2*aline_widht)

        ship_hight=self.ship.rect.height
        available_space_y=(self.setting.screen_height-(3*aline_hight)-ship_hight)
        number_rows=available_space_y//(2*aline_widht) 

        for row_number in range(number_rows):
            for alin_number in range(number_aline_x):
                self.create_aline(alin_number,row_number)
    def create_aline(self,alin_number,row_number):
            aline=Aline(self)
            aline_widht,aline_hight = aline.rect.size
            aline.x=aline_widht + 2*aline_widht*alin_number
            aline.rect.x=aline.x
            aline.rect.y=aline_hight + 2 * aline.rect.height * row_number
            self.alines.add(aline)
    
    def _update_alines(self):

        self.check_fleet_edges()
        self.alines.update() 
        if pygame.sprite.spritecollideany(self.ship,self.alines):
            self.ship_hit()
        self.check_aline_bottom()

    def check_fleet_edges(self):
         for aline in self.alines.sprites():
              if aline.check_edges():
                   self.change_fleet_directon()
                   break
    
    def change_fleet_directon(self):
        for aline in self.alines.sprites():
            aline.rect.y+=self.setting.fleet_drop_speed
        self.setting.fleet_direction *=-1
    
    def ship_hit(self):
        if self.stats.ship_left>0:   
            self.stats.ship_left-=1
            self.sb.prep_ships()
            self.alines.empty()
            self.bullets.empty()
            self.create_fleet()
            self.ship.ship_center()
            
            sleep(0.8) 
        else:
            self.alines.empty()
            self.stats.game_active=False
            pygame.mouse.set_visible(True)
    
    def check_aline_bottom(self):
        screen_rect=self.screen.get_rect()
        for aline in self.alines.sprites():
            if aline.rect.bottom>=screen_rect.bottom:
                self.ship_hit()
                break
                
if __name__=='__main__':
    ai=AlineInvasion()
    ai.rungame()