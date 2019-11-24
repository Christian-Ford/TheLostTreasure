# Other creatures and characters

class Humanoid:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room


class Enemy(Humanoid):
    def __init__(self, name, current_room, health, weapon, armor):
        super().__init__(name, current_room)
        self.health = health
        self.weapon = weapon
        self.armor = armor

class NPC(Humanoid):
    def __init__(self, name, current_room, money):
        super().__init__(name, current_room)
        self.inventory = []
        self.money = money

# Testing
# skeleton = Enemy("Skeleton", "Clearing", 20, "Rusty Sword", "None")
# print(skeleton.name, skeleton.armor)

# blacksmith = NPC("Blacksmith", "Blacksmith Shop",
# ["Silver Sword", "Iron Armor"], 50)

# print(blacksmith.inventory, blacksmith.money)