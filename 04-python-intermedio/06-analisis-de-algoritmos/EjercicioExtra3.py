"""
Analice la siguiente función:
"""

def print_all_pairs(my_dict):
    for key1 in my_dict: # O(n)
        for key2 in my_dict: # O(n^2)
            print(f"{key1}-{key2}") # O(1)


"""
Preguntas:

¿Cuál es la complejidad temporal?
O(n^2) = n * n

¿Cuanto dura si hay 1 millón de claves?

n = 1,000,000
n * n = 1,000,000,000,000
"""