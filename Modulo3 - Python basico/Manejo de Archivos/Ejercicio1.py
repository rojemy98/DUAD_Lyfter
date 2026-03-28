"""
Cree un programa que lea nombres de canciones de un archivo (línea por línea)
y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
"""

SONGS_PATH = r"C:\Users\Usuario\Documents\Lyfter\Tareas\Modulo3 - Python principiantes\songs.txt"
SORTED_SONGS_PATH = r"C:\Users\Usuario\Documents\Lyfter\Tareas\Modulo3 - Python principiantes\sorted_songs.txt"


def read_and_sort_file(path):
    songs = []

    try:
        with open(path) as file:
            for line in file.readlines():
                songs.append(line)

        songs.sort()
        return songs

    except FileNotFoundError:
        print("Error: The file was not found.")

    except PermissionError:
        print("Error: You don't have permission to read this file.")

    except OSError as error:
        print(f"File error: {error}")


def write_new_file(path, songs):

    try:
        with open(path, "w") as file:
            file.writelines(songs)

    except PermissionError:
        print("Error: You don't have permission to write to this file.")

    except OSError as error:
        print(f"File error: {error}")


try:
    songs = read_and_sort_file(SONGS_PATH)

    if songs is not None:
        write_new_file(SORTED_SONGS_PATH, songs)

except Exception as error:
    print(f"Unexpected error: {error}")