# -*- coding: utf-8 -*-

# possible directions
enum_directions = {
    'north': 0,
    'east': 1,
    'south': 2,
    'west': 3,
}


class Element(object):
    """This is a class that designates
    an object in the battlefield
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vehicule(Element):
    """This is a class to manage directions
    in the battlefield
    """

    def __init__(self, x, y):
        super(Vehicule, self).__init__(x, y)
        self.direction = enum_directions['north']

    def move_forward(self):
        print('Your tank moves forward')

        if self.direction == enum_directions['north']:
            self.y += 1

        elif self.direction == enum_directions['east']:
            self.x += 1

        elif self.direction == enum_directions['south']:
            self.y -= 1

        elif self.direction == enum_directions['west']:
            self.x -= 1

        print('Your tank is now at (%d, %d)' % (self.x, self.y))

    def turnright(self):
        print('Your tank turns 90° to the right')
        if self.direction == 3:
            self.direction = 0
        else:
            self.direction += 1

    def turnleft(self):
        print('Your tank turns 90° left')
        if self.direction == 0:
            self.direction = 3
        else:
            self.direction -= 1


class Tank(Vehicule):
    """This is a class to manage the weapons
    """

    def __init__(self, x, y):
        super(Tank, self).__init__(x, y)
        self.ammo = 50
        print ("Creation d'une instance de Tank")

    def fire(self):
        if not self.ammo <= 0:
            print('Your tank fires')
            self.ammo -= 1
            print('Your tank has %s ammo left' % self.ammo)
        else:
            print('You cannot fire when ammo is empty')

    def reload(self):
        """This function handles reloading ammos
        """
        print('Your tank reloads')
        self.ammo = 50


#class Battlefield(object):
# def __init__(self):
#      self.elements = []
#
# def add_elements(self, elements):
