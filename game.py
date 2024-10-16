from gameparser import normalise_input
from interactions import item_drop_interactions, item_inventory_interactions
from map import rooms
from items import *

player = {
    "inventory": [],
    "current_room": rooms['Entrance'],
    "game_flags": [],

}


def list_of_items(items):
    """
    Takes a list of items, defined in items.py, and returns a comma separated list of them.

    >>> list_of_items([])
    ''

    >>> list_of_items([item_chair])
    'a chair'

    >>> list_of_items([item_chair, item_torch])
    'a chair and a torch'

    >>> list_of_items([item_chair, item_matches, item_torch])
    'a chair, a pack of matches and a torch'
    """
    if len(items) == 0:
        return ''
    if len(items) == 1:
        return items[0]['name']

    items_string = ''

    for index, item in enumerate(items):
        items_string += item['name']

        # handle trailing comma/and
        if index < len(items) - 2:
            items_string += ', '
        elif index == len(items) - 2:
            items_string += ' and '

    return items_string


def print_room_items(room):
    """
    Takes a room as a parameter and prints out the present items as a comma separated list.

    >>> print_room_items(rooms['Kitchen'])
    There is a pack of matches here.
    """
    if room['items']:
        print(f"There is {list_of_items(room['items'])} here.")


def print_room(room):
    """
    Takes a room as a parameter and nicely prints out all relevant information.
    room argument is a dictionary containing name, description, and items for a room.

    >>> print_room(rooms['Kitchen'])
    <BLANKLINE>
    KITCHEN
    <BLANKLINE>
    Lorem ipsum
    <BLANKLINE>
    There is a pack of matches here.
    """
    print(f"\n{room['name'].upper()}\n\n{room['description']}\n")
    print_room_items(room)


def print_inventory(items):
    """
    Takes a list of items, and prints them nicely assuming the player has said items.

    >>> print_inventory([item_chair, item_matches])
    You have a chair and a pack of matches.

    >>> print_inventory([])
    You have no items.

    >>> print_inventory([item_chair, item_matches, item_torch])
    You have a chair, a pack of matches, and a torch.
    """
    if items:
        print(f"You have {list_of_items(items)}.")
    else:
        print("You have no items.")


def print_exit(direction, leads_to):
    """
    Prints a line of a menu of exits. Takes a direction and the name of the room into which it leads.

    >>> print_exit('east', 'Entrance Hall')
    GO EAST to Entrance Hall.
    """
    print(f"GO {direction.upper()} to {leads_to}.")


def exit_leads_to(exits, direction):
    """
    Takes a dictionary of exits and a direction, returning the name of the room the exit leads to.

    >>> exit_leads_to(rooms['Entrance']['exits'], 'north')
    'The Hallway'
    """
    return rooms[exits[direction]]['name']


def print_menu():
    """
    Takes the player dictionary and displays a menu of possible actions the player can take.
    """
    print("You can:")
    for direction in player['current_room']['exits']:
        print_exit(direction, exit_leads_to(player['current_room']['exits'], direction))

    for item in player['current_room']['items']:
        print(f"TAKE {item['id'].upper()} to take {item['name']}.")

    for item in player['inventory']:
        print(f"DROP {item['id'].upper()} to drop your {item['name']}.")

    for item in player['inventory']:
        print(f"INSPECT {item['id'].upper()} to inspect your {item['name']}.")

    print("What do you want to do?")


def menu():
    """
    Takes the player dictionary and prints a menu of possible actions the player can make.
    Then requests input from the user, and returns a normalised list of keywords.
    """

    print_menu()
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


def is_valid_exit(exits, direction):
    """
    Checks, given a dictionary of exits, and a direction, whether this
    is a valid direction to move to.

    Returns a boolean.

    >>> is_valid_exit(rooms['Entrance']['exits'], 'north')
    True

    >>> is_valid_exit(rooms['Dungeon']['exits'], 'south')
    False
    """
    return direction in exits


def move(exits, direction):
    """
    Returns the room into which the player will move given a direction and list of exits.
    """
    return rooms[exits[direction]]


def execute_go(direction):
    if is_valid_exit(player['current_room']['exits'], direction):
        player['current_room'] = move(player['current_room']['exits'], direction)
    else:
        print("You cannot go there.")


def execute_take(item_id):
    """
    Takes an item_id, and removes it from the current room, adds it to the
    players inventory, if it is present in the room.
    """
    found = False

    for item in player["current_room"]["items"]:
        if item_id == item["id"].lower():
            found = True
            player["current_room"]["items"].remove(item)
            player['inventory'].append(item)

    if not found:
        print("You cannot take that.")


def execute_drop(item_id):
    """
    Takes an item_id, and removes it from the players inventory, adds it to the
    current room, if the player has it in their inventory.
    """
    found = False

    for item in player["inventory"]:
        if item_id == item["id"].lower():
            found = True
            player["current_room"]["items"].append(item)
            player['inventory'].remove(item)

    if not found:
        print("You cannot drop that.")


def execute_inspect(item_id):
    """
    Takes an item_id, and displays its description, if the player has it in
    their inventory.
    """
    found = False

    for item in player["inventory"]:
        if item_id == item["id"].lower():
            found = True
            print(item['description'])

    if not found:
        print("You cannot inspect that.")


def execute_command(command):
    """
    Takes a command (a list of words returned by normalise_input) and
    depending on the type of action, executes said action.
    """

    if len(command) == 0:
        print("Do what?")

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what?")

    else:
        print("This makes no sense.")


def execute_drop_interaction():
    """
    Checks if a player has dropped an item in a room where this should trigger an interaction, then triggers
    the appropriate function.
    i.e. chair in library.
    """
    for interaction in item_drop_interactions:
        required_items = interaction['required_items']
        room_items = rooms[interaction['required_room']]['items']

        all_items_present = True

        # Check if an item is NOT present.
        for required_item in required_items:
            item_found = False
            for room_item in room_items:
                if room_item['id'] == required_item:
                    item_found = True

            if not item_found:
                all_items_present = False

        if all_items_present:
            interaction_function = interaction['function']
            interaction_function(player, rooms)


def execute_inventory_interaction():
    """
    Checks if the player is holding the correct items in a room which should trigger
    an interaction to occur, then triggers said interaction function.
    i.e. torch and matches in the dungeon.
    """
    for interaction in item_inventory_interactions:
        required_room = interaction['required_room']
        required_items = interaction['required_items']

        if player['current_room']['name'] == required_room:
            all_items_present = True

            # Check if an item is NOT present.
            for required_item in required_items:
                item_found = False
                for inventory_item in player['inventory']:
                    if inventory_item['id'] == required_item:
                        item_found = True

                if not item_found:
                    all_items_present = False

            if all_items_present:
                interaction_function = interaction['function']
                interaction_function(player, rooms)


def execute_interactions():
    """
    Executes any interactions that have had their conditions fulfilled.
    """
    execute_drop_interaction()
    execute_inventory_interaction()


def main():
    while True:
        execute_interactions()
        
        #  Win Condition
        if 'exit_unlocked' in player['game_flags']:
            break
        
        print_room(player['current_room'])
        print_inventory(player['inventory'])
        command = menu()
        execute_command(command)


if __name__ == "__main__":
    main()
