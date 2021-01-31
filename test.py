import os
import random
import pygame
import sys
from time import sleep


pygame.init
windowX = 800
windowY = 500
speed = 0.5


screen = pygame.display.set_mode([windowX,windowY])
background = pygame.image.load("images/background.png")


def main():
	running = True
	player = rocket()
	rock = asteroid()
	while running:
		screen.fill((0,0,0))	
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			keys = pygame.key.get_pressed()
			if(keys[pygame.K_UP]):
				player.moveUp = True
			if(keys[pygame.K_DOWN]):
				player.moveDown = True
			if(keys[pygame.K_SPACE]):
				rock.stopMoving = True

			if(keys[pygame.K_UP]==False):
				player.moveUp = False
			if(keys[pygame.K_DOWN]==False):
				player.moveDown = False
			if(keys[pygame.K_SPACE]==False):
				rock.stopMoving = False


		if(player.x + player.w > rock.x and player.x < rock.x + rock.w and player.y + player.h > rock. y and player.y < rock.y + rock.h):
			rock.collided = True
			player.collided = True
			print("collision occured!")

		screen.blit(background, (0, 0))
		player.update()
		player.draw()
		rock.update()
		rock.draw()
		
		

		pygame.time.delay(8)

		pygame.display.update()
		
		
class rocket():
	def __init__(self):
		self.x = 20
		self.y = 225
		self.h = 50
		self.w = 50
		self.moveUp = False
		self.moveDown = False
		self.collided = False

	def draw(self):
		image = pygame.image.load("images/rocket.png")
		image = pygame.transform.scale(image, (self.w, self.h))
		screen.blit(image, (self.x, self.y))
		#pygame.draw.rect(screen,(0,0,255),(self.x,self.y,self.w,self.h))

	def update(self):
		if (self.collided == True):
			self.moveUp = False
			self.moveDown = False
		elif self.moveUp:
			self.y -= 5
		elif self.moveDown:
			self.y += 5

	

class asteroid():

	def __init__(self):
		self.x = 800
		self.y = 200
		self.h = 100
		self.w = 800
		self.collided = False

	def draw(self):
		image = pygame.image.load("images/image0.png")
		image = pygame.transform.scale(image, (self.w, self.h))
		screen.blit(image, (self.x, self.y))
		#pygame.draw.rect(screen,(0,255,255),(self.x,self.y,self.w,self.h))

	def update(self):
		if(self.collided == False):
			self.x -= 3
		
		if (self.x == -1000):
			self.x = 800
		





main()