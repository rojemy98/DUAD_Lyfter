"""
Cree una clase de User que:
1. Tenga un atributo de date_of_birth.
2. Tenga un property de age.

Luego cree un decorador para funciones que acepten un User como parámetro
que se encargue de revisar si el User es mayor de edad y arroje una excepción
de no ser así.

"""

from datetime import date


class User:
    def __init__(self, date_of_birth: date):
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year

        # Ajuste si aún no ha cumplido años este año
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age
    

def require_adult_user(func):
    def wrapper(*args, **kwargs):

        # Buscar el User en args o kwargs
        user = None

        # Revisar args
        for arg in args:
            if isinstance(arg, User):
                user = arg
                break

        # Revisar kwargs si no se encontro
        if user is None:
            for value in kwargs.values():
                if isinstance(value, User):
                    user = value
                    break

        # Validar que exista
        if user is None:
            raise ValueError("Function must receive a User object")

        # Validar edad
        if user.age < 18:
            raise ValueError("User must be an adult +18")

        return func(*args, **kwargs)

    return wrapper