import pytest
from seasons import validate_date

def test_season():
    with pytest.raises(ValueError):
        assert validate_date("barkmeow")
        assert validate_date("1234")
        assert validate_date("January 1, 1990")