# Creating our player

class Player:
    def __init__(self, name, current_room, health, money, weapon, armor):
        self.name = name
        self.current_room = current_room
        self.health = health
        self.money = money
        self.weapon = weapon
        self.armor = armor
        self.inventory = []

    # Player Movement
    def move_player(self, command):
        if getattr(self.current_room, f'{command}_to') is not None:
            self.current_room = getattr(self.current_room, f'{command}_to')
        else:
            print(f'YOU CANNOT GO THAT WAY')

    # Define Get and Drop Items
    def get_item(self, pickup_item):
        self.inventory.append(pickup_item)

    def drop_item(self, drop_item):
        self.inventory.remove(drop_item)
        self.current_room.inventory.append(drop_item)

    #Output to console
    def __str__(self):
        output = ''
        output += '---------------------------------------- \n'
        output += f'Player Name: {self.name} \n'
        output += f'Current Room: {self.current_room} \n'

        return output


