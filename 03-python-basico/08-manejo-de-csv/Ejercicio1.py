"""

Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
Debe incluir:
Nombre
Género
Desarrollador
Clasificación ESRB

"""


import csv

PATH = r"C:\Users\Usuario\Documents\Lyfter\Tareas\Modulo3 - Python principiantes\videogames.csv"

video_game_headers = (
    "Name",
    "Genre",
    "Developer",
    "ESRB"
)


def games_csv_writer(path):

    try:
        n = int(input("How many video games do you want to enter?: "))

        with open(path, "w", encoding="utf-8", newline="") as file:

            writer = csv.DictWriter(file, fieldnames=video_game_headers)

            writer.writeheader()

            for i in range(n):

                name = input("Enter game name: ")
                genre = input("Enter genre: ")
                developer = input("Enter developer: ")
                esrb = input("Enter ESRB rating: ")

                game = {
                    "Name": name,
                    "Genre": genre,
                    "Developer": developer,
                    "ESRB": esrb
                }

                writer.writerow(game)

        print("Video games saved successfully!")

    except ValueError:
        print("Error: You must enter a valid number.")

    except PermissionError:
        print("Error: You don't have permission to write to this file.")

    except FileNotFoundError:
        print("Error: The file path is invalid.")

    except OSError as error:
        print(f"File system error: {error}")


games_csv_writer(PATH)


"""

Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del
ejercicio dearriba que guarde el archivo separado por tabulaciones en vez de por comas.

"""

import csv

PATH = r"C:\Users\Usuario\Documents\Lyfter\Tareas\Modulo3 - Python principiantes\videogames_tab.csv"

video_game_headers = (
    "Name",
    "Genre",
    "Developer",
    "ESRB"
)


def games_tsv_writer(path):

    try:
        n = int(input("How many video games do you want to enter?: "))

        with open(path, "w", encoding="utf-8", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=video_game_headers,
                delimiter="\t"
            )

            writer.writeheader()

            for i in range(n):

                name = input("Enter game name: ")
                genre = input("Enter genre: ")
                developer = input("Enter developer: ")
                esrb = input("Enter ESRB rating: ")

                game = {
                    "Name": name,
                    "Genre": genre,
                    "Developer": developer,
                    "ESRB": esrb
                }

                writer.writerow(game)

        print("Video games saved successfully!")

    except ValueError:
        print("Error: You must enter a valid number.")

    except PermissionError:
        print("Error: You don't have permission to write to this file.")

    except FileNotFoundError:
        print("Error: The file path is invalid.")

    except OSError as error:
        print(f"File system error: {error}")


games_tsv_writer(PATH)