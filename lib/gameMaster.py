import pygame
import os
from .UI import UIController
from .UI import Button
from .UI import Text


class GameMaster:
  controls = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f]

  def __init__(self):
    pygame.font.init()
    self.font = pygame.font.Font(None, 30)
    UIController(self.font)
    self.mainMenu()
    EventWatcher.watch()

  @staticmethod
  def quitGame():
    global done
    print("quit game")
    done = True

  def mainMenu(self):
    controller = MainMenuController(self)
    controller.init(self.font)


class EventWatcher:
  eventSubscribers = []
  tickSubscribers = []

  @staticmethod
  def subscribeEvents(subscriber):
    EventWatcher.eventSubscribers.append(subscriber)

  @staticmethod
  def unsubscribeEvents(subscriber):
    EventWatcher.eventSubscribers.remove(subscriber)

  @staticmethod
  def subscribeTicks(subscriber):
    EventWatcher.tickSubscribers.append(subscriber)

  @staticmethod
  def unsubscribeTicks(subscriber):
    EventWatcher.tickSubscribers.remove(subscriber)

  @staticmethod
  def watch():
    global done
    done = False
    while not done:
      for subscriber in EventWatcher.tickSubscribers:
        subscriber.receiveTick()
      UIController.draw()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          GameMaster.quitGame()
        else:
          for subscriber in EventWatcher.eventSubscribers:
            subscriber.receiveEvent(event)
      pygame.display.flip()


class MainMenuController:
  buttons = [
    [30, 100, "Play Game"],
    [30, 200, "Quit"]
  ]

  def __init__(self, gameMaster):
    self.gameMaster = gameMaster

  def init(self, font):
    pygame.mixer.music.load("static/music/Main Reaktor - Recession [NCS Release].mp3")
    pygame.mixer.music.play(-1)
    for button in self.buttons:
      UIController.registerDrawable('main_menu', Button(button[0], button[1], button[2], (0, 0, 0), font))
    EventWatcher.subscribeEvents(self)

  def receiveEvent(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      for button in self.buttons:
        if event.pos[0] >= button[0] and event.pos[0] <= button[0] + 180 and event.pos[1] >= button[1] and event.pos[
          1] <= button[1] + 60:
          # currentColor = 1 if currentColor==0 else 0
          self.selfDestruct()
          if button[2] == "Endless Mode":
            self.gameMaster.playEndless()
          elif button[2] == "Options":
            self.gameMaster.options()
          elif button[2] == "Exit to Desktop":
            GameMaster.quitGame()

  def selfDestruct(self):
    UIController.removeByLabel("main_menu")
    EventWatcher.unsubscribeEvents(self)
