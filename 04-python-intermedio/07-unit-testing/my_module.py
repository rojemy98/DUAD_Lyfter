def bubble_sort(my_list):

    if not isinstance(my_list, list):
        raise TypeError("Parameter must be a list")

    if not my_list:
        raise ValueError("The list cannot be empty")

    n = len(my_list)

    for i in range(n - 1):
        for j in range (n - 1 - i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


def sum_list_numbers(numbers):
    accumulator = 0
    for number in numbers:
        accumulator += number
    return accumulator


def reverse_string(text):
    reversed_text = ""
    for character in text:
        reversed_text = character + reversed_text
    return reversed_text


def order_words(text):
    words = text.split("-")
    sorted_words = sorted(words)
    return "-".join(sorted_words)