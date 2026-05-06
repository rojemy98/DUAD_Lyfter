"""
Considere los siguientes dos algoritmos:
"""

def linear_search(my_list, target):
    for item in my_list: # O(N)
        if item == target: # O(1)
            return True # O(1)
    return False # O(1)


def binary_search(my_list, target):
    low = 0 # O(1)
    high = len(my_list) - 1 # O(1)
    while low <= high: # O(log n)
        mid = (low + high) // 2 # O(1)
        if my_list[mid] == target: # O(1)
            return True # O(1)
        elif my_list[mid] < target: # O(1)
            low = mid + 1 # O(1)
        else:
            high = mid - 1 # O(1)
    return False # O(1)


"""
¿Cuál es la complejidad de cada algoritmo?
linear_search: O(N)
binary_search: O(log n)

¿En qué condiciones conviene usar cada uno?

linear_search: Cuando la lista no esta ordenada, listas pequeñas.

binary_search: Cuando la lista ordenada, listas mas grandes.

¿Qué pasa si la lista no está ordenada?

El binary_search puede fallar, los numeros deben de estar ordenados de menor a mayor
porque el algoritmo asume que todo lo que esta a la izquierda es menor y todo lo que esta
a la derecha es mayor.

"""