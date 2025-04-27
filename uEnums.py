import pygame

# ------------------------------------------------------------------ #
# this file contains global constants (enums) that other files may 
# acssess, but no file should modify the variables contained
# ------------------------------------------------------------------ #

class COLORS:
  def __init__(self):
    self.transPlayer = (245, 169, 183)
    self.eggPlayer = (167, 187, 216)
    self.cisPlayer = (90, 205, 250)
    self.playArea = (30, 30, 30)
    self.textboxBorder = (128, 128, 128)
    self.textboxInner = (30, 30, 30)
    self.text = (230, 230, 230)
    self.screenBorder = (0, 0, 0)
    self.door = (90, 60, 40)
    self.doorknob = (255, 225, 25)
    self.lockedDoor = (70, 70, 70)
    self.lockedDoorKnob = (70, 70, 70)
    self.mom = (200, 100, 20)
    self.dad = (200, 20, 50)
    self.miscPerson = (20, 200, 150)

class DIMENSIONS:
  def __init__(self):
    self.wScreen = 800
    self.hScreen = 600
    self.wPlayer = 30
    self.hPlayer = 40
    self.wBorder = 20
    self.hBorder = 20
    self.hTextbox = 180
    self.textboxBorder = 5
    self.hTextSpacer = 5
    self.vTextSpacer = 5
    self.hDoor = 75
    self.wDoor = 50
    self.doorknob = 9
    self.hubDoorHeight = 50
    self.hubDoorSpacing = 40
    self.otherDoorHeight = 285
  
"""
DOCUMENTING RUSHED CODE:

- the order of items in uAssets must reflect the numerical
  ordering present in this, or wrongwarps will happen
"""

class DESTINATIONS:
  def __init__(self):
    self.none = -1
    self.hub = 0
    self.r1a = 1
    self.r1b = 2
    self.r2 = 3
    self.r3 = 4
    self.r4 = 5
    self.r5 = 6
    self.r6 = 7
    self.r7 = 8
    self.r8 = 9

class MISC:
  def __init__(self):
    self.norm = pygame.font.Font("files/fonts/PixelOperator.ttf", 36)
    self.bold = pygame.font.Font("files/fonts/PixelOperator-Bold.ttf", 36)
    self.lockedText = "It's locked"