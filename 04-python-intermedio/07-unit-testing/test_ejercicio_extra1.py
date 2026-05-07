# Ejercicios extra de Unit Testing
# Python Intermedio

"""
Cree una clase de pruebas que contenga al menos 3 funciones que operen con números (como suma, promedio, conversión, etc.) y escriba:
Un caso con números positivos
Un caso con números negativos
Un caso con ceros
"""

from my_module_extra import calculate_average, celsius_to_fahrenheit, find_max_number

# Casos con numeros positivos

# calculate_average
def test_average_with_positive_numbers():
    # arrange
    numbers = [10, 20, 30]

    # act
    result = calculate_average(numbers)

    # assert
    assert result == 20


# celsius_to_fahrenheit
def test_celsius_to_fahrenheit_with_positive_numbers():
    # arrange
    celsius = 25

    # act
    result = celsius_to_fahrenheit(celsius)

    # assert
    assert result == 77


# find_max_number
def test_find_max_with_positive_numbers():
    # arrange
    numbers = [5, 10, 15]

    # act
    result = find_max_number(numbers)

    # assert
    assert result == 15


# Casos con numeros positivos

# calculate_average
def test_average_with_negative_numbers():
    # arrange
    numbers = [-10, -20, -30]

    # act
    result = calculate_average(numbers)

    # assert
    assert result == -20


# celsius_to_fahrenheit
def test_celsius_to_fahrenheit_with_negative_numbers():
    # arrange
    celsius = -10

    # act
    result = celsius_to_fahrenheit(celsius)

    # assert
    assert result == 14


# find_max_number
def test_find_max_with_negative_numbers():
    # arrange
    numbers = [-5, -10, -3]

    # act
    result = find_max_number(numbers)

    # assert
    assert result == -3


# Casos con ceros

# calculate_average
def test_average_with_zeros():
    # arrange
    numbers = [0, 0, 0]

    # act
    result = calculate_average(numbers)

    # assert
    assert result == 0


# celsius_to_fahrenheit
def test_celsius_to_fahrenheit_with_zero():
    # arrange
    celsius = 0

    # act
    result = celsius_to_fahrenheit(celsius)

    # assert
    assert result == 32


# find_max_number
def test_find_max_with_zeros():
    # arrange
    numbers = [0, 0, 0]

    # act
    result = find_max_number(numbers)

    # assert
    assert result == 0