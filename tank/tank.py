# -*- coding: utf-8 -*-

# We create a dictionnary for directions.
# The tank is able to turn on himself even before moving
enum_direction = {
    'droite': 0,
    'haut' : 1,
    'gauche': 2,
    'bas': 3,
}


# This is a class to declare the first class Tank with specifies.
# The Tank fight with ammo wich decrease and directions which are shown 
# in a grid.   
class Tank(object):
    def __init__(self, xinitial, yinitial):
        self.ammo = 50
        self.x = xinitial
        self.y = yinitial
        self.direction = enum_direction['droite']

    def move_forward(self):
        print ('votre tank avance')
        if self.direction == enum_direction['droite']:
            self.x = self.x +1
        elif self.direction == enum_direction['haut']:
            self.y = self.y +1 
        elif self.direction == enum_direction['gauche']:
            self.x = self.x -1
        elif self.direction == enum_direction['bas']:
            self.y = self.y -1    

        print ('Votre tank est sur la position %d, %d' % (self.x, self.y))

    def turnright(self):
        print ('votre tank tourne à droite')
        self.direction == enum_direction['droite']
        self.x = self.x +1

        print ('Votre tank est sur la position %d, %d' % (self.x, self.y))
        

    def turnleft(self):
        print ('votre tank pivote à gauche')
        self.direction == enum_direction['gauche']
        self.x = self.x -1

        print ('Votre tank est sur la position %d, %d' % (self.x, self.y))

    def fight(self):
        print ('votre tank fait feu')
        self.ammo = self.ammo -1 
        print ('il vous reste %d munitions' % self.ammo)

    def reload(self):
        print ('plus de munitions, vous devez recharger')
