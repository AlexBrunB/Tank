from tank import Tank

def main():
    tankalex = Tank(5, 5)

    tankalex.move_forward()
    tankalex.move_forward()
    tankalex.turnleft()
    tankalex.fire()
    tankalex.move_forward()
    tankalex.move_forward()
    tankalex.fire()
    tankalex.fire()
    tankalex.reload()

    tankalex.turnleft()
    tankalex.turnleft()
    tankalex.move_forward()
    tankalex.move_forward()
