import pygame

class game()
  def __init__ (self)
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