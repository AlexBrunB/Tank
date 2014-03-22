from tank import Tank

def test_move():
    print('Spawning tank at (0, 0)')
    mytank = Tank(0, 0)

    mytank.move_forward()

    assert mytank.x == 0, 'X should not have changed'
    assert mytank.y == 1, 'Y should have incremented of 1'

def test_move_and_turnright():
    print('Spawning tank at (0, 0)')
    mytank = Tank(0, 0)

    mytank.move_forward()
    mytank.turnright()
    mytank.move_forward()

    assert mytank.x == 1, 'X should have incremented of 1'
    assert mytank.y == 1, 'Y should have incremented of 1'

def test_move_and_turnleft():
    print('Spawning tank at (0, 0)')
    mytank = Tank(0, 0)

    mytank.move_forward()
    mytank.turnleft()
    mytank.move_forward()

    assert mytank.x == -1, 'X should have decremented of 1'
    assert mytank.y == 1, 'Y should have incremented of 1'

def test_turnright_and_move_all():
    print('Spawning tank at (0, 0)')
    mytank = Tank(0, 0)

    mytank.move_forward()
    mytank.turnright()
    mytank.move_forward()
    mytank.turnright()
    mytank.move_forward()
    mytank.turnright()
    mytank.move_forward()
    mytank.turnright()

    assert (mytank.x == 0 and mytank.y == 0), 'Tank should be at spawn'

def test_turnleft_and_move_all():
    print('Spawning tank at (0, 0)')
    mytank = Tank(0, 0)

    mytank.move_forward()
    mytank.turnleft()
    mytank.move_forward()
    mytank.turnleft()
    mytank.move_forward()
    mytank.turnleft()
    mytank.move_forward()
    mytank.turnleft()

    assert (mytank.x == 0 and mytank.y == 0), 'Tank should be at spawn'

