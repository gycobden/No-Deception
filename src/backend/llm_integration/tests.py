#sample test - raghavi for CI build system trigger
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


# sample test - chi for CI build system trigger
def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

def test_even():
    assert isEven(2) == True
    assert isEven(3) == False