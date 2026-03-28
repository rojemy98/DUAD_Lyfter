"""

Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé,
niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

"""

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if (age <= 2):
    print(f"{name} {last_name} you are a Baby")
elif (age > 2 and age <= 10):
    print(f"{name} {last_name} you are a kid")
elif (age > 10 and age <= 12):
    print(f"{name} {last_name} you are a preteen")
elif (age > 12 and age <= 18):
    print(f"{name} {last_name} you are a teenager")
elif (age > 18 and age <= 29):
    print(f"{name} {last_name} you are a young adult")
elif (age > 29 and age <= 59):
    print(f"{name} {last_name} you are an adult")
elif (age > 59):
    print(f"{name} {last_name} you are an older adult")

"""

Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse
hasta que el usuario adivine el numero.

"""

import random

secret_number = random.randint(1, 10)

user_number = int(input("Guess the secret number, Enter a number from 1 to 10: "))

while(user_number != secret_number):
    print("Wrong number, try again")
    user_number = int(input("Guess the secret number, Enter a number from 1 to 10: "))
print(f"Congratulations!! the secret number is {secret_number}")

"""

Cree un programa que le pida tres números al usuario y muestre el mayor.

"""

print("Please enter 3 numbers")
number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))
number_3 = int(input("Number 3: "))

if number_1 == number_2 and number_1 == number_3:
    print(f"All 3 numbers are the same: {number_1, number_2, number_3}")
elif number_1 >= number_2 and number_1 >= number_3:
    print(f"The number {number_1} is the largest")
elif number_2 >= number_1 and number_2 >= number_3:
    print(f"The number {number_2} is the largest")
else:
    print(f"The number {number_3} is the largest")

"""

Dada n cantidad de notas de un estudiante, calcular:
Cuantas notas tiene aprobadas (mayor a 70).
Cuantas notas tiene desaprobadas (menor a 70).
El promedio de todas.
El promedio de las aprobadas.
El promedio de las desaprobadas.

"""
total_grades = int(input("Enter the quantity of grades: "))

if total_grades <= 0:
    print("No grades entered.")
else:
    grades_counter = 1
    total_sum = 0
    approved_sum = 0
    failed_sum = 0
    number_of_approved_grades = 0
    number_of_failed_grades = 0

    while grades_counter <= total_grades:
        actual_grade = int(input(f"Enter the grade number {grades_counter}: "))
        grades_counter += 1

        total_sum += actual_grade

        if actual_grade < 70:
            number_of_failed_grades += 1
            failed_sum += actual_grade
        else:
            number_of_approved_grades += 1
            approved_sum += actual_grade

    average_of_total_grades = total_sum / total_grades

    average_of_failed_grades = (
        failed_sum / number_of_failed_grades
        if number_of_failed_grades > 0 else 0
    )

    average_of_approved_grades = (
        approved_sum / number_of_approved_grades
        if number_of_approved_grades > 0 else 0
    )

    print(f"The student has {number_of_approved_grades} approved grades")
    print(f"The average of approved grades is: {average_of_approved_grades}")

    print(f"The student has {number_of_failed_grades} failed grades")
    print(f"The average of failed grades is: {average_of_failed_grades}")

    print(f"The total grades average is: {average_of_total_grades}")



