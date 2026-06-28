from bank import bank

def main():
    test_bank()

def test_bank():
    assert bank("hello") == "$0"
    assert bank("howdy") == "$20"
    assert bank("ball") == "$100"

if __name__ == "__main__":
    main()