import math

"""

Cree una clase de Circle con:

1. Un atributo de radius (radio).
2. Un método de get_area que retorne su área.

"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * (self.radius ** 2)
        return area


"""

Cree una clase de Bus con:

1. Un atributo de max_passengers.
2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección).
Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
3. Un método para bajar pasajeros uno por uno (en cualquier orden).

"""


class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = [] 

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)

            available_seats = self.max_passengers - len(self.passengers)

            print(f"{person.name} added successfully. Seats available: {available_seats}")
        else:
            print("The bus is full, cannot add another person")
    
    def get_passenger_off(self):
        if not self.passengers:
            print("The bus is empty")
        else:
            removed = self.passengers.pop()
            print(f"{removed.name} removed from the bus")



"""

Cree las siguientes clases:

Head
Torso
Arm
Hand
Leg
Feet

Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.

"""

class Head:
    def __init__(self):
        self.eyes = 2
        self.ears = 2
        self.nose = 1
        self.mouth = 1


class Hand:
    def __init__(self):
        self.fingers = 5


class Arm:
    def __init__(self):
        self.hand = Hand()


class Feet:
    def __init__(self):
        self.toes = 5


class Leg:
    def __init__(self):
        self.feet = Feet()


class Torso:
    def __init__(self):
        self.heart = 1
        self.lungs = 2

        self.left_arm = Arm()
        self.right_arm = Arm()

        self.left_leg = Leg()
        self.right_leg = Leg()


class Human:
    def __init__(self):
        self.head = Head()
        self.torso = Torso()