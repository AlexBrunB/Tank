# -*- coding: utf-8 -*-
enum_direction = {
    'droite': 0,
    'haut' : 1,
    'gauche': 2,
    'bas': 3,
}


#This a class to declare the first class Tank with specifies.
#The Tank can fight with ammo, a warzone to move, and directions.    
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
        

    def turnleft(self):
        print ('votre tank pivote à gauche')

    def fight(self):
        print ('votre tank fait feu')
        self.ammo = self.ammo -1 
        print ('il vous reste %d minutions' % self.ammo)

    def reload(self):
        print ('plus de munitions, vous devez recharger')







