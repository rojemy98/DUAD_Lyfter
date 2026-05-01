"""
Validación de entrada antes de ordenar

Cree una función que reciba una lista y valide:
- Que todos los elementos sean números
- Que no esté vacía
- Luego aplique bubble_sort si pasa las validaciones
- Si hay error, debe lanzar un mensaje apropiado
"""

list = [5,12,1,7]

def bubble_sort(list):

    n = len(list)

    for i in range(n - 1):
        for j in range (n - 1 - i):
            if list[j] > list[j+1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                print(f"Lista: {list}")
    print(f"Lista ordenada: {list}")

def validated_bubble_sort(list):

    #Valida que no esté vacía
    if len(list) == 0:
        print("Error: The list is empty")
        return

    #Valida que todos los elementos sean números
    for item in list:
        if not isinstance(item, (int, float)):
            print("Error: The list contains no numeric elements")
            return

    bubble_sort(list)