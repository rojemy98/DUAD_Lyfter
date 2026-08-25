from .auth_routes import create_auth_blueprint
from .product_routes import create_products_blueprint


__all__ = [
    "create_auth_blueprint",
    "create_products_blueprint",
]