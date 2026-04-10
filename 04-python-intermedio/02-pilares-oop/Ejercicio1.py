"""
Cree una clase de BankAccount que:

1. Tenga un atributo de balance.
2. Tenga un método para ingresar dinero.
3. Tengo un método para retirar dinero.

Cree otra clase que herede de esta llamada SavingsAccount que:

2. Tenga un atributo de min_balance que se pueda asignar al crearla.
3. Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance.
Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.

"""


class BankAccount:
    def __init__(self, balance=0.0):
        self._balance = balance  # protegido

    def deposit_money(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self._balance += amount

    def withdraw_money(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than 0")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, min_balance, balance=0.0):
        super().__init__(balance)
        self._min_balance = min_balance  # protegido

    def withdraw_money(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than 0")

        if self._balance - amount < self._min_balance:
            raise ValueError("Cannot withdraw: minimum balance would be violated")

        self._balance -= amount


"""

Cree una clase abstracta de Shape que:

1. Tenga los métodos abstractos de calculate_perimeter y calculate_area.
2. Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

"""


from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4  

    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.base + self.height)

    def calculate_area(self):
        return self.base * self.height
    

"""

Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

R/
Combinar comportamientos (mixins)
Reutilizar código de múltiples fuentes
Sistemas con múltiples roles

"""


class TimestampMixin:
    def get_timestamp(self):
        from datetime import datetime
        return datetime.now()


class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")


class Order(LoggerMixin, TimestampMixin):
    def create_order(self):
        self.log(f"Order created at {self.get_timestamp()}")
