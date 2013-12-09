from tank import Tank

def main():
    tankalex = Tank(5, 5)
    tankzouzou = Tank(1, 1)

    tankalex.move_forward()
    tankalex.move_forward()
    tankalex.turnleft()
    tankalex.turnleft()
    tankalex.turnleft()
    tankalex.fire()
    tankalex.reload()
    
    tankzouzou.turnright()
    tankalex.turnleft()
    tankalex.turnright()

    tankalex.fire()
