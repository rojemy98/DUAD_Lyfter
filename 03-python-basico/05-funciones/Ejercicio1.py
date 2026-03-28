"""

Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

Experimente con el concepto de scope:


"""


def second_function():
    print("Hello second function")


def first_function():
    print("Hello first function")
    second_function()


first_function()


"""

Intente acceder a una variable definida dentro de una función desde afuera.
Intente acceder a una variable global desde una función y cambiar su valor.

"""


counter = 10


def my_function():
    global counter
    counter = counter + 1


my_function()

print(counter)


"""

Cree una función que retorne la suma de todos los números de una lista.
La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
[4, 6, 2, 29] → 41

"""


def sum_list_numbers(numbers):
    accumulator = 0
    for number in numbers:
        accumulator += number
    return accumulator


print(sum_list_numbers([4, 6, 2, 29]))


"""

Cree una función que le dé la vuelta a un string y lo retorne.

"""


def reverse_string(text):
    reversed_text = ""
    for character in text:
        reversed_text = character + reversed_text
    return reversed_text


print(reverse_string("Hola mundo"))


"""

Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.

"""


def count_letters(text):
    uppercase_count = 0
    lowercase_count = 0

    for character in text:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1

    print(f"There’s {uppercase_count} upper cases and {lowercase_count} lower cases")


count_letters("Hola Mundo")


"""

Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.

Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.

“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

"""


def order_words(text):
    words = text.split("-")
    sorted_words = sorted(words)
    return "-".join(sorted_words)


print(order_words("python-variable-funcion-computadora-monitor"))


"""

Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]

"""


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def prime_numbers_selector(list_numbers):
    list_prime_numbers = []

    for number in list_numbers:
        if is_prime(number):
            list_prime_numbers.append(number)

    return list_prime_numbers


print(prime_numbers_selector([1, 4, 6, 7, 13, 9, 67]))