#import files
from player import Player
from room import Room
from roomList import room
from items import Item



# Linking Rooms
room['village'].n_to = room['path']
room['village'].w_to = room['blacksmith']    
room['village'].e_to = room['apothecary']
room['blacksmith'].s_to = room['village']
room['apothecary'].s_to = room['village']
room['path'].s_to = room['village']
room['path'].n_to = room['lostForestEntrance']
room['lostForestEntrance'].w_to = room['river']
room['lostForestEntrance'].n_to = room['lostForestPath']
room['lostForestEntrance'].s_to = room['path']
room['lostForestPath'].w_to = room['clearing']
room['lostForestPath'].n_to = room['caveEntrance']
room['river'].s_to = room['lostForestEntrance']
room['river'].e_to = room['clearing']
room['clearing'].s_to = room['lostForestPath']
room['clearing'].w_to = room['river']
room['clearing'].n_to = room['cabin']
room['caveEntrance'].s_to = room['lostForestPath']
room['cabin'].s_to = room['clearing']
room['cabin'].n_to = room['cabinInside']

# Add Items to rooms
room['village'].inventory = [
    Item('odd stone', 'junk', 5, 'An odd stone that catches your attention') ,
    
]
room['river'].inventory = [
    Item('silver sword', 'weapon', 20, 'A steel sword, great for taking out skeletons')
]
room['cabinInside'].inventory = [
    Item('treasure', 'treasure', 999, 'You did it! You found the treasure!')
]



# Direction inputs
movement = ['n' , 's' , 'e' , 'w' ,]


# Start of Game
welcomeMessage = f'Hello Traveler! Thank you for embarking on this adventure.'
gameAuthor = f'Game Creator: Christian Ford'
gameRepo = f'Game Repo: https://github.com/Christian-Ford/TheLostTreasure \n'


print(gameAuthor)
print(gameRepo)
print(welcomeMessage)

# Asking player their name
nameInput = input('What is your name?: \n')
newPlayer = Player(nameInput, room['village'], 100, 20, [] , [])
    
# Game Loop Monicer
completion = False
# Game Loop
while completion == False:

    if(len(newPlayer.current_room.inventory) > 0):
        print(
            f'The following items are observed in this room: {[item.name for item in newPlayer.current_room.inventory]}\n')
    else:
        print('There are no items left in this room.\n')
    
    

    print(newPlayer)

    # User Prompt
    playerAction = input(
        'What do you do? \n'
        
    )

    playerOption = playerAction.split(' ')

    

    # User Input Conditionals
    if playerAction.lower() == 'q':
        exit()
    
    elif playerAction.lower() == 'h':
        print(f'Move North = "n" , Move South = "s" , Move East = "e" , Move West = "w" , Get/Drop Items = "get"/"drop" + "item name" Help = "h" Quit Game = "q" \n')
    
    elif playerAction.lower() in movement:
        newPlayer.move_player(playerAction)

    elif playerOption[0].lower() == 'get':
        for item in newPlayer.current_room.inventory:
            if(item.name == playerOption[1]):
                newPlayer.get_item(item)
                newPlayer.current_room.inventory.remove(item)
                for x in newPlayer.inventory:
                    if(x.name == 'treasure'):
                        print('\n\n\nCongratulations! You got the treasure! You win!')
                        completion = True
            else:
                print('\n\n\nThat item is not in this room.')
    elif playerOption[0] == 'drop':
        for item in newPlayer.inventory:
            if(item.name.lower() == playerOption[1].lower()):
                newPlayer.drop_item(item)
            else:
                print(f'You do not have a {playerOption[1]} to drop in here.')

        
    else:
        print(f'Please choose a valid option \n'
               'Valid Options: "n", "s", "e", or "w" for directions \n"get" / "drop: + "item name" to get/drop items\n"h" for help for "q" to quit the game')

