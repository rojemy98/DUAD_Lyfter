"""
Cree un decorador @requires_login que:

- Verifique si la variable global user_logged_in es True
- Si no lo es, debe lanzar una excepción "Usuario no autenticado"
- Si lo es, la función decorada se ejecuta normalmente
"""

user_logged_in = False


def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise PermissionError("User not authenticated")
        func(*args, **kwargs)
    return wrapper


@requires_login
def view_profile():
    print("Showing user profile")