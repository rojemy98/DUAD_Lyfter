"""
Cree una función que se llame multiply, la cual obtiene dos valores
y los multiplica entre si

A esta función se le debe combinar dos decoradores:
@log_call: imprime el nombre de la función, los argumentos, fecha actual
y el retorno
@validate_numbers: revisa que todos los argumentos sean numéricos
"""

from functools import wraps
from datetime import datetime


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(
            f"Function name: {func.__name__}\n"
            f"Function arguments: Positional args - {args} || Keyword args - {kwargs}\n"
            f"Date: {datetime.now()}\n"
            f"Function return: {result}\n"
        )
        return result
    return wrapper


def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Validates positional args
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Invalid argument: {arg} is not a number")
        
        # Validates keyword args
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"Invalid argument: {key}={value} is not a number")
        
        return func(*args, **kwargs)
    
    return wrapper


@log_call
@validate_numbers
def multiply(a,b):
    return a*b