from functools import wraps
from flask import request, jsonify, g
import jwt


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

            token = token.replace("Bearer ", "")

            try:

                decoded = auth_service.decode(token)

                g.user = decoded

            except jwt.ExpiredSignatureError:

                return jsonify({
                    "message": "Token has expired."
                }), 401

            except jwt.InvalidTokenError:

                return jsonify({
                    "message": "Invalid token."
                }), 401

            return func(*args, **kwargs)

        return wrapper

    return decorator