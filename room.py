# Creating Room class

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    # Output to console
    def __str__(self):
        output = ''
        output += f'{self.name} \n'
        output += f'\nDescription: {self.description} \n'

        return output