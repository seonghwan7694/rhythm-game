import sys
import pygame
from pygame.locals import *

pygame.init()
FPS = 60
black = (0, 0, 0)
white = (255, 255, 255)
FramePerSec = pygame.time.Clock()
GameDisplay = pygame.display.set_mode((500, 1440))
GameDisplay.fill(white)
pygame.display.set_caption("rhythm-game")
music = pygame.mixer.Sound("SIIK & Alenn - Mess [NCS Release].mp3")


def main_page():
  area = pygame.draw.rect(GameDisplay, black, [0, 0, 30, 30])
  while True:
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if area.collidepoint(event.pos):
            print("클릭됨.")
      if event.type == pygame.QUIT:
        return None
    FramePerSec.tick(FPS)


if __name__ == '__main__':
  pygame.init()
  main_page()

  pygame.quit()
  sys.exit()

"""
while True:
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  FramePerSec.tick(FPS)
"""
