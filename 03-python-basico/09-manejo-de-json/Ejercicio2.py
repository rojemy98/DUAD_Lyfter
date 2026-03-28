import json

PATH = r"C:\Users\Usuario\Documents\Lyfter\Tareas\Modulo3 - Python principiantes\Pokemons.json"

"""

Cree un programa que abra un archivo .json con la información de Pokémon
( en base al JSON que fue generado en el ejercicio 1) y:

1. Lea el archivo JSON de Pokémon
2. Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)

"""


def show_pokemons(path):

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

            for row in data:
                print(f"Name: {row['name']['english']}\n"
                      f"Level: {row['level']}\n"
                      f"Type: {row['type']}\n")

    except FileNotFoundError:
        print("File not found.")

    except json.JSONDecodeError:
        print("JSON is empty or corrupted.")

    except KeyError as e:
        print(f"Missing key in JSON data: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")


show_pokemons(PATH)

"""

Cree un programa que abra un archivo .json con la información de Pokémon
( en base al JSON que fue generado en el ejercicio 1) y:

1. Lea el archivo JSON de Pokémon
2. Pida al usuario un tipo de Pokémon
3. Muestre todos los Pokémon que sean de ese tipo

"""


def pokemons_by_type(path):

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        pokemon_type_input = input("Enter Pokemon type to search: ").strip().lower()

        pokemon_list = []

        for row in data:
            types = [t.lower() for t in row["type"]]

            if pokemon_type_input in types:
                pokemon_list.append(row["name"]["english"])

        if pokemon_list:
            print("Pokemons found:")
            for name in pokemon_list:
                print(f"- {name}")
        else:
            print("No Pokemons found with that type.")

    except FileNotFoundError:
        print("File not found.")

    except json.JSONDecodeError:
        print("JSON is empty or corrupted.")

    except KeyError as e:
        print(f"Missing key in JSON data: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")


pokemons_by_type(PATH)

"""

Cree un programa que abra un archivo .json con la información de Pokémon
( en base al JSON que fue generado en el ejercicio 1) y:

1. Lea el archivo JSON de Pokémon
2. Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)

"""


def show_pokemons_stats(path):

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

            for row in data:
                print(f"Name: {row['name']['english']}\n"
                      f"Attack: {row['base']['Attack']}\n"
                      f"Defense: {row['base']['Defense']}\n"
                      f"Speed: {row['base']['Speed']}\n")

    except FileNotFoundError:
        print("File not found.")

    except json.JSONDecodeError:
        print("JSON is empty or corrupted.")

    except KeyError as e:
        print(f"Missing key in JSON data: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
            

show_pokemons_stats(PATH)

"""

Cree un programa que abra un archivo .json con la información de Pokémon
( en base al JSON que fue generado en el ejercicio 1) y:


1. Lea el archivo JSON
2. Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
3. Calcule y muestre el promedio de nivel para cada tipo:

"""


def average_level_by_type(path):

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        type_levels = {}

        for row in data:
            level = row["level"]
            types = row["type"]

            for t in types:
                t = t.lower()

                if t not in type_levels:
                    type_levels[t] = []

                type_levels[t].append(level)

        for t, levels in type_levels.items():
            avg = sum(levels) / len(levels)
            print(f"Type: {t.capitalize()} → Average Lvl: {avg:.1f}")

    except FileNotFoundError:
        print("File not found.")

    except json.JSONDecodeError:
        print("JSON is empty or corrupted.")

    except KeyError as e:
        print(f"Missing key in JSON data: {e}")

    except TypeError:
        print("Data type error in JSON (expected numbers or lists).")

    except Exception as e:
        print(f"Unexpected error: {e}")


average_level_by_type(PATH)