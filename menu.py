import pygame

class Menu():
  def __init__(self, game):
    self.game = game
    self.mid_height, self.mid_width = self.game.WindowX/2, self.game.WindowY/2
    self.run_display = True
    self.cursor_rect = pygame.Rect(0, 0, 20, 20)
    self.offset = -100

  def draw_cursor():
    self.game.