#import files
from player import Player
from room import Room
from roomList import room



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
newPlayer = Player(nameInput, room['village'], 100, 20, [] , [] , [])
    
# Game Loop
while True:

    print(newPlayer)

    # User Prompt
    playerAction = input(
        'What do you do? \n'
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

