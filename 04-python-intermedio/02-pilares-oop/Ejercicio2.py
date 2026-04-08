"""

Cree una clase Employee con los siguientes requisitos:

1. Atributos privados: _name, _salary

2. Use @property y @<atributo>.setter para:
    Mostrar el nombre y el salario
    Validar que el salario nunca sea negativo

Cree un método promote que aumente el salario un porcentaje definido

"""


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary

    @name.setter
    def name(self, name):
        self._name = name

    @salary.setter
    def salary(self, amount):
        if amount < 0:
            raise ValueError("The amount of salary could not be less than 0")
        self._salary = amount

    def promote(self, percentage = 0.1):
        self.salary = self.salary * (1 + percentage)


"""

Cree una clase abstracta User con los siguientes métodos abstractos:
1. get_role()
2. has_permission(permission)

Luego cree dos clases que hereden de ella:
1. AdminUser
2. RegularUser

Cada una debe implementar los métodos
Por ejemplo:
AdminUser siempre tiene permisos
RegularUser solo tiene permisos limitados ("read", por ejemplo)

"""


from abc import ABC, abstractmethod


class User(ABC):

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):

    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return True


class RegularUser(User):

    def get_role(self):
        return "regular"

    def has_permission(self, permission):
        return permission == "read"
    

"""

Cree una clase base Vehicle con los atributos:
_brand
_year

Agregue un método get_info() que devuelva una descripción del vehículo.

Luego cree dos clases hijas:
Car
Motorcycle

Cada una debe agregar su propio atributo (por ejemplo, doors o type) y
sobrescribir el método get_info() para incluir esta información adicional.

"""


class Vehicle:

    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"{self._brand} ({self._year})"


class Car(Vehicle):

    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self._doors = doors

    def get_info(self):
        return f"{self._brand} ({self._year}) - {self._doors} doors"


class Motorcycle(Vehicle):

    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self._type = type

    def get_info(self):
        return f"{self._brand} ({self._year}) - Type: {self._type}"