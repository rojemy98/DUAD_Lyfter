"""
Cree una función que imprima “Hola, [nombre]” dos veces:

Cree un decorador @repeat_twice que haga que la función decorada
se ejecute dos veces seguidas, con los mismos argumentos
"""


def repeat_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@repeat_twice
def say_hello(name):
    print(f"Hello, {name}")