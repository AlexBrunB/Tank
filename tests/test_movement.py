from tank import Tank

def test_move():
    print('Spawning tank at (0, 0)')
    mytank = Tank(0, 0)

    mytank.move_forward()

    assert mytank.x == 0, 'X should not have changed'
    assert mytank.y == 1, 'Y should have incremented of 1'

def test_move_and_turn():
    print('Spawning tank at (0, 0)')
    mytank = Tank(0, 0)

    mytank.move_forward()
    mytank.turnright()
    mytank.move_forward()

    assert mytank.x == 1, 'X should have incremented of 1'
    assert mytank.y == 1, 'Y should have incremented of 1'
