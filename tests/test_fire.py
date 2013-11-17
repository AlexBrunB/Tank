from tank import Tank

def test_fire_consumes_ammo():
    mytank = Tank(0, 0)

    assert mytank.ammo == 50, 'Initial ammo should be 50'
    mytank.fire()

    assert mytank.ammo == 49, 'Ammo should have decreased of one'

def test_cannot_fire_without_ammo():
    mytank = Tank(0, 0)

    while not mytank.ammo == 0:
        mytank.fire()

    # here mytank has no more ammo... try to fire and check ammo again

    mytank.fire()

    assert mytank.ammo == 0, "Ammo should not be allowed to go below 0"

def test_reload():
    mytank = Tank(0, 0)

    assert mytank.ammo == 50, 'Initial ammo should be 50'
    mytank.fire()

    assert mytank.ammo == 49, 'Ammo should have decreased of one'
    mytank.reload()

    assert mytank.ammo == 50, 'After reloading we should have 50 ammo back'
