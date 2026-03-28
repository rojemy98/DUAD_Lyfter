"""

Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar

"""

list_of_numbers = []

print("Please enter 10 numbers")
for i in range (1 , 11):
    number = int(input(f"Enter number {i}: "))
    list_of_numbers.append(number)

number_to_find = int(input("Enter a number to start search: "))
counter = 0

for i in range(len(list_of_numbers)):
    if (number_to_find == list_of_numbers[i]):
        counter += 1

print(f"The number {number_to_find} was found {counter} times")

"""

Cree un programa que verifique si todos los elementos de una lista son positivos

"""

my_list = [3, 6, 0, -2, 4]

all_positive = True

for number in my_list:
    if number <= 0:
        all_positive = False
        break

if (all_positive):
    print("All the numbers in the list are positive")
else:
    print("There is at least one negative number or 0")

"""

Cree un programa que muestre el valor más pequeño de una lista sin usar min().

"""

my_list = [10, 20, 30, 40, 50]
min_number = my_list[0]

for i in range (len(my_list)):
    if (my_list[i] < min_number):
        min_number = my_list[i]
print (f"The lowest value is {min_number}")

"""

Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio

"""

my_list = [10, 20, 30, 40, 50]
greater_than_aver = []

sum = 0
average = 0

for i in range(len(my_list)):
    sum = sum + my_list[i]

average = sum / len(my_list)

print(f"Average: {average}")

for i in range(len(my_list)):
    if (my_list[i] > average):
        greater_than_aver.append(my_list[i])

print(f"New list: {greater_than_aver}")

"""

Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras

"""

words_list = ['sol', 'estrella', 'luz', 'planeta', 'roca']
long_words = []

for word in words_list:
    if len(word) > 4:
        long_words.append(word)

print(long_words)