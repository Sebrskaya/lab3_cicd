from main import calculator
import pytest
def test_calculator():
    assert calculator(2, 3, '+') == 5
    assert calculator(5, 2, '-') == 3
    assert calculator(4, 3, '*') == 12
    assert calculator(8, 2, '/') == 4
    with pytest.raises(ValueError):
        calculator(1, 0, '/')  # Тест деления на ноль
    with pytest.raises(ValueError):
        calculator(1, 2, '%')  # Тест с недопустимым оператором