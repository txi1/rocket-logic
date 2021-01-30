import os
import random
import pygame
import sys
from time import sleep

windowX, windowY = 800,500
display = pygame.Surface((windowX, windowY))
screen = pygame.display.set_mode([windowX, windowY])

class Game():
	
	def __init__(self):
		pygame.init()

		self.running = True
		self.playing = False
		self.UP, self.DOWN, self.START, self.BACK = False, False, False, False

		self.player = rocket()
		
		self.windowX, self.windowY = 800,500
		
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
				print(True)
				self.player.up = True
				self.UP = True
			if(keys[pygame.K_DOWN]):
				self.DOWN = True
			
			if(keys[pygame.K_UP]==False):
				#print(False)
				self.player.up = False
			if(keys[pygame.K_DOWN]==False):
				self.player.down = False

			

	def reset_keys(self):
		self.UP, self.DOWN, self.START, self.BACK = False, False, False, False

	def game_loop(self):
		
		while self.playing:

			self.check_events()
		
			if self.START:
				self.playing = False

			self.player.draw(screen)
			self.player.update()
			screen.blit(display, (0,0))

			pygame.display.update()
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

	def draw(self,surface):
	
		pygame.draw.rect(surface,(0,0,255),(self.x,self.y,self.w,self.h))

	def update(self):
		
		if(self.up):
			self.y -= 4
		if(self.down):
			self.y += 4

	
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


