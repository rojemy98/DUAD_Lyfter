"""

Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

"""

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for i in range(len(first_list)):
    print(f"{first_list[i]} {second_list[i]}")

"""

Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

"""

my_string = "Pizza con piña"

for i in range(len(my_string) -1, -1, -1):
    print(my_string[i])

"""

Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

"""
my_list = [4, 3, 6, 1, 7]

if len(my_list) < 2:
    print("There is only 1 number in the list")
else:
    temp = my_list[0]
    my_list[0] = my_list[-1]
    my_list[-1] = temp

print(my_list)

"""

Cree un programa que elimine todos los números impares de una lista.

"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(my_list) - 1, -1, -1):
    if(my_list[i] % 2 != 0):
        my_list.pop(i)
print(my_list)

"""

Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

"""

list_of_numbers = []

print("Please enter 10 numbers")
for i in range (1 , 11):
    number = int(input(f"Enter number {i}: "))
    list_of_numbers.append(number)

largest_number = list_of_numbers[0]

for i in range (len(list_of_numbers)):
    if (list_of_numbers[i] > largest_number):
        largest_number = list_of_numbers[i]

print(list_of_numbers)
print(f"The largest number is: {largest_number}")