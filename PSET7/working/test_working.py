import pytest
from working import convert

def main():
    test_working()
    working_error()

def test_working():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("5:30 PM to 12 AM") == "17:30 to 12:00"
    assert convert("6:30 AM to 10 PM") == "06:30 to 22:00"
    assert convert("7:30 PM to 5:50 AM") == "19:30 to 05:50"

def working_error():
    with pytest.raises(ValueError):
        convert("6 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("6:69 AM to 7:89 M")
    with pytest.raises(ValueError):
        convert("I HATE YOU")
    with pytest.raises(ValueError):
        convert("I am a cat meow meow")
    with pytest.raises(ValueError):
        convert("6:00 AM to 13:00 PM")

if __name__ == "__main__":
    main()