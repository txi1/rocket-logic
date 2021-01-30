import os
import random
import pygame
import sys
from time import sleep


pygame.init
windowX = 800
windowY = 500

screen = pygame.display.set_mode([windowX,windowY])

def main():
	running = True
	player = rocket()
	while running:
		screen.fill((255,255,255))	
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		player.draw()
		pygame.display.update()
		
class rocket():

	def __init__(self):

		self.x = 20
		self.y = 225

	def draw(self):
		
		pygame.draw.rect(screen,(0,0,255), (self.x,self.y,50,50))

class asteroid():

	def __init__(self):
		
		self.x = 800



main()