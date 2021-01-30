import os
import random
import pygame
import sys
import equations
from menu import MainMenu
from time import sleep

class Game():
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.UP, self.DOWN, self.LEFT, self.RIGHT, self.START, self.BACK = False, False, False, False, False, False
        self.player = rocket(self)
        self.rock = asteroid(self)
        self.windowX, self.windowY = 1200, 700
        self.display = pygame.Surface((self.windowX, self.windowY))
        self.screen = pygame.display.set_mode([self.windowX, self.windowY])
        self.font_name = 'fonts/game_over.ttf'
        pygame.display.set_caption("Rocket Logic: Not quite rocket science")
        self.curr_menu = MainMenu(self)

        equation, result = equations.generate_equation(1)
        self.text = pygame.font.Font('freesansbold.ttf',32).render(equation,True,(0,0,0))
        self.textrect = self.text.get_rect()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.START = True
        if keys[pygame.K_BACKSPACE]:
            self.BACK = True
        if keys[pygame.K_UP]:
            self.UP = True
        if keys[pygame.K_DOWN]:
            self.DOWN = True            


    def reset_keys(self):
        self.UP, self.DOWN, self.LEFT, self.RIGHT, self.START, self.BACK = False, False, False, False, False, False

    def game_loop(self):
        while self.playing:
            #evebt 
            self.screen.blit(self.text,self.textrect)
            self.check_events()
            if self.START:
                self.playing = False
            self.display.fill((0,0,0))
            self.player.draw()
            self.player.update()
            self.rock.draw()
            self.rock.update()
            #self.draw_text('Thanks for Playing', 120, self.windowX/2, self.windowY/2)		
            self.screen.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
            pygame.time.delay(10)

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)



class rocket():
    
    def __init__(self, game):
        self.game = game
        self.x = 20
        self.y = 325
        self.w = 50
        self.h = 50
        self.up = False
        self.down = False

    def draw(self):
        pygame.draw.rect(self.game.display,(0,0,255),(self.x,self.y,self.w,self.h))


    def update(self):
        if(self.game.UP):
            self.y -= 5
        if(self.game.DOWN):
            self.y += 5
              
class asteroid():

	def __init__(self, game):
		self.game = game
		self.x = 1200
		self.y = 300
		self.h = 100
		self.w = 1200

	def draw(self):
		pygame.draw.rect(self.game.display,(0,255,255),(self.x,self.y,self.w,self.h))

	def update(self):
		self.x -= 3

start_game = Game()

while start_game.running:
    start_game.curr_menu.display_menu()
    start_game.game_loop()