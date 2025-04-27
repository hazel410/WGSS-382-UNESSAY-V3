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
DOCUMENTING RUSHED CODE:

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
    ([hubXPos[0], dims.hubDoorHeight], "[2008]: As you open the door, the smell of your childhood home creeps into you", dest.r1a),
    ([hubXPos[1], dims.hubDoorHeight], "[2011]: It's the bookstore with your mom. This is the first time you truly felt unloved", dest.r2),
    ([hubXPos[2], dims.hubDoorHeight], "[2012]: From one small school to another, it's your first week", dest.r3),
    ([hubXPos[3], dims.hubDoorHeight], "[2016]: You were so hateful", dest.r4),
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
    ([450, 130, 25, 30], (colr.miscPerson), "You remember all too well what they were saying. That word still breathes so much displreasure into you."),
    ([360, 135, 25, 30], (colr.miscPerson), "You hope they're doing alright now")
  ],
  # Screen 4
  [
    ([460, 120, 25, 30], (colr.youngPlayer), "STRY: You said some hurtful joke. You were surronded by other \"edgy\" assholes. You could finally ignore all the people punching down on you if you just punched down on others."),
    ([500, 100, 80, 150], (colr.lockedDoor), "The table is grey with blue dots. You're all eating flavorless spaghetti."),
    ([460, 180, 25, 30], (colr.miscPerson), "It's your bestfriend. In a few years you two will have a falling out as you begin to understand the hurt you've caused. For now he gives a sliver of comfort."),
    ([600, 120, 25, 30], (colr.miscPerson), "They wanted to try new pronouns. Years later you will too. But you weren't ready to face that yet.")
  ],
  # Screen 5
  [
    ([285, 120, 25, 30], (colr.youngPlayer), "STRY: 5")
  ],
  # Screen 6
  [
    ([285, 120, 25, 30], (colr.youngPlayer), "STRY: 6")
  ],
  # Screen 7
  [
    ([285, 120, 25, 30], (colr.youngPlayer), "STRY: 7")
  ],
  # Screen 8
  [
    ([285, 120, 25, 30], (colr.youngPlayer), "STRY: 8")
  ],
]