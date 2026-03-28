"""

Cree un diccionario que guarde la siguiente información sobre un hotel:
nombre
numero_de_estrellas
habitaciones


El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
numero
piso
precio_por_noche

"""

hotel_information = {
    "name": "Hotel RIU",
    "stars": 5,
    "rooms": [
        {
            "number": 100,
            "floor": 1,
            "price_per_night": 120.0,
        },
        {
            "number": 101,
            "floor": 1,
            "price_per_night": 120.0,
        },
        {
            "number": 200,
            "floor": 2,
            "price_per_night": 230.0,
        },
    ]
}

print(hotel_information)

"""

Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
Ejemplos:
list_a = [’first_name’, ‘last_name’, ‘role’]
list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]
→ {’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}

"""

list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']

my_dict = {}

for i in range(len(list_a)):
    my_dict[list_a[i]] = list_b[i]

print(my_dict)


"""

Cree un programa que use una lista para eliminar keys de un diccionario.
Ejemplos:
list_of_keys = [’access_level’, ‘age’]
employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}
→ {’name’: ‘John’, 'email’: ‘john@ecorp.com’}

"""
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

list_of_keys = ["access_level", "age"]

for keys in list_of_keys:
    employee.pop(keys)

print(employee)