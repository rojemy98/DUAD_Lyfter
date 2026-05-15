import pytest

from services.validations import (
    validate_text_input,
    validate_amount,
    validate_date
)


# test_validate_text_input_valid
def test_validate_text_input_valid():
    # arrange
    value = "Salary"

    # act
    result = validate_text_input(value)

    # assert
    assert result == "Salary"


# test_validate_text_input_invalid
def test_validate_text_input_invalid():
    # arrange
    value = ""

    # act - assert
    with pytest.raises(ValueError):
        validate_text_input(value)


# test_validate_amount_valid
def test_validate_amount_valid():
    # arrange
    value = "100"

    # act
    result = validate_amount(value)

    # assert
    assert result == 100.0


# test_validate_amount_invalid
def test_validate_amount_invalid():
    # arrange
    value = "abc"

    # act - assert
    with pytest.raises(ValueError):
        validate_amount(value)


# test_validate_date_valid
def test_validate_date_valid():
    # arrange
    value = "01/01/2025"

    # act
    result = validate_date(value)

    # assert
    assert result == "01/01/2025"


# test_validate_date_invalid
def test_validate_date_invalid():
    # arrange
    value = "2025-01-01"

    # act - assert
    with pytest.raises(ValueError):
        validate_date(value)