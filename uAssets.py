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

doors = [
  # HUB
  [
    ([hubXPos[0], dims.hubDoorHeight], "As you open the door, the smell of your childhood home creeps into you", dest.r1a),
    ([hubXPos[1], dims.hubDoorHeight], "It's the bookstore with your mom. This is the first time you truly felt unloved", dest.r2),
    ([hubXPos[2], dims.hubDoorHeight], "Its your first week of school after transferring", dest.r3),
    ([hubXPos[3], dims.hubDoorHeight], "lalala", dest.none),
    ([hubXPos[4], dims.hubDoorHeight], "lalala", dest.none),
    ([hubXPos[5], dims.hubDoorHeight], "lalala", dest.none),
    ([hubXPos[6], dims.hubDoorHeight], "lalala", dest.none),
    ([hubXPos[7], dims.hubDoorHeight], "lalala", dest.none)
  ],
  # Screen 1a
  [
    ([hubXPos[0], dims.otherDoorHeight], "", dest.hub),
    ([hubXPos[0], dims.hubDoorHeight], "", dest.r1b)
  ],
  # Screen 1b
  [
    ([hubXPos[0], dims.otherDoorHeight], "", dest.r1a)
  ],
  # Screen 2
  [
    ([hubXPos[1], dims.otherDoorHeight], "", dest.hub)
  ],
  # Screen 3
  [
    ([hubXPos[2], dims.otherDoorHeight], "", dest.hub)
  ],
  # Screen 4
  [
    ([hubXPos[3], dims.otherDoorHeight], "", dest.hub)
  ],
  # Screen 5
  [
    ([hubXPos[4], dims.otherDoorHeight], "", dest.hub)
  ],
  # Screen 6
  [
    ([hubXPos[5], dims.otherDoorHeight], "", dest.hub)
  ],
  # Screen 7
  [
    ([hubXPos[6], dims.otherDoorHeight], "", dest.hub)
  ],
  # Screen 8
  [
    ([hubXPos[7], dims.otherDoorHeight], "", dest.hub)
  ],
]

objects = [
  # Hub
  [

  ],
  # Screen 1a
  [
    ([550, 250, 30, 40], (colr.mom), "It's your mom. She's trying to maintain composure, but you knew she was scared too."), 
    ([500, 248, 30, 40], (colr.dad), "It's your dad. You don't even remember why he was upset.")
  ],
  # Screen 1b
  [
    ([500, 300, 25, 30], (colr.youngPlayer), "STRY: It's you. You're scared. The walls barely muffle his yelling")
  ],
  # Screen 2
  [
    ([300, 170, 25, 30], (colr.youngPlayer), "STRY: It's you. You're sobbing. You felt so dejected and unwanted. There was nothing you could do to change yourself."),
    ([450, 165, 30, 40], (colr.mom), "It's your mom; She seemed so tired. But you couldn't blame her."),
    ([550, 130, 50, 100], (colr.door), "It's a bookshelf. Your mom picked out a book titled \"How to deal with autistic children\"")
  ],
  # Screen 3
  [
    ([410, 150, 25, 30], (colr.youngPlayer), "STRY: You knew they were making fun of you, but you pretended not to because it felt good to be included"),
    ([450, 130, 25, 30], (colr.miscPerson), "You don't remember what they were saying."),
    ([360, 135, 25, 30], (colr.miscPerson), "You hope they're doing alright now")
  ],
  # Screen 4
  [
    ([285, 120, 25, 30], (colr.youngPlayer), "STRY: ")
  ]
]