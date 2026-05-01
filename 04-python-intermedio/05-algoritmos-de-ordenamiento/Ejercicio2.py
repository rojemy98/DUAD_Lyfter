"""
Modifica el bubble_sort para que funcione de derecha a izquierda
ordenando los números menores primero
"""

def bubble_sort_reversed(list):

    n = len(list)

    for i in range(n - 1):
        for j in range (n - 1, i, -1):
            if list[j] < list[j-1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                print(f"Lista: {list}")
    print(f"Lista ordenada: {list}")