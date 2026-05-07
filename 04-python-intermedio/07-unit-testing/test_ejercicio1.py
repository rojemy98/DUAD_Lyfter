# Ejercicios de Unit Testing
# Python Intermedio

"""
Cree los siguientes unit tests para el algoritmo bubble_sort:

1. Funciona con una lista pequeña.
2. Funciona con una lista grande (de más de 100 elementos.)
3. Funciona con una lista vacía.
4. No funciona con parámetros que no sean una lista.
"""

import pytest
from my_module import bubble_sort, sum_list_numbers, reverse_string, order_words


def test_bubble_sort_with_short_list():
    # arrange
    short_list = [20, 10, 50, 40]

    # act
    result = bubble_sort(short_list)

    #assert
    assert result == [10, 20, 40, 50]


def test_bubble_sort_with_big_list():
    # arrange
    big_list = [
    87, 12, 45, 3, 99, 56, 23, 78, 1, 65,
    34, 90, 11, 67, 42, 18, 73, 5, 29, 84,
    60, 14, 97, 31, 8, 50, 76, 21, 39, 92,
    6, 58, 27, 81, 16, 44, 70, 2, 95, 36,
    53, 19, 88, 25, 63, 10, 74, 41, 7, 86,
    32, 55, 13, 98, 24, 69, 4, 80, 37, 61,
    17, 93, 28, 52, 9, 71, 46, 100, 20, 64,
    35, 82, 15, 57, 30, 96, 43, 66, 22, 79,
    40, 54, 26, 91, 33, 68, 47, 85, 38, 59,
    72, 49, 94, 62, 51, 75, 89, 48, 83, 77
    ]

    # act
    result = bubble_sort(big_list)

    #assert
    assert result == [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100
    ]


def test_bubble_sort_with_empty_list():
    # arrange
    empty_list = []

    # act - assert
    with pytest.raises(ValueError):
        bubble_sort(empty_list) 


def test_bubble_sort_works_only_with_list():
    # arrange
    value = "Test"

    # act - assert
    with pytest.raises(TypeError):
        bubble_sort(value)