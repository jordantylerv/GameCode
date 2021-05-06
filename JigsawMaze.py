#Jordan Veridiano

#establish rooms, directions, and items
rooms = {
    'Room 1' : {'NORTH' : 'Room 2', 'EAST' : 'Room 8'}, #start game
    'Room 2' : {'NORTH' : 'Room 3', 'EAST' : 'Room 9'},
    'Room 3' : {'NORTH' : 'Room 10', 'EAST' : 'Room 4'},
    'Room 4' : {'EAST' : 'Room 5', 'SOUTH' : 'Room 9'},
    'Room 5' : {'NORTH' : 'Room 11', 'SOUTH' : 'Room 6'},
    'Room 6' : {'WEST' : 'Room 9', 'SOUTH' : 'Room 7'},
    'Room 7' : 'Finish' #end game
}
items = {
    'Room 1' : {'item' : 'None'},
    'Room 2' : {'item' : 'Puzzle 1'}, #puzzles
    'Room 3' : {'item' : 'Puzzle 2'},
    'Room 4' : {'item' : 'Puzzle 3'},
    'Room 5' : {'item' : 'Puzzle 4'},
    'Room 6' : {'item' : 'Puzzle 5'},
    'Room 7' : {'item' : 'Puzzle 6'},
    'Room 8' : {'item' : 'Capturer'}, #villain rooms
    'Room 9' : {'item' : 'Capturer'},
    'Room 10' : {'item' : 'Capturer'},
    'Room 11' : {'item' : 'Capturer'}
}

#game menu and commands
def main_menu():
   print("Escape Room")
   print("Collect 6 puzzle pieces to win the game and avoid your capturer!")
   print("Move commands: NORTH, SOUTH, EAST, WEST or EXIT to quit game.")

#function for current position and items obtained in game
def current_position():
    print('You are in:', [current_room])
    print ("You now have available to you: ", items[current_room])
    print('Pick a door')

#starting point
start = 'Room 1'
#value for starting point
current_room = start

#play game
main_menu()
while True:
    #call to prompt functions
    current_position()
    move = input('NORTH, SOUTH, EAST, WEST, or EXIT:\n>').upper()
    #quit command
    if move == 'EXIT'.upper():
        print('Thank you for playing')
        break
    #move in-between rooms
    elif move in rooms[current_room]:
        current_room = rooms[current_room][move]
        #enter a room with the villain
        if current_room == 'Room 8':
            print('You got caught!')
            break
        if current_room == 'Room 9':
            print('You got caught!')
            break
        if current_room == 'Room 10':
            print('You got caught!')
            break
        if current_room == 'Room 11':
            print('You got caught!')
            break
        if current_room == 'Room 7':
            print('You won!')
            break
    #if user input is typoed or no door available
    else:
        print('Error: No door in that direction!')