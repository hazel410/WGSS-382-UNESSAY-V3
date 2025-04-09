import pygame
pygame.init()
import uDisplay
import uInput
import uAssets
import uEntities
import uEnums

# Pygame inits
dims = uEnums.DIMENSIONS()
screen = pygame.display.set_mode([dims.wScreen, dims.hScreen], flags=pygame.SCALED, vsync=1)
pygame.display.set_caption("WGSS382 UNESSAY: Untitled")
clock = pygame.time.Clock()

# Grabbing other files' classes
dauber = uDisplay.DAUBER(screen)
textbox = uDisplay.TEXTBOX(screen)
player = uEntities.PLAYER()
events = uInput.EVENTS()
dest = uEnums.DESTINATIONS()

# Important variables
running = True
target = dest.none
gameState = 2
objects = []
doors = []
hubUnlocks = 1
activeScreen = dest.hub

while running:

  # Grabbing Events
  events.getEvents()
  quit = events.quit
  jPress = events.jPress
  fPress = events.fPress
  movement = events.move

  # Textbox logic
  if gameState == 0:
    if jPress:
      textbox.advanceText()
    if not textbox.displayTrue:
      if target == dest.none:
        gameState = 1
      else:
        gameState = 2
        activeScreen = target
  
  # movement logic
  elif gameState == 1:
    player.applyVelocity(movement)
    player.snapBorder()
    for object in objects:
      if player.detectObjectCollision(object.neswEdges):
        player.fixObjectCollision(object.rect, object.angles, object.center)
      if player.isTouchingObject(object.neswEdges):
        object.touchingPlayer = True
      else:
        object.touchingPlayer = False
      if object.touchingPlayer and jPress and object.text != "":
        gameState = 0
        object.interacted = True
        textbox.applyText(object.text)
    for door in doors:
      if player.detectObjectCollision(door.neswEdges):
        player.fixObjectCollision(door.rect, door.angles, door.center)
      if player.isTouchingObject(door.neswEdges):
        door.touchingPlayer = True
      else:
        door.touchingPlayer = False
      if door.touchingPlayer and jPress:
        if door.currentTarget == dest.none:
          gameState = 0
          textbox.applyText(door.dispText)
        else:
          target = door.currentTarget
          textbox.applyText(door.dispText)
          gameState = 0
  
  # transistion logic
  elif gameState == 2:
    keyIter = 0
    doors = []
    objects = []
    for doorInfo in uAssets.doors[activeScreen]:
      currentDoor = uEntities.DOOR(doorInfo[0], doorInfo[1], doorInfo[2])
      if activeScreen == dest.hub:
        # this if block prevents fuckery on game start
        if target != dest.none:
          player.setMiddle()
        if keyIter < hubUnlocks:
          currentDoor.unlock()
        keyIter += 1
      else:
        player.setMiddle()
        currentDoor.unlock()
      doors.append(currentDoor)
    for objectInfo in uAssets.objects[activeScreen]:
      objects.append(uEntities.OBJECT(objectInfo[0], objectInfo[1], objectInfo[2]))
    gameState = 1
    target = dest.none
  
  # Display calls
  dauber.drawPlayArea()
  dauber.drawBorder()
  dauber.drawEntity(player.rect, player.color)
  for object in objects:
    dauber.drawEntity(object.rect, object.color)
  for door in doors:
    dauber.drawEntity(door.rect, door.cDispDoor)
    dauber.drawEntity(door.knobRect, door.cDispKnob)
  if textbox.displayTrue:
    textbox.drawTextbox()
  dauber.drawEntity(player.rect, player.color)

  # final processes
  if fPress:
    pygame.display.toggle_fullscreen()
  if quit:
    running = False
  pygame.display.flip()
  clock.tick(60)

# game is over now :3
pygame.quit()
print("thanks for playing :)")