#import files
from player import Player
from room import Room

room = {
    'village': Room("Village Center", "In the Village Center you see the BlackSmith's Shop to the West, the Apothecary to the East, and a Path leading North towards the lost forest"),

    'blacksmith': Room("Blacksmith's Shop", "You enter the Blacksmith's shop, the walls are lined with weapons and armors, though you cannot buy anything as you are poor, return to the Village Center by heading South"),

    'apothecary': Room("Apothecary", "You enter the Apothecary, the shelves lined with different herps and potions, though you cannot buy anything as you are poor, return to the Village Center by heading South"),

    'path': Room("Path to Lost Forest", "You head North, stopping halfway to the Lost Forest to rest. You can continue North to the Lost Forest, or head South to get to the Village Center"),

    'lostForestEntrance': Room("Lost Forest Entrance", "You arrive at the line of the Lost Forest. There's a path to the west that leads to a river, and a path North to brave the insides of the Lost Forest. " ),
}

    # Linking Rooms
room['village'].n_to = room['path']
room['village'].w_to = room['blacksmith']    
room['village'].e_to = room['apothecary']
room['blacksmith'].s_to = room['village']
room['apothecary'].s_to = room['village']
room['path'].s_to = room['village']
room['path'].north_to = room['lostForestEntrance']

# Direction inputs
movement = ['n' , 's' , 'e' , 'w' ,]


# Start of Game
welcomeMessage = f'Hello Traveler! Thank you for embarking on this adventure.'
gameAuthor = f'Game Creator: Christian Ford'
gameRepo = f'Game Repo: https://github.com/Christian-Ford/TheLostTreasure \n'


print(gameAuthor)
print(gameRepo)
print(welcomeMessage)

nameInput = input('What is your name?: \n')
newPlayer = Player(nameInput, room['village'])
    
while True:

    print(newPlayer)

    # User Prompt
    playerAction = input(
        'Where do you go? \n'
        '---------------------------------------- \n'
    )

    # User Input Conditionals
    if playerAction == 'q':
        exit()
    elif playerAction == 'h':
        print(f'Move North = "n" , Move South = "s" , Move East = "e" , Move West = "w" , Quit Game = "q" \n')
    elif playerAction in movement:
        newPlayer.move_player(playerAction)
    else:
        print(f'Please choose a valid option \n'
               'Valid Options: "n", "s", "e", "w", or "q"')

