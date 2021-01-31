import os
import random
import pygame
import sys
import equations
from menu import MainMenu
from menu import InstructionsMenu
from menu import OptionsMenu
from time import sleep

class Game():
    def __init__(self):
		
        pygame.init()
        self.level = 0
        self.checkanswer = True
        self.running = True
        self.playing = False
        self.paused = False
        self.UP, self.DOWN, self.LEFT, self.RIGHT, self.START, self.BACK = False, False, False, False, False, False
        self.player = rocket(self)
        self.rock = asteroid(self)
        self.windowX, self.windowY = 1200, 700
        self.display = pygame.Surface((self.windowX, self.windowY))
        self.screen = pygame.display.set_mode([self.windowX, self.windowY])
        self.font_name = 'fonts/game_over.ttf'
        pygame.display.set_caption("Rocket Logic: Not quite rocket science")
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.instr_menu = InstructionsMenu(self)
        self.curr_menu = self.main_menu
        self.get_new_equation()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.paused = False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if(self.playing == False):
                    if event.key == pygame.K_UP:
                        self.UP = True
                    if event.key == pygame.K_DOWN:
                        self.DOWN = True
                if event.key == pygame.K_RETURN:
                    self.START = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK = True

        if(self.playing):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.UP = True
            if keys[pygame.K_DOWN]:
                self.DOWN = True            


    def reset_keys(self):
        self.UP, self.DOWN, self.LEFT, self.RIGHT, self.START, self.BACK = False, False, False, False, False, False

    def get_new_equation(self):
        self.level += 1
        
        self.equation, self.answer = equations.generate_equation(int(self.level/10)+1)
        print(equations.generate_equation(1),equations.generate_equation(2),equations.generate_equation(3))
        
        answers = ['p','T','F']
        for a in answers:
            if a == self.answer:
               answers.remove(a)
        random_number = random.randint(0,1)

        self.wronganswer = answers[random_number]
        random_number = random.randint(1,2)

        if random_number == 1:
            self.answery = 100
            self.wronganswery = 600
        else:
            self.answery = 600
            self.wronganswery = 100
    

    def game_loop(self):
        while (self.playing and (self.paused == False)):
            
            self.check_events()
            if self.START:
                    self.paused = True
            if self.BACK:
                self.playing = False
            self.display.fill((0,0,0))
            self.player.draw()
            self.player.update()
            self.rock.draw()
            self.rock.update()
            self.draw_text(self.equation, 50, self.windowX/2, 60)
            self.draw_text(self.answer, 50, 850, self.answery)
            self.draw_text(self.wronganswer, 50, 850, self.wronganswery)
            string = f'Score: {self.level-1}'
            self.draw_text(string,50,50,600)
            
            if self.checkanswer == True and self.rock.x <= -1200:
       
                self.checkanswer = False
                if((self.answery > 400 and self.player.y > 400) or (self.answery < 300 and self.player.y < 300)):
                    self.get_new_equation()
                    self.rock.x = 1200
                    self.checkanswer = True

            self.screen.blit(self.display, (0,0))

            pygame.display.update()
            self.reset_keys()
            pygame.time.delay(10)

        while self.paused == True:
            self.check_events()
            if self.START:
                self.paused = False
            if self.BACK:
                self.playing = False
                self.paused = False
            self.draw_text('PAUSED', 240, self.windowX/2, self.windowY/2)
            self.screen.blit(self.display, (0,0))
            

            pygame.display.update()          	

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
        #pygame.draw.rect(self.game.display,(0,0,255),(self.x,self.y,self.w,self.h))
        image = pygame.image.load("images/rocket.png")
        image = pygame.transform.scale(image, (self.w, self.h))
        self.game.display.blit(image, (self.x, self.y))


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
		#pygame.draw.rect(self.game.display,(0,255,255),(self.x,self.y,self.w,self.h))
                image = pygame.image.load("images/image0.png")
                image = pygame.transform.scale(image, (self.w, self.h))
                self.game.display.blit(image, (self.x, self.y))

	def update(self):
		self.x -= 10

start_game = Game()

while start_game.running:
    start_game.curr_menu.display_menu()
    start_game.game_loop()

