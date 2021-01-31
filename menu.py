import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_width, self.mid_height = self.game.windowX/2, self.game.windowY/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("*", 80, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.screen.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()
        
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_width, self.mid_height + 50
        self.instructionsx, self.instructionsy = self.mid_width, self.mid_height + 90
        self.optionsx, self.optionsy = self.mid_width, self.mid_height + 130
        self.creditsx, self.creditsy = self.mid_width, self.mid_height + 170
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty + 14)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            image = pygame.image.load("Images/logo.png")
            image = pygame.transform.scale(image, (400, 300))
            self.game.display.blit(image, (400,0))
            self.game.draw_text("Main Menu", 100, self.mid_width, self.mid_height - 0)
            self.game.draw_text("Start Game", 80, self.startx, self.starty)
            self.game.draw_text("Instructions", 80, self.instructionsx, self.instructionsy)
            self.game.draw_text("Options", 80, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 80, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.instructionsx + self.offset, self.instructionsy + 14)
                self.state = 'Instructions'
            elif self.state == 'Instructions':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy + 14)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy + 14)
                self.state = 'Credits'            
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty + 14)
                self.state = 'Start'                
        if self.game.UP:
            if self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy + 14)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.instructionsx + self.offset, self.instructionsy + 14)
                self.state = 'Instructions'
            elif self.state == 'Instructions':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty + 14)
                self.state = 'Start'
            elif self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy + 14)
                self.state = 'Credits'      

    def check_input(self):
        self.move_cursor()
        if self.game.START:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Instructions':
                self.game.curr_menu = self.game.instr_menu
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options_menu
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits_menu
            self.run_display = False
        if self.game.BACK:
            pygame.quit()

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Volume"
        self.volx, self.voly = self.mid_width, self.mid_height + 50
        self.controlsx, self.controlsy = self.mid_width, self.mid_height + 90
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly + 14)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text("Options", 100, self.mid_width, self.mid_height - 60)
            self.game.draw_text("Volume", 80, self.volx, self.voly)
            self.game.draw_text("Controls", 80, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP or self.game.DOWN:
            if self.state == "Volume":
                self.state = "Controls"
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy + 14)
            else:
                self.state = "Volume"
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly + 14)
        elif self.game.START:
            pass

class InstructionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.positiony = self.mid_height - 120
        self.text = ["General Rules of Logic",
                    "True",
                    "- p v T (Domination Law)",
                    "- p v (not)p (Law excluded Middle)",
                    "- p -> p (Implication)",
                    "- T v F ",
                    "- p v (p v T) (Domination and Idempotent Law)",

                    "False",
                    "- p ^ F (Domination Law)",
                    "- p ^ not(p) (Contradiction)",
                    "- not(p) <-> p (Bijection)",
                    "- T ^ F",
                    "- p ^ (p ^ F) (Domination and Idempotent Law)]"]

    def display_menu(self):
        self.positiony = self.mid_height - 240
        self.game.display.fill((0, 0, 0))
        for line in self.text:
            self.game.draw_text(line, 75, self.mid_width, self.positiony)
            self.positiony += 40
            print(line)
        self.blit_screen()
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.blit_screen()

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.fill((0, 0, 0))
            self.game.draw_text("Made By:", 100, self.mid_width, self.mid_height - 60)
            self.game.draw_text("Taylor Xi", 100, self.mid_width, self.mid_height)
            self.game.draw_text("William Yin", 100, self.mid_width, self.mid_height + 40)
            self.game.draw_text("Eric Gershtein", 100, self.mid_width, self.mid_height + 80)
            self.game.draw_text("Laura Jin", 100, self.mid_width, self.mid_height + 120)
            self.game.check_events()
            if self.game.BACK:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.blit_screen()
