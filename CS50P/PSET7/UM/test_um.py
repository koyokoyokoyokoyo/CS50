from um import count

def main():
    test_um()
    test_num()
    test_yum()


def test_um():
    assert count("hello, um, um, world.") == 2
    assert count("um, um..... im shy uwu") == 2
    assert count("I um, I like um... um, stuff...") == 3

def test_num():
    assert count("69umum") == 0
    assert count("895674um435763453") == 0
    assert count("9um83434534534") == 0

def test_yum():
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("kyuuuum") == 0
    assert count("kum") == 0
    assert count("chum") == 0