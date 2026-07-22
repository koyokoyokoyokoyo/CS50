import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(20)
    assert jar.capacity == 20

def test_str():
    jar = Jar()
    assert str(jar) == "" #OR assertjar.__str__ but this is unpythonic
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(200)

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪"
    
    with pytest.raises(ValueError):
        jar.withdraw(300)