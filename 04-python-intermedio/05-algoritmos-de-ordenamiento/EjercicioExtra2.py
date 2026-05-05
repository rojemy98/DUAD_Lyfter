"""
Conteo de pasos (bubble_sort_steps)

Modifique su implementación de bubble_sort para que:
- Cuente cuántas iteraciones (pasadas) realiza el algoritmo
- Cuente cuántos intercambios se hicieron en total
"""

def bubble_sort_steps(list):

    n = len(list)

    iterations = 0
    swaps = 0

    for i in range(n - 1):

        for j in range(n - 1 - i):

            if list[j] > list[j + 1]:

                list[j], list[j + 1] = list[j + 1], list[j]
                swaps += 1

                print(f"Lista: {list}")

        iterations += 1

    print(f"\nLista ordenada: {list}")
    print(f"Iteraciones: {iterations}")
    print(f"Intercambios: {swaps}")