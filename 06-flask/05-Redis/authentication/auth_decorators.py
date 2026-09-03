import jwt
from functools import wraps
from flask import request, jsonify, g


def jwt_required(auth_service):

    def decorator(f):

        @wraps(f)
        def wrapper(*args, **kwargs):

            token = request.headers.get("Authorization")

            if not token:
                return jsonify({
                    "message": "Missing authorization token."
                }), 401

            if not token.startswith("Bearer "):
                return jsonify({
                    "message": "Invalid authorization format."
                }), 401

            token = token.replace("Bearer ", "", 1)

            try:

                decoded = auth_service.decode(token)

                if decoded.get("type") != "access":
                    return jsonify({
                        "message": "Access token required."
                    }), 401

                g.user = decoded

                return f(*args, **kwargs)

            except jwt.ExpiredSignatureError:

                return jsonify({
                    "message": "Access token has expired."
                }), 401

            except jwt.InvalidTokenError:

                return jsonify({
                    "message": "Invalid access token."
                }), 401

        return wrapper

    return decorator

def role_required(required_role):

    def decorator(f):

        @wraps(f)
        def wrapper(*args, **kwargs):

            if not hasattr(g, "user") or g.user is None:
                return jsonify({
                    "message": "Authentication required."
                }), 401

            user_role = g.user.get("role")

            if user_role != required_role:
                return jsonify({
                    "message": "Unauthorized access."
                }), 403

            return f(*args, **kwargs)

        return wrapper

    return decorator