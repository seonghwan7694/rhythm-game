import sys
import pygame
from pygame.locals import *

FPS = 60
black = (0, 0, 0)
white = (255, 255, 255)
FramePerSec = pygame.time.Clock()
GameDisplay = pygame.display.set_mode((500, 1440))
GameDisplay.fill(white)
pygame.display.set_caption("rhythm-game")


class TextBox:
  def __init__(self, screen, pos):
    self.font = pygame.font.SysFont('Arial', 25)
    self.screen = screen
    self.pos = pos
    pygame.display.update()

  def addRect(self):
    self.rect = pygame.draw.rect(self.screen, black, (175, 75, 200, 100), 2)
    pygame.display.update()

  def addText(self):
    self.screen.blit(self.font.render('Hello!', True, (255, 0, 0)), (200, 100))
    pygame.display.update()


def main_page():
  play_btn = pygame.draw.rect(GameDisplay, black, [0, 0, 30, 30])
  quit_btn = pygame.draw.rect(GameDisplay, black, [50, 50, 30, 30])
  while True:
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if quit_btn.collidepoint(event.pos):
            return 0
          if play_btn.collidepoint(event.pos):
            return 1
      if event.type == pygame.QUIT:
        return 0
    FramePerSec.tick(FPS)


def game_page():
  pygame.mixer.init()
  pygame.mixer.music.load("SIIK & Alenn - Mess [NCS Release].mp3")
  pygame.mixer.music.play()
  while True:
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return None
    FramePerSec.tick(FPS)


if __name__ == '__main__':
  running = True
  pygame.init()
  while running:
    var = main_page()
    if var == 0:
      running = False
    elif var == 1:
      game_page()
      pygame.quit()
      sys.exit()
