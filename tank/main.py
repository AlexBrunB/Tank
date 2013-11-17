from tank import Tank

def main():
    tankalex = Tank(5, 5)
    tankzouzou = Tank(10, 10)

    tankalex.move_forward()
    tankzouzou.turnright()
    tankalex.turnleft()
    tankalex.turnright()

    tankalex.fire()
