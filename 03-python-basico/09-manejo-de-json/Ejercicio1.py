"""

Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON
(https://learning.lyfter.team/dashboard/roadmap/fffab4f1-5c3f-480a-9671-ae1a235c3b6a/dac6b243-2cab-496f-96de-5debb9ce613e)

1. Debe leer el archivo para importar los Pokémones existentes.
2. Luego debe pedir la información del Pokémon a agregar.
3. Finalmente debe guardar el nuevo Pokémon en el archivo.

"""

import json

PATH = r"C:\Users\Usuario\Documents\Lyfter\Tareas\Modulo3 - Python principiantes\Pokemons.json"

def add_pokemon(path):

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found. Creating a new one...")
        data = []
    except json.JSONDecodeError:
        print("JSON is empty or corrupted. Initializing new list...")
        data = []

    try:
        name = input("Enter Pokemon name: ")
        level = int(input("Enter level: "))
        pokemon_type = input("Enter type: ")
        hp = int(input("Enter HP: "))
        attack = int(input("Enter Attack: "))
        defense = int(input("Enter Defense: "))
        sp_attack = int(input("Enter Sp. Attack: "))
        sp_defense = int(input("Enter Sp. Defense: "))
        speed = int(input("Enter Speed: "))

    except ValueError:
        print("Invalid input. Numbers were expected.")
        return

    new_pokemon = {
        "name": {
            "english": name
        },
        "level": level,
        "type": [pokemon_type],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

    data.append(new_pokemon)

    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("Pokemon added successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")


add_pokemon(PATH)