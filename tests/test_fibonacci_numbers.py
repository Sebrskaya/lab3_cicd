from main import fibonacci_numbers
def test_fibonacci_numbers():
    assert fibonacci_numbers(0) == []
    assert fibonacci_numbers(1) == [0]
    assert fibonacci_numbers(2) == [0, 1]
    assert fibonacci_numbers(5) == [0, 1, 1, 2, 3]