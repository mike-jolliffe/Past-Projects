class Creature(object):
    '''Used for creating a creature, giving it stats, and making it fight'''

    def __init__(self, health, weapon, location):
        self.health = health
        self.weapon = weapon
        self.location = location

    def move(self, dir):
        '''Given a direction tuple, updates creature object's location on the board'''
        # TODO resolve directions so NSEW actually move player NSEW
        move_dict = {"N": (1,0), "S": (-1, 0), "E": (0, 1), "W": (0, -1)}
        if dir in move_dict:
            self.location = tuple(x + y for x, y in zip(self.location, move_dict[dir]))
        return self.location

    def attack(self):
        '''Makes creature object attack Hero object'''
        pass

class Hero(Creature):
    '''Player Character that modifies Creature class'''
    def __init__(self, health, weapon, location, armor, inventory):
        Creature.__init__(self, health, weapon, location)
        self.armor = armor
        self.inventory = inventory

