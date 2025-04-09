import pygame

# ------------------------------------------------------------------ #
# This is the simplest file in the project. Simply gets events from
# the user, and then main accsesses the events (and does shit w/ it)
# ------------------------------------------------------------------ #

class EVENTS:
  def __init__(self):
    self.jPress = False
    self.fPress = False
    self.quit = False
    self.wDown = False
    self.aDown = False
    self.sDown = False
    self.dDown = False
    self.move = [False, False, False, False]

    pygame.event.set_blocked(None)
    pygame.event.set_allowed(pygame.KEYDOWN)
    pygame.event.set_allowed(pygame.KEYUP)
    pygame.event.set_allowed(pygame.QUIT)

  def getEvents(self):
    self.jPress = False
    self.fPress = False
    self.quit = False  

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_j:
          self.jPress = True
        elif event.key == pygame.K_f:
          self.fPress = True
        elif event.key == pygame.K_w:
          self.wDown = True
        elif event.key == pygame.K_a:
          self.aDown = True
        elif event.key == pygame.K_s:
          self.sDown = True
        elif event.key == pygame.K_d:
          self.dDown = True
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
          self.wDown = False
        elif event.key == pygame.K_a:
          self.aDown = False
        elif event.key == pygame.K_s:
          self.sDown = False
        elif event.key == pygame.K_d:
          self.dDown = False
      elif event.type == pygame.QUIT:
        self.quit = True

    self.move = [self.wDown, self.aDown, self.sDown, self.dDown]
