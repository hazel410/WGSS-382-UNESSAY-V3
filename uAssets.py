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
  ([hubXPos[1], dims.hubDoorHeight], "lalala", dest.none),
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
  ([550, 250, 30, 40], (colr.mom), "It's your mom. She's not reacting much."), 
  ([500, 248, 30, 40], (colr.dad), "It's your dad. You don't remember why he was upset.")
]
sc1bDoors = [
  ([hubXPos[0], dims.otherDoorHeight], "", dest.r1a)
]
sc1bObjects = [
  ([500, 300, 25, 30], (colr.youngPlayer), "It's you. You're scared. The walls barely muffle his yelling")
]
### ------------------ ###

### ----assignment---- ###
"MAKE SURE THESE ARE ORDERED"
doors = []
doors.append(hubDoors)
doors.append(sc1aDoors)
doors.append(sc1bDoors)

objects = []
objects.append(hubObjects)
objects.append(sc1aObjects)
objects.append(sc1bObjects)
### ------------------ ###