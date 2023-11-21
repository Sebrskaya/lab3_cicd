from main import bubble_sort

def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([5, 4, 7, 1, 3]) == [1, 3, 4, 5, 7]