"""

Cree un programa que abra un archivo .csv con lainformación
de videojuegos (el que fue generado en el ejercicio 1) y:

Lea cada línea usando csv.reader()
Muestre el contenido en pantalla de forma legible, línea por línea

"""

import csv

PATH = r"C:\Users\Usuario\Documents\Lyfter\Tareas\Modulo3 - Python principiantes\videogames.csv"


def videogames_csv_reader(path):

    try:
        with open(path, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                print(
                    f"Name: {row.get('Name')}\n"
                    f"Genre: {row.get('Genre')}\n"
                    f"Developer: {row.get('Developer')}\n"
                    f"ESRB: {row.get('ESRB')}\n"
                )

    except FileNotFoundError:
        print("Error: The file path is invalid.")

    except PermissionError:
        print("Error: You don't have permission to read this file.")

    except OSError as error:
        print(f"File system error: {error}")

videogames_csv_reader(PATH)


"""

Cree un programa que abra un archivo .csv con la información de
videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:

Lea el archivo CSV de videojuegos
Pida al usuario una clasificación ESRB (por ejemplo: "T")
Muestre todos los videojuegos que tengan esa clasificación

"""


def search_videogames_by_rating(path):

    try:
        with open(path, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            rating = input("Please enter ESRB: ").upper()

            found = False

            for row in reader:

                if row.get("ESRB", "").upper() == rating:
                    print(f"Videogame: {row.get('Name')} ESRB: {row.get('ESRB')}\n")
                    found = True

            if not found:
                print(f"No videogames found with {rating} ESRB rating.")

    except FileNotFoundError:
        print("Error: The file path is invalid.")

    except PermissionError:
        print("Error: You don't have permission to read this file.")

    except csv.Error as error:
        print(f"CSV format error: {error}")

    except OSError as error:
        print(f"File system error: {error}")

search_videogames_by_rating(PATH)



"""

Cree un programa que abra un archivo .csv con la información de
videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:

Lea el archivo .csv con videojuegos
Cuente cuántos videojuegos hay de cada género
Muestre el resultado de forma ordenada

"""


def search_videogames_by_genre(path):

    try:
        with open(path, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            genre_count = {}

            for row in reader:

                genre = row.get("Genre", "Unknown")

                if genre in genre_count:
                    genre_count[genre] += 1
                else:
                    genre_count[genre] = 1

            sorted_genres = sorted(genre_count.items())

            print("\nVideogames by genre:\n")

            for genre, count in sorted_genres:
                print(f"{genre}: {count}")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: You don't have permission to read the file.")

    except csv.Error as error:
        print(f"CSV format error: {error}")

    except OSError as error:
        print(f"File system error: {error}")

search_videogames_by_genre(PATH)


"""

Cree un programa que abra un archivo .csv con la información de
videojuegos( en base al CSV que fue generado en el ejercicio 1) y:

Lea el archivo .csv con videojuegos
Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
Muestre todos los videojuegos desarrollados por esa empresa en formato legible:

"""


def search_games_by_developer(path):
    developer_input = input("Enter developer name: ").strip().lower()
    found = False

    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            print(f"\nVideogames developed by {developer_input.title()}:")

            for row in reader:
                developer = row["Developer"].strip().lower()

                if developer == developer_input:
                    name = row["Name"]
                    genre = row["Genre"]
                    rating = row["ESRB"]

                    print(f"- {name} (Rating: {rating}, Genre: {genre})")
                    found = True

        if not found:
            print("Cannot found videogames for this developer.")

    except FileNotFoundError:
        print("Cannot found the file.")


search_games_by_developer(PATH)