# Creating our player

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    # Player Movement
    def move_player(self, command):
        if getattr(self.current_room, f'{command}_to') is not None:
            self.current_room = getattr(self.current_room, f'{command}_to')
        else:
            print(f'YOU CANNOT GO THAT WAY')

    #Output to console
    def __str__(self):
        output = ''
        output += '---------------------------------------- \n'
        output += f'Player Name: {self.name} \n'
        output += f'Current Room: {self.current_room} \n'

        return output