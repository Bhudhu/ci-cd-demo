from app import add, subtract

def test_add():
    assert add(2, 3) == 7

def test_subtract():
    assert subtract(10, 4) == 6
