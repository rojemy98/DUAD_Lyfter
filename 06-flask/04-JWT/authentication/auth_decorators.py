from functools import wraps
from flask import request, jsonify, g


def jwt_required(auth_service):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            token = request.headers.get("Authorization")

            if token is None:
                return jsonify({
                    "message": "Missing token."
                }), 401

            if not token.startswith("Bearer "):
                return jsonify({
                    "message": "Invalid token format."
                }), 401

            try:

                token = token.replace("Bearer ", "")

                decoded = auth_service.decode(token)

                g.user = decoded

            except Exception:

                return jsonify({
                    "message": "Invalid token."
                }), 401

            return func(*args, **kwargs)

        return wrapper

    return decorator

def role_required(*roles):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if g.user["role"] not in roles:

                return jsonify({
                    "message": "Unauthorized access."
                }), 403

            return func(*args, **kwargs)

        return wrapper

    return decorator