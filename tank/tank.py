# -*- coding: utf-8 -*-

# possible directions
enum_directions = {
    'north': 0,
    'east' : 1,
    'south': 2,
    'west': 3,
}


# This is a class to declare the first class Tank with specifies.
# The Tank fight with ammo which decrease each time the player fires
# and directions which are shown in a grid.   
class Tank(object):
    def __init__(self, x, y):
        self.ammo = 50
        self.x = x
        self.y = y
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

    def fire(self):
        if not self.ammo <= 0:
            print('Your tank fires')
            self.ammo -= 1
            print('Your tank has %s ammo left' % self.ammo)
        else:
            print('You cannot fire when ammo is empty')

    def reload(self):
        print('Your tank reloads')
        self.ammo = 50
