from items import *

room_entrance = {
    "name": "Entrance Hall",
    "description":
    """You stand at the entrance of the castle, the heavy door creaking
shuts behind you. Moonlight spills through the cracks, casting ghostly
shadows on the ancient stones. The air is thick with anitcipation,
you see four ancient wooden doors surrounding the area. The north door
leads to the Hallway, the east door to the Kitchen, the south door to the
Dungeon and the last door which is the west door leads to the Armoury.
What is your next move?""",
    "exits": {
        "north": "Hallway",
        "east": "Kitchen",
        "south": "Dungeon",
        "west": "Armoury",

    },
    "items": []
}

room_dungeon = {
    "name": "Dungeon",
    "description":
    """A cold shiver runs down your spine as you descend into the dungeon's depths. 
The air is damp and heavy, carrying the scent of decay.The flickering torches barely illuminate the damp stone walls, 
revealing forgotten chains and ominous cells.It seems that there is a missing torch inside. 
Maybe something will be revealed.There is a door at the north which leads 
to the Entrance what is your next move?""",
    "exits": {
        "north": "Entrance",

    },
    "items": []
}

room_kitchen = {
    "name": "Kitchen",
    "description":
    """You step into the castle's kitchen, a place frozen in time.
Dusty pots and pans hang from hooks, and a table sits in the middle,
covered in a thin layer of neglect. As you explore, you spot a small
set of matches. In the wall there is a key that you can take with
3 riddles. What is your next move?""",
    "exits": {
        "west": "Entrance",

    },
    "items": [item_matches]
}

room_armoury = {
    "name": "Armoury",
    "description":
    """Entering the armoury, the air is laden with the scent of rusted metal
and ancient leather. Rows of dusty weapons line the walls, each with its own
story of battles long past. It seems that there is a torch here although it 
requires matches, and also there is a mysterious piece of paper. 
The only exit is at the east. What is your next move?""",
    "exits": {
        "east": "Entrance",

    },
    "items": [item_torch, item_riddle2]
}

room_hallway = {
    "name": "The Hallway",
    "description": 
    """You find yourself in a dimly lit hallway, a chilling draft sweeps through 
leaving behind a haunted aura. You see two ancient wooden doorways on both ends 
of the hallway, the west door leads to a bedroom, and the east door leads to a library. 
The stairway is located to the south of you. What is your next move?""",

    "exits": {
        "east": "Library",
        "south": "Entrance",
        "west": "Bedroom",

    },
    "items": []
}

room_bedroom = {
    "name": "Bedroom",
    "description": """You are greeted by a sense of apprehension, the bed is draped in dusty, cobweb-covered
curtains. You notice a sturdy wooden chair in the dark corner of the room. The door on the
west leads to a bathroom, and the door on the east leads back to the hallway. What is your next move?
""",
    "exits": {
        "east": "Hallway",
        "west": "Bathroom",

    },
    "items": [item_chair]
}

room_bathroom = {
    "name": "Bathroom",
    "description": """You are met with an eerie sight. The tarnished, cracked mirror reflects your image
distorted and ghastly. You notice a crumpled piece of paper on the cold stone floor. The
door on the east leads back to the bedroom. What is your next move?
""",
    "exits": {
        "east": "Bedroom",

    },
    "items": [item_riddle3]
}

room_library = {
    "name": "Library",
    "description": """You see a bunch of shelves adorned with weathered books and dust-covered manuscripts. On
top of one of the shelves, you notice something of interest, but you cannot reach it without
something to stand on. The door on the west leads back to the hallway. What is your next move?
""",
    "exits": {
        "west": "Hallway",

    },
    "items": []
}

rooms = {
    "Entrance": room_entrance,
    "Dungeon": room_dungeon,
    "Kitchen": room_kitchen,
    "Armoury": room_armoury,
    "Hallway": room_hallway,
    "Bedroom": room_bedroom,
    "Bathroom": room_bathroom,
    "Library": room_library,

}
