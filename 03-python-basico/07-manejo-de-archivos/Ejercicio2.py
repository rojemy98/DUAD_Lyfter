"""
Cree un programa que lea un archivo con texto línea por línea, quite los saltos
de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo
"""

PATH = r"C:\Users\Usuario\Documents\Lyfter\Tareas\Modulo3 - Python principiantes\Ejercicio14.txt"
PATH_2 = r"C:\Users\Usuario\Documents\Lyfter\Tareas\Modulo3 - Python principiantes\Ejercicio14_Una_Linea.txt"


def removes_line_breaks(path):
    words = []

    try:
        with open(path) as file:
            for line in file:
                line = line.replace("\n", " ")
                words.append(line)

        return words

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: You don't have permission to read this file.")

    except OSError as error:
        print(f"File error: {error}")


def write_one_line(path, words):
    try:
        with open(path, "w") as file:
            file.writelines(words)

    except PermissionError:
        print("Error: You don't have permission to write to this file.")

    except OSError as error:
        print(f"File error: {error}")


words = removes_line_breaks(PATH)
write_one_line(PATH_2, words)


"""
Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
"""


def words_counter(path):
    try:
        with open(path) as file:
            text = file.read()
            words = text.split()

        print(f"The file contains {len(words)} words")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: You don't have permission to read this file.")

    except OSError as error:
        print(f"File error: {error}")


words_counter(PATH_2)


"""
Cree un programa que:
Lea un archivo línea por línea
Convierta cada línea a mayúsculas
Escriba el contenido en un nuevo archivo
"""


def upper_case_converter(path):
    upper_words = []

    try:
        with open(path) as file:
            for word in file:
                upper_words.append(word.upper())

        return upper_words

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: You don't have permission to read this file.")

    except OSError as error:
        print(f"File error: {error}")


def write_upper_words(path, words):
    try:
        with open(path, "w") as file:
            file.writelines(words)

    except PermissionError:
        print("Error: You don't have permission to write to this file.")

    except OSError as error:
        print(f"File error: {error}")


words = upper_case_converter(PATH)
write_upper_words(PATH_2, words)


"""
Cree un programa que:
Pida al usuario una línea de texto
Agregue esa línea al final de un archivo existente
Si el archivo no existe, lo crea automáticamente
"""


def append_text_to_file(path):
    try:
        text = input("Enter text to append to file: ")

        with open(path, "a") as file:
            file.write("\n" + text)

        print("Text added to file successfully!!")

    except PermissionError:
        print("Error: You don't have permission to write to this file.")

    except OSError as error:
        print(f"File error: {error}")


append_text_to_file(PATH_2)