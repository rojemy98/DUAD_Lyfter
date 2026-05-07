# Ejercicios extra de Unit Testing
# Python Intermedio

"""
Cree un test que:
1. Valide que dividir(10, 2) retorna 5.0
2. Verifique que dividir por cero lanza un ValueError
3. Valide que dividir con un string como parámetro también lanza TypeError
"""

import pytest
from my_module_extra import divide


def test_divide_valid_numbers():
    # arrange
    number1 = 10
    number2 = 2

    # act
    result = divide(number1, number2)

    # assert
    assert result == 5.0


def test_divide_by_zero_raises_value_error():
    # arrange
    number1 = 10
    number2 = 0

    # act & assert
    with pytest.raises(ValueError, match="Cannot be divided by zero"):
        divide(number1, number2)


def test_divide_with_string_raises_type_error():
    # arrange
    number1 = "10"
    number2 = 2

    # act & assert
    with pytest.raises(TypeError):
        divide(number1, number2)