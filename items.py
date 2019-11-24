# Defining Item Class
class Item:
    def __init__(self, name, type, value, description):
        self.name = name
        self.type = type
        self.value = value
        self.description = description

# Defining Weapon Class
class Weapon:
    def __init__(self, name, type, value, description, attack_rating, durability):
        super().__init__(name, type, value, description)
        self.attack_rating = attack_rating
        self.durability = durability

# Defining Armor Class
class Armor:
    def __init__(self, name, type, value, description, armor_type, armor_rating, durability):
        super().__init__(name, type, value, description)
        self.armor_type = armor_type
        self.armor_rating = armor_rating
        self.durability = durability