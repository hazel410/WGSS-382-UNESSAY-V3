import numpy
import asyncio
import pygame

pygame.init() # needs to be called before uEnums/uDisplay

import uEnums
import uDisplay
import uInput
import uAssets
import uEntities
import uConf

class MAIN():
  def __init__(self):
    # pygame inits
    self.DIMENSIONS = uEnums.DIMENSIONS()
    if uConf.RUNNING_LOCALLY:
      self.screen = pygame.display.set_mode([self.DIMENSIONS.wScreen, self.DIMENSIONS.hScreen],flags=pygame.SCALED)
    else:
      self.screen = pygame.display.set_mode([self.DIMENSIONS.wScreen, self.DIMENSIONS.hScreen])
    self.clock = pygame.time.Clock()
    pygame.display.set_caption("WGSS382 UNESSAY: Untitled")
    
    # grabbing classes from other files
    self.dauber = uDisplay.DAUBER(self.screen)
    self.textbox = uDisplay.TEXTBOX(self.screen)
    self.player = uEntities.PLAYER()
    self.events = uInput.EVENTS()
    self.dests = uEnums.DESTINATIONS()

    # important loop vars
    self.target = self.dests.none
    self.gameState = 2
    self.objects = []
    self.doors = []
    self.hubUnlocks = 8
    self.activeScreen = self.dests.hub
    self.interactedStoryObjects = []

    # dynamic loop vars
    self.quit = False
    self.jPress = False
    self.fPress = False
    self.movement = [False, False, False, False]
    self.keyIter = 0
    
    asyncio.run(self.main())

  async def main(self):
    while True:

      # grabbing events
      self.events.getEvents()
      self.quit = self.events.quit
      self.jPress = self.events.jPress
      self.fPress = self.events.fPress
      self.movement = self.events.move

      # handling game state
      if self.gameState == 0:
        self.handleTextboxState()
      elif self.gameState == 1:
        self.handleWalkingState()
      elif self.gameState == 2:
        self.handleTransitionState()
      
      self.handleDrawing()
      
      if self.fPress:
        pygame.display.toggle_fullscreen()
      if self.quit:
        return
      pygame.display.flip()
      self.clock.tick(60)
      
      await asyncio.sleep(0)
  
  def handleTextboxState(self):
    if self.gameState == 0:
      if self.jPress:
        self.textbox.advanceText()
      if not self.textbox.displayTrue:
        if self.target == self.dests.none:
          self.gameState = 1
        else:
          self.gameState = 2
          self.activeScreen = self.target

  def handleWalkingState(self):
    
    self.player.applyVelocity(self.movement)
    self.player.snapBorder()
    
    for object in self.objects:
      if self.player.detectObjectCollision(object.neswEdges):
        self.player.fixObjectCollision(object.rect, object.angles, object.center)
      if self.player.isTouchingObject(object.neswEdges):
        object.touchingPlayer = True
      else:
        object.touchingPlayer = False
      # if player interacts with interactable object
      if object.touchingPlayer and self.jPress and object.text != "":
        self.gameState = 0
        object.interacted = True
        # if object is story related and first time interacting
        if object.storyRelated and not object.text in self.interactedStoryObjects:
          self.hubUnlocks += 1
          self.interactedStoryObjects.append(object.text)
        self.textbox.applyText(object.text)
    
    for door in self.doors:
      if self.player.detectObjectCollision(door.neswEdges):
        self.player.fixObjectCollision(door.rect, door.angles, door.center)
      if self.player.isTouchingObject(door.neswEdges):
        door.touchingPlayer = True
      else:
        door.touchingPlayer = False
      if door.touchingPlayer and self.jPress:
        if door.currentTarget == self.dests.none:
          self.gameState = 0
          self.textbox.applyText(door.dispText)
        else:
          self.target = door.currentTarget
          self.textbox.applyText(door.dispText)
          self.gameState = 0
    
  def handleTransitionState(self):
    self.keyIter = 0
    self.doors = []
    self.objects = []
    for doorInfo in uAssets.doors[self.activeScreen]:
      currentDoor = uEntities.DOOR(doorInfo[0], doorInfo[1], doorInfo[2])
      if self.activeScreen == self.dests.hub:
        # this if prevents fuckery on game start
        if self.target != self.dests.none:
          self.player.setMiddle()
        if self.keyIter < self.hubUnlocks:
          currentDoor.unlock()
        self.keyIter += 1
      else:
        self.player.setMiddle()
        currentDoor.unlock()
      self.doors.append(currentDoor)
    for objectInfo in uAssets.objects[self.activeScreen]:
      if objectInfo[2].find("STRY: ") == 0:
        self.objects.append(uEntities.OBJECT(objectInfo[0], objectInfo[1], (objectInfo[2])[6:]))
        self.objects[-1].storyRelated = True
      else:
        self.objects.append(uEntities.OBJECT(objectInfo[0], objectInfo[1], objectInfo[2]))
    self.gameState = 1
    self.target = self.dests.none
    
  def handleDrawing(self):
    self.dauber.drawPlayArea()
    self.dauber.drawBorder()
    self.dauber.drawEntity(self.player.rect, self.player.color)
    for object in self.objects:
      self.dauber.drawEntity(object.rect, object.color)
    for door in self.doors:
      self.dauber.drawEntity(door.rect, door.cDispDoor)
      self.dauber.drawEntity(door.knobRect, door.cDispKnob)
    if self.textbox.displayTrue:
      self.textbox.drawTextbox()
    self.dauber.drawEntity(self.player.rect, self.player.color)

MAIN()
