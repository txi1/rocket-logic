import pygame

class game():
  def __init__ (self):
    pygame.init()
    self.running, self.playing = True, False
    self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    self.win = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.RESIZABLE)
    pygame.display.set_caption("Rocket Logic: Not quite rocket science")
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False

      pygame.draw.rect(win, (255, 0, 0), (50, 50, 50, 50))
      pygame.display.update()

class Menu():
  def __init__(self, game):
    self.game = game
    self.mid_height, self.mid_width = self.game.WindowX/2, self.game.WindowY/2
    self.run_display = True
    self.cursor_rect = pygame.Rect(0, 0, 20, 20)
    self.offset = -100

  def draw_cursor():
    self.game.