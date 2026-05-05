"""
Crea un bubble_sort por tu cuenta sin revisar el código de la lección.
"""

def bubble_sort(list):

    n = len(list)

    for i in range(n - 1):
        for j in range (n - 1 - i):
            if list[j] > list[j+1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                print(f"Lista: {list}")
    print(f"Lista ordenada: {list}")
