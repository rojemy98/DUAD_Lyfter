"""
Analice el algoritmo de bubble_sort usando la Big O Notation.
"""

def bubble_sort(list):

    n = len(list) # O(1)

    for i in range(n - 1): # O(n)
        for j in range (n - 1 - i): # O(n^2)
            if list[j] > list[j+1]: # O(1)
                list[j], list[j + 1] = list[j + 1], list[j] # O(1)
                print(f"Lista: {list}") # O(1)
    print(f"Lista ordenada: {list}") # O(1)