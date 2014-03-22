from tank import Tank
from tank import Element


def main():
    tankflo = Tank (10, 10)
    mur = Element (0,0)
    murun= Element(4,4)
    murdeux=Element(5,5)

    mur.add_elements()
    murun.add_elements()
    mur.error_elements()
    

    tankflo.turnright()
    mur.add_elements()
    tankflo.turnleft()
    tankflo.fire()
    tankflo.fire()
    tankflo.fire()
    tankflo.fire()
    tankflo.fire()
    tankflo.fire()
    tankflo.fire()
