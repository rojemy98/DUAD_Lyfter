"""

Cree un programa que:

Pida al usuario su nombre

Si el nombre es numérico (isdigit()), haga raise ValueError

"""


name = input("Enter your name: ")

if name.isnumeric():
    raise ValueError("The name cannot be a number")


"""


Luego pida su edad

Si no es un número válido, capture el ValueError


"""


try:
    age = int(input("How old are you? : "))

except ValueError:
    print("Enter a valid number")

else:

    """
    Si todo sale bien imprima el mensaje
    """
    print(f"Hello {name}, you are {age} years old")



"""

Cree una función convertir_a_entero(lista) que:
Reciba una lista de strings
Intente convertir cada elemento a entero usando int()
Use try-except para atrapar los errores ValueError
Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás

"""


my_list = ['4', 'hola', '10', '5.2']

def convert_to_int(list_of_strings):
    for word in list_of_strings:

        try:
            number = int(word)
            print(f"'{word}' converted to {number}")

        except ValueError:
            print(f"Not possible to convert => {word}")


convert_to_int(my_list)


"""

Cree una función sumar_valores(lista) que:
Reciba una lista de elementos (strings, enteros, flotantes mezclados)
Intente convertir cada elemento a tipo float
Si puede, sume el valor y muestre: "<valor> sumado correctamente"
Si no puede, muestre: "Elemento inválido: <valor>"
Al final, imprima la suma total
Ejemplo:

"""

my_list = ['10', 'manzana', '5.5', '3', 'n/a']

def sum_values(list):
    total = 0
    for value in list:
        try:
            number = float(value)
            total = total + number
            print (f"'{value}' added successfully")
        except ValueError:
            print(f"Invalid value: {value}")
    print(f"Total sum: {total}")

sum_values(my_list)
