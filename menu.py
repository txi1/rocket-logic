import pygame
pygame.init()

win = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.RESIZABLE)

pygame.display.set_caption("Rocket Logic: Not quite rocket science")

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.draw.rect(win, (255, 0, 0), (50, 50, 50, 50))
  pygame.display.update()