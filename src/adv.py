import time
from room import Room
from player import Character


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input('Hello! please enter your name!')
current_room = room['outside']
player_1 = Character(player_name, current_room)
# Write a loop that:
while True:
# * Prints the current room name
    print(player_1.current_room)
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
Answer_N = ["N", "n"]
Answer_W = ["W", "w"]
Answer_S = ["S", "s"]
Answer_E = ["E", "e"]

required = ("\n That movement isn't allow. Use only N, W, S, E to move")
# If the user enters "q", quit the game.

def beginning():
    print ("After a long journey you finally arrive outside MixAmp Cave. An excited look comes across you face as you imagine the wonderful treasure it holds from all the stories you've heard.")
    time.sleep(1)
    print ("""N. Move into the cave mount""")
    choice = input(">>>") #first move
    if choice in Answer_N:
        option_foyer()
    else:
        print (required)
        intro()
