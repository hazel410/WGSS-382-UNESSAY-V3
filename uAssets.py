import uEnums
colr = uEnums.COLORS()
dims = uEnums.DIMENSIONS()
dest = uEnums.DESTINATIONS()

# ------------------------------------------------------------------ #
# This file contains the specifics of all objects in the game.
# This data will be loaded into various objects defined by the
# entities file. Then, main will direct those objects to be drawn
# by the display file
# ------------------------------------------------------------------ #

"""
DOCUMENTATING QUIRKS OF RUSHED CODE:

- STORY RELATED OBJECTS
  An object being story related, i.e. and object which unlocks a door is
  denoted by "STRY: " begining the objects interaction text. Furthermore,
  no story related objects may have repeat text, or else weird shit will
  happen.
"""
  
### ------math-------- ###
hubYInt = dims.wBorder + dims.hubDoorSpacing
hubSlope = dims.wDoor + dims.hubDoorSpacing
hubXPos = []
for x in range(8):
  hubXPos.append((hubSlope * x) + hubYInt)
### ------------------ ###

### ------hub-:3------ ###
hubDoors = [
  ([hubXPos[0], dims.hubDoorHeight], "As you open the door, the smell of your childhood home creeps into you", dest.r1a),
  ([hubXPos[1], dims.hubDoorHeight], "It's the bookstore with your mom. This is the first time you truly felt unloved", dest.r2),
  ([hubXPos[2], dims.hubDoorHeight], "lalala", dest.none),
  ([hubXPos[3], dims.hubDoorHeight], "lalala", dest.none),
  ([hubXPos[4], dims.hubDoorHeight], "lalala", dest.none),
  ([hubXPos[5], dims.hubDoorHeight], "lalala", dest.none),
  ([hubXPos[6], dims.hubDoorHeight], "lalala", dest.none),
  ([hubXPos[7], dims.hubDoorHeight], "lalala", dest.none)
]
hubObjects = []
### ------------------ ###

### ----screen-1------ ###
sc1aDoors = [
  ([hubXPos[0], dims.otherDoorHeight], "", dest.hub),
  ([hubXPos[0], dims.hubDoorHeight], "", dest.r1b)
]
sc1aObjects = [
  ([550, 250, 30, 40], (colr.mom), "It's your mom. She's trying to maintain composure, but you knew she was scared too."), 
  ([500, 248, 30, 40], (colr.dad), "It's your dad. You don't even remember why he was upset.")
]
sc1bDoors = [
  ([hubXPos[0], dims.otherDoorHeight], "", dest.r1a)
]
sc1bObjects = [
  ([500, 300, 25, 30], (colr.youngPlayer), "STRY: It's you. You're scared. The walls barely muffle his yelling")
]
### ------------------ ###

### ----screen-2------ ###
sc2Doors = [
  ([hubXPos[1], dims.otherDoorHeight], "", dest.hub)
]
sc2Objects = [
  ([300, 170, 25, 30], (colr.youngPlayer), "STRY: It's you. You're sobbing. You felt so dejected and unwanted. There was nothing you could do to change yourself."),
  ([450, 165, 30, 40], (colr.mom), "It's your mom; She told you with tears that she couldn't deal with you anymore because she didn't understand how to raise a child like you."),
  ([550, 130, 50, 100], (colr.door), "It's a bookshelf. Your mom picked out a book titled \"How to deal with autistic children\"")
]
### ------------------ ###

### ----assignment---- ###
"MAKE SURE THESE ARE ORDERED"
doors = []
doors.append(hubDoors)
doors.append(sc1aDoors)
doors.append(sc1bDoors)
doors.append(sc2Doors)

objects = []
objects.append(hubObjects)
objects.append(sc1aObjects)
objects.append(sc1bObjects)
objects.append(sc2Objects)
### ------------------ ###