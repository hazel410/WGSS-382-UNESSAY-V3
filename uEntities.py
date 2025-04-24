import uEnums
import numpy

# ------------------------------------------------------------------ #
# This file contains the classes for objects, the player, doors, etc.
# This file should only be called by main to establish entities. main 
# may also read and write specific variables of specific entities
# ------------------------------------------------------------------ #

colr = uEnums.COLORS()
dims = uEnums.DIMENSIONS()
dest = uEnums.DESTINATIONS()
misc = uEnums.MISC()

def angleBetween(point1, point2):
    """
    Finds the angle between two points in degrees.
    (starting from the positive x axis and rotating
    counter-clockwise), from the perspective of 
    point 1
    """

    xDel = point2[0] - point1[0]
    yDel = point2[1] - point1[1]
    
    # prevents div0
    if xDel == 0:
      if yDel < 0:
        return 90
      elif yDel > 0:
        return 270
    # if not div0, calculates angle
    else:
      rawAngle = (numpy.arctan(yDel / xDel) * (180 / numpy.pi))
      if xDel > 0 and yDel > 0:   # Q4
        return 360 - abs(rawAngle)
      elif xDel < 0 and yDel > 0: # Q3
        return 180 + abs(rawAngle)
      elif xDel < 0 and yDel < 0: # Q2
        return 180 - abs(rawAngle)
      else:                       # Q1
        return abs(rawAngle)

    
class PLAYER:
  def __init__(self):
    self.nScreenBorder = dims.hBorder
    self.eScreenBorder = dims.wScreen - dims.wBorder - dims.wPlayer
    self.sScreenBorder = dims.hScreen - dims.hPlayer - dims.hTextbox - (2 * dims.hBorder)
    self.wScreenBorder = dims.wBorder
    self.rect = [dims.wScreen / 2, (self.nScreenBorder + self.sScreenBorder) / 2, 
                 dims.wPlayer, dims.hPlayer]
    self.updatePositionDependencies()
    self.speedModifier = 4
    self.velocity = [0, 0]
    self.color = colr.player
    
  def updatePositionDependencies(self):
    """
    When self.rect is changed, call this function. 
    It updates all the things dependent on self.rect
    """
    self.nEdge = self.rect[1]
    self.eEdge = self.rect[0] + self.rect[2]
    self.sEdge = self.rect[1] + self.rect[3]
    self.wEdge = self.rect[0]
    self.center = [(self.eEdge + self.wEdge) / 2, (self.nEdge + self.sEdge) / 2]

  def applyVelocity(self, wasd):
    """
    given key presses, change velocity and update position
    """
    # converting input to velocity
    self.velocity = [0, 0]
    if wasd[0]:
      self.velocity[1] -= 1 
    if wasd[1]:
      self.velocity[0] -= 1
    if wasd[2]:
      self.velocity[1] += 1
    if wasd[3]:
      self.velocity[0] += 1

    # adds speed modifier and normalizes diagonal
    self.velocity[0] *= self.speedModifier
    self.velocity[1] *= self.speedModifier
    if abs(self.velocity[0]) is not abs(self.velocity[1]):
      self.velocity[0] *= (2 ** .5)
      self.velocity[1] *= (2 ** .5)

    # changes position
    self.rect[0] += self.velocity[0]
    self.rect[1] += self.velocity[1]
    self.updatePositionDependencies()

  def snapBorder(self):
    """
    If beyond screen border, snap to corresponding screen border
    """
    if self.rect[1]   < self.nScreenBorder: 
      self.rect[1]    = self.nScreenBorder
    elif self.rect[1] > self.sScreenBorder: 
      self.rect[1]    = self.sScreenBorder
    if self.rect[0]   > self.eScreenBorder:
      self.rect[0]    = self.eScreenBorder 
    elif self.rect[0] < self.wScreenBorder: 
      self.rect[0]    = self.wScreenBorder
    self.updatePositionDependencies()

  def detectObjectCollision(self, neswObjEdges):
    """
    If colliding with a given object's edges, return true
    """
    horzOverlap = (self.wEdge < neswObjEdges[1]) and (self.eEdge > neswObjEdges[3])
    vertOverlap = (self.nEdge < neswObjEdges[2]) and (self.sEdge > neswObjEdges[0])
    return horzOverlap and vertOverlap
  
  def fixObjectCollision(self, objRect, objAngles, objCenter):
    """
    when called, snaps player to given object's nearest wall
    """
    angleToPlayer = angleBetween(objCenter, self.center)
    
    # player north of object
    if angleToPlayer >= objAngles[0] and angleToPlayer <= objAngles[1]:
      self.rect[1] = objRect[1] - self.rect[3]
    
    # player west of object
    elif angleToPlayer >= objAngles[1] and angleToPlayer <= objAngles[2]:
      self.rect[0] = objRect[0] - self.rect[2]
    
    # player south of object
    elif angleToPlayer >= objAngles[2] and angleToPlayer <= objAngles[3]:
      self.rect[1] = objRect[1] + objRect[3]
    
    # player east of object
    else:
      self.rect[0] = objRect[0] + objRect[2]
    self.updatePositionDependencies()
  
  def isTouchingObject(self, neswObjEdges):
    """
    if player is touching object, return true
    """

    vertAlligned = (self.nEdge < neswObjEdges[2] and self.sEdge > neswObjEdges[0])
    horzAlligned = (self.eEdge > neswObjEdges[3] and self.wEdge < neswObjEdges[1])

    touchingObjN = self.sEdge == neswObjEdges[0] and horzAlligned
    touchingObjE = self.wEdge == neswObjEdges[1] and vertAlligned
    touchingObjS = self.nEdge == neswObjEdges[2] and horzAlligned
    touchingObjW = self.eEdge == neswObjEdges[3] and vertAlligned
    
    return (touchingObjN or touchingObjE or touchingObjS or touchingObjW)
  
  def setMiddle(self):
    """
    Put player's y pos at middle of playable screen
    """

    self.rect[1] = (self.nScreenBorder + self.sScreenBorder) / 2
    self.updatePositionDependencies()

class OBJECT:
  def __init__(self, rect, color, text, storyRelated=False):
    self.rect = rect
    self.nEdge = self.rect[1]
    self.eEdge = self.rect[0] + self.rect[2]
    self.sEdge = self.rect[1] + self.rect[3]
    self.wEdge = self.rect[0]
    self.neswEdges = [self.nEdge, self.eEdge, self.sEdge, self.wEdge]
    self.center = [(self.eEdge + self.wEdge) / 2, (self.sEdge + self.nEdge) / 2]
    self.angles = [angleBetween(self.center, [self.eEdge, self.nEdge]),
                   angleBetween(self.center, [self.wEdge, self.nEdge]),
                   angleBetween(self.center, [self.wEdge, self.sEdge]),
                   angleBetween(self.center, [self.eEdge, self.sEdge])]
    self.color = color
    self.text = text
    self.touchingPlayer = False
    self.interacted = False
    self.storyRelated = storyRelated

class DOOR:
  def __init__(self, position, unlockText, target, lockedText=misc.lockedText):
    self.rect = [position[0], position[1], dims.wDoor, dims.hDoor]
    self.nEdge = self.rect[1]
    self.eEdge = self.rect[0] + self.rect[2]
    self.sEdge = self.rect[1] + self.rect[3]
    self.wEdge = self.rect[0]
    self.knobRect = [self.rect[0] + (.66 * self.rect[2]), self.rect[1] + (.5 * self.rect[3]), dims.doorknob, dims.doorknob]
    self.neswEdges = [self.nEdge, self.eEdge, self.sEdge, self.wEdge]
    self.center = [(self.eEdge + self.wEdge) / 2, (self.sEdge + self.nEdge) / 2]
    self.angles = [angleBetween(self.center, [self.eEdge, self.nEdge]),
                   angleBetween(self.center, [self.wEdge, self.nEdge]),
                   angleBetween(self.center, [self.wEdge, self.sEdge]),
                   angleBetween(self.center, [self.eEdge, self.sEdge])]
    self.touchingPlayer = False

    self.cUnlockDoor = colr.door
    self.cUnlockKnob = colr.doorknob
    self.cLockedDoor = colr.lockedDoor
    self.cLockedKnob = colr.lockedDoorKnob
    self.unlockText = unlockText
    self.lockedText = lockedText
    self.unlockedTarget = target
    
    self.cDispKnob = self.cLockedKnob
    self.cDispDoor = self.cLockedDoor
    self.dispText  = self.lockedText
    self.currentTarget = dest.none

  def unlock(self):
    self.cDispDoor = self.cUnlockDoor
    self.cDispKnob = self.cUnlockKnob
    self.dispText  = self.unlockText
    self.currentTarget = self.unlockedTarget
  