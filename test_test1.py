from test1 import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(6, 2) == 3.0
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5.0
    assert divide(0, 5) == 0.0

def test_divide_by_zero():
    assert divide(5, 0) == "Error: Division by zero is not allowed."
def test_all_tests():
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    print("All tests passed successfully.")

    print("Testing complete!")