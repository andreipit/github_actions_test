def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

def test_not_failing():
    assert func(3) == 4