"""
Cree un decorador que se encargue de revisar si todos los parámetros de la
función que decore son números, y arroje una excepción de no ser así.
"""

def validate_numeric_args_only(func):
    def wrapper(*args, **kwargs):
        
        for value in args:
            if not isinstance(value, (int, float)):
                raise ValueError("This function contains numeric arguments")
            
        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise ValueError("This function contains numeric arguments")
            
        return func(*args, **kwargs)

    return wrapper