import pytest
from fuel import convert, gauge

def main():
    test_fuel()

def test_fuel():
    with pytest.raises(ValueError):
        convert("5/4")
    assert convert("1/2") == 50.0
    assert gauge(67) == "67%"

if __name__ == "__main__":
    main()