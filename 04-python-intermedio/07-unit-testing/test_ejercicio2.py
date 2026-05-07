# Ejercicios de Unit Testing
# Python Intermedio

"""
Cree unit tests para probar 3 casos de éxito distintos de cada
uno de los ejercicios de funciones (exceptuando el 1 y 2).
"""

from my_module import sum_list_numbers, reverse_string, order_words


# sum_list_numbers

def test_sum_list_numbers_with_valid_numbers():
    # arrange
    numbers = [1, 2, 3, 4]

    # act
    result = sum_list_numbers(numbers)

    # assert
    assert result == 10


def test_sum_list_numbers_with_empty_list():
    # arrange
    numbers = []

    # act
    result = sum_list_numbers(numbers)

    # assert
    assert result == 0


def test_sum_list_numbers_with_negative_numbers():
    # arrange
    numbers = [-1, -2, 3]

    # act
    result = sum_list_numbers(numbers)

    # assert
    assert result == 0


# reverse_string

def test_reverse_string_with_normal_text():
    # arrange
    text = "hello"

    # act
    result = reverse_string(text)

    # assert
    assert result == "olleh"


def test_reverse_string_with_single_character():
    # arrange
    text = "a"

    # act
    result = reverse_string(text)

    # assert
    assert result == "a"


def test_reverse_string_with_empty_string():
    # arrange
    text = ""

    # act
    result = reverse_string(text)

    # assert
    assert result == ""


# order_words

def test_order_words_with_multiple_words():
    # arrange
    text = "banana-apple-cherry"

    # act
    result = order_words(text)

    # assert
    assert result == "apple-banana-cherry"


def test_order_words_with_already_sorted_words():
    # arrange
    text = "apple-banana-cherry"

    # act
    result = order_words(text)

    # assert
    assert result == "apple-banana-cherry"

    
def test_order_words_with_single_word():
    # arrange
    text = "banana"

    # act
    result = order_words(text)

    # assert
    assert result == "banana"