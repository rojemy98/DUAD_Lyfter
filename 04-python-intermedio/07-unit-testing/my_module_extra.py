def calculate_average(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    return sum(numbers) / len(numbers)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def find_max_number(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number

    return max_number


def divide(number1, number2):
    if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
        raise TypeError("Parameters must be numeric")
    if number2 == 0:
        raise ValueError("Cannot be divided by zero")
    return number1 / number2


def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()