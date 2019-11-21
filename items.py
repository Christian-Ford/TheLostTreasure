# Defining Item Class
class Item:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

# Defining Weapon Class
class Weapon:
    def __init__(self, name, type, value, attack_rating, durability):
        super().__init__(name, type, value)
        self.attack_rating = attack_rating
        self.durability = durability

# Defining Armor Class
class Armor:
    def __init__(self, name, type, value, armor_type, armor_rating, durability):
        super().__init__(name, type, value)
        self.armor_type = armor_type
        self.armor_rating = armor_rating
        self.durability = durability