"""

Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto

"""

def character_counter(text, character):
    counter = 0

    for char in text:
        if char == character:
            counter += 1
    return counter

print(character_counter("hello", "l"))


"""

Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras

"""


def filter_words_longer_than(list_of_words, n):
    filtered_words = []

    for word in list_of_words:
        if len(word) > n:
            filtered_words.append(word)
    
    return filtered_words

print(filter_words_longer_than(["cielo", "sol", "maravilloso", "día"],4))


"""

Cree una función que reciba un string y retorne cuántas vocales contiene

"""


def vocals_counter(text):
    list_vocals = ["a","e","i","o","u","A","E","I","O","U"]
    counter = 0
    
    for i in text:
        for j in list_vocals:
            if i == j:
                counter += 1
    
    return counter

print(vocals_counter("Hola Mundo"))