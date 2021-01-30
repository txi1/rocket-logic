import os
import random
import pygame
import sys
from time import sleep

class Game():
    
    def __init__(self):
        pygame.init()

        self.running = True
        self.playing = False
        self.UP, self.DOWN, self.START, self.BACK = False, False, False, False
        
        self.player = rocket()
        
        self.windowX, self.windowY = 800,500

        self.display = pygame.Surface((self.windowX, self.windowY))
        self.screen = pygame.display.set_mode([self.windowX, self.windowY])
        self.font_name = 'Minecrafter.ttf'

        pygame.display.set_caption("Rocket Logic: Not quite rocket science")

    def check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False

            keys = pygame.key.get_pressed()
            if(keys[pygame.K_RETURN]):
                self.START = True
            if(keys[pygame.K_BACKSPACE]):
                self.BACK = True
            if(keys[pygame.K_UP]):
                self.player.up = True
                #self.UP = True
            if(keys[pygame.K_DOWN]):
                self.DOWN = True
            
            """if(keys[pygame.K_UP]==False):
                print(False)
                self.player.up = False
            if(keys[pygame.K_DOWN]==False):
                self.player.down = False"""

            

    def reset_keys(self):
        self.UP, self.DOWN, self.START, self.BACK = False, False, False, False

    def game_loop(self):
        
        while self.playing:

            #evebt
            self.check_events()
        
            if self.START:
                self.playing = False
            
            #update
            self.player.update()

            #render
            self.player.draw(self.screen)
            #self.screen.blit(self.display, (0,0))

            
            #self.reset_keys()

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font,size)
        text_surface = font.render(text,True,(0,0,0))
        text_rect = text_surface.get_rect()
        text.rect.center = (x,y)
        self.display.blit(text_surface, text_rect)

class rocket():
    
    def __init__(self):

        self.x = 20
        self.y = 225
        self.w = 50
        self.h = 50
        self.up = False
        self.down = False

    def draw(self,screen):
        counter = 0
        if (counter % 2 == 0):
            pygame.draw.rect(screen,(0,0,255),(self.x,self.y,self.w,self.h))
            counter+=1
        else:
            pygame.draw.rect(screen,(255,0,0),(self.x,self.y,self.w,self.h))
            counter+=1
        pygame.display.update()
        return


    def update(self):
        
        if(self.up):
            self.y -= 4
            self.up = False
        if(self.down):
            self.y += 4
            self.down = False
        return

    
class asteroid():

    def __init__(self):
        self.x = 800
        self.y = 200
        self.h = 100
        self.w = 800

    def draw(self,screen):
        
        pygame.draw.rect(screen,(0,0,255),(self.x,self.y,self.w,self.h))

start_game = Game()
while start_game.running:
    start_game.playing = True
    start_game.game_loop()


