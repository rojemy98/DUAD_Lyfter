from flask import Flask

from config import (
    load_private_key,
    load_public_key,
    JWT_ALGORITHM,
    JWT_ACCESS_TOKEN_EXPIRES,
)

from database.db_manager import DatabaseManager

from routes import (
    create_auth_blueprint,
    create_products_blueprint,
    create_carts_blueprint
)

from services import JWTManager


DATABASE_URL = (
    "postgresql+psycopg://postgres:Nyjah2022_@localhost:5432/postgres"
)


def create_app():
    app = Flask(__name__)

    db_manager = DatabaseManager(DATABASE_URL)

    jwt_manager = JWTManager(
        private_key=load_private_key(),
        public_key=load_public_key(),
        algorithm=JWT_ALGORITHM,
        access_token_expires=JWT_ACCESS_TOKEN_EXPIRES
    )

    auth_blueprint = create_auth_blueprint(
        db_manager,
        jwt_manager
    )

    products_blueprint = create_products_blueprint(
        db_manager,
        jwt_manager
    )

    carts_blueprint = create_carts_blueprint(
        db_manager,
        jwt_manager
    )

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(products_blueprint)
    app.register_blueprint(carts_blueprint)

    return app


app = create_app()
app.json.sort_keys = False


if __name__ == "__main__":
    app.run(debug=True)