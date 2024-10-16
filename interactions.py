from items import *


def interaction_unlock_riddle_1(player, rooms):
    if 'riddle_1_unlocked' not in player['game_flags']:
        print("You climb on the chair and find something atop the bookshelf...")
        rooms['Library']['items'].append(item_riddle1)
        player['game_flags'].append('riddle_1_unlocked')


def interaction_light_dungeon(player, rooms):
    if 'dungeon_lit' not in player['game_flags']:
        print('You light up the dungeon...')

        rooms['Dungeon']['description'] = """You place the torch... 
You reveal a map highlighting the Library, Armoury and Bathroom..."""

        player['inventory'].remove(item_torch)
        player['inventory'].remove(item_matches)

        player['game_flags'].append('dungeon_lit')


def interaction_unlock_kitchen_key(player, rooms):
    if 'kitchen_key_unlocked' not in player['game_flags']:
        print('You find a key hidden here...')  # TODO

        rooms['Kitchen']['items'].append(item_smallKey)
        player['game_flags'].append('kitchen_key_unlocked')


def interaction_unlock_dungeon_key(player, rooms):
    if 'dungeon_key_unlocked' not in player['game_flags']:
        print('You unlock a new key...')  # TODO

        rooms['Dungeon']['items'].append(item_mainKey)
        player['inventory'].remove(item_smallKey)
        player['game_flags'].append('dungeon_key_unlocked')


def interaction_unlock_exit(player, rooms):
    if 'exit_unlocked' not in player['game_flags']:
        print('You use the main key to unlock the exit to the castle... You escape succesfully')
        
        player['inventory'].remove(item_mainKey)
        player['game_flags'].append('exit_unlocked')
        


item_drop_interactions = [
    {
        'required_items': ['chair'],
        'required_room': 'Library',
        'function': interaction_unlock_riddle_1,
    }
]

item_inventory_interactions = [
    {
        'required_items': ['torch', 'matches'],
        'required_room': 'Dungeon',
        'function': interaction_light_dungeon,
    },
    {
        'required_items': ['riddle1', 'riddle2', 'riddle3'],
        'required_room': 'Kitchen',
        'function': interaction_unlock_kitchen_key,
    },
    {
        'required_items': ['smallKey'],
        'required_room': 'Dungeon',
        'function': interaction_unlock_dungeon_key,
    },
    {
        'required_items': ['mainKey'],
        'required_room': 'Entrance Hall',
        'function': interaction_unlock_exit,
    }
]
