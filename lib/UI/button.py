import pygame
from .text import Text


class Button:
  width = 100
  height = 60
  color = (255, 255, 255)

  def __init__(self, posX, posY, text, color, font):
    self.rect = pygame.Rect(posX, posY, self.width, self.height)
    self.text = Text(posX + 15, posY + 20, text, color, font)

  def draw(self, screen):
    pygame.draw.rect(screen, self.color, self.rect)
    self.text.draw(screen)
