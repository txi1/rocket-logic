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
        #self.player = rocket()
        self.windowX, self.windowY = 800, 500
        self.display = pygame.Surface((self.windowX, self.windowY))
        self.screen = pygame.display.set_mode([self.windowX, self.windowY])
        pygame.display.set_caption("Rocket Logic: Not quite rocket science")


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK = True
                if event.key == pygame.K_UP:
                    self.UP = True
                if event.key == pygame.K_DOWN:
                    self.DOWN = True

    def reset_keys(self):
        self.UP, self.DOWN, self.START, self.BACK = False, False, False, False

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START:
                self.playing = False
            self.screen.fill((255,255,255))		
            #self.player.draw()
            self.screen.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()



class rocket():

	def __init__(self):

		self.x = 20
		self.y = 225

	def draw(self):
		
		pygame.draw.rect(screen,(0,0,255), (self.x,self.y,50,50))

class asteroid():

	def __init__(self):
		
		self.x = 800



start_game = Game()

while start_game.running:
    start_game.playing = True
    start_game.game_loop()