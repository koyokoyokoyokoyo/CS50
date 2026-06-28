from plates import is_valid

def main():
    test_valid()

def test_valid():
    assert is_valid("GOODBYE") == False
    assert is_valid("CS50") == True
    assert is_valid("I AM A CAT MEOW MEOW") == True

if __name__ == "__main__":
    main()