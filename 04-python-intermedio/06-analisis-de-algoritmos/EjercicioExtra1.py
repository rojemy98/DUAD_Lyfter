"""
Los siguientes dos algoritmos hacen lo mismo: calcular la suma de
los primeros n números naturales
"""

# Versión 1:

def manual_add(number):
    result = 0 # O(1)
    for i in range(1, number + 1): # O(n)
        result += i # O(1)
    return result # O(1)


# Versión 2:

def add_formula(number):
    return number * (number + 1) // 2 # O(1)


# Preguntas:

"""
¿Cuál es la complejidad de cada versión?

Version 1 : O(n)
Version 2 : O(1)


¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?

R/ Usaria la version 2.

Porque si utlizo la version 1 el for se tendria que ejecutar
1 000 000 000 de veces lo cual alargaria el tiempo de ejecucion
"""
