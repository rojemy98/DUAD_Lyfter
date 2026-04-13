"""
Cree un decorador que haga print de los parámetros y retorno de la función que decore.
"""


def print_args_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Positional Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"Result: {result}")
        
        return result
    return wrapper