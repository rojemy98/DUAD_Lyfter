from flask import Flask, jsonify, request, g

# Database
from database.database_connection import DatabaseConnection

# Redis
from cache.redis_connection import CacheManager

# Repositories
from repositories.users_repository import UsersRepository
from repositories.products_repository import ProductsRepository
from repositories.invoices_repository import InvoicesRepository
from repositories.invoice_products_repository import InvoiceProductsRepository
from repositories.contacts_repository import ContactsRepository
from repositories.login_history_repository import LoginHistoryRepository

# Services
from services.purchase_service import PurchaseService

# Authentication
from authentication.auth_service import JWT_Manager
from authentication.auth_decorators import jwt_required, role_required

from database.models import UserRole

from datetime import timedelta

import jwt

import json


# ======================================================
# Database configuration
# ======================================================

db_manager = DatabaseConnection(
    user="postgres",
    password="Nyjah2022_",
    host="localhost",
    database="postgres",
    port="5432"
)

session = db_manager.create_session()


# ======================================================
# Redis configuration
# ======================================================


cache_manager = CacheManager(
    host="PLACEHOLDER",
    port=17262,
    password="PLACEHOLDER",
    decode_responses=True
)


# ======================================================
# Flask application
# ======================================================


app = Flask(__name__)
app.json.sort_keys = False


# ======================================================
# Application dependencies
# ======================================================

# Repositories
users_repo = UsersRepository(session)
products_repo = ProductsRepository(session)
invoices_repo = InvoicesRepository(session)
invoice_products_repo = InvoiceProductsRepository(session)
contact_repo = ContactsRepository(session)
login_history_repo = LoginHistoryRepository(session)

# Services
purchase_service = PurchaseService(
    session=session,
    products_repo=products_repo,
    invoices_repo=invoices_repo,
    invoice_products_repo=invoice_products_repo
)

# Authentication
auth_service = JWT_Manager("RS256")


# ======================================================
# Global error handlers
# ======================================================


@app.errorhandler(ValueError)
def handle_value_error(error):
    return jsonify({
        "message": str(error)
    }), 400


@app.errorhandler(PermissionError)
def handle_permission_error(error):
    return jsonify({
        "message": str(error)
    }), 403


@app.errorhandler(LookupError)
def handle_lookup_error(error):
    return jsonify({
        "message": str(error)
    }), 404


@app.errorhandler(Exception)
def handle_exception(error):
    return jsonify({
        "message": "Internal server error.",
        "error": str(error)
    }), 500


# ======================================================
# Authentication endpoints
# ======================================================


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    user = users_repo.insert_user(data)

    token = auth_service.encode(
        {
            "id": user.id,
            "role": user.role,
            "type": "access"
        },
        expires_in=timedelta(minutes=15)
    )

    return jsonify({
        "access_token": token
    }), 201


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Request body is required."
        }), 400

    email = data.get("email")
    password = data.get("password")

    if email is None or password is None:
        return jsonify({
            "message": "Email and password are required."
        }), 400

    user = users_repo.get_user_by_email(email)

    ip_address = request.remote_addr or "127.0.0.1"

    if user is None:

        login_history_repo.insert_login_history(
            user_id=None,
            ip_address=ip_address,
            success=False
        )

        return jsonify({
            "message": "Invalid credentials."
        }), 401
    
    result = users_repo.get_user(email, password)

    if result is None:

        login_history_repo.insert_login_history(
            user_id=user.id,
            ip_address=ip_address,
            success=False
        )

        return jsonify({
            "message": "Invalid credentials."
        }), 401
    
    login_history_repo.insert_login_history(
        user_id=user.id,
        ip_address=ip_address,
        success=True
    )

    access_token = auth_service.encode(
        {
            "id": user.id,
            "role": user.role,
            "type": "access"
        },
        expires_in=timedelta(minutes=15)
    )

    refresh_token = auth_service.encode(
        {
            "id": user.id,
            "type": "refresh"
        },
        expires_in=timedelta(days=7)
    )

    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token
    }), 200


@app.route("/refresh-token", methods=["POST"])
def refresh_token():

    data = request.get_json()

    if not data or not data.get("refresh_token"):
        return jsonify({
            "message": "Refresh token is required."
        }), 400

    token = data["refresh_token"]

    try:

        decoded = auth_service.decode(token)

        if decoded.get("type") != "refresh":
            return jsonify({
                "message": "Invalid refresh token."
            }), 401

        user = users_repo.get_user_by_id(
            decoded["id"]
        )

        new_access_token = auth_service.encode(
            {
                "id": user.id,
                "role": user.role,
                "type": "access"
            },
            expires_in=timedelta(minutes=15)
        )

        return jsonify({
            "access_token": new_access_token
        }), 200

    except jwt.ExpiredSignatureError:

        return jsonify({
            "message": "Refresh token has expired. Please login again."
        }), 401

    except jwt.InvalidTokenError:

        return jsonify({
            "message": "Invalid refresh token."
        }), 401


@app.route("/login-history", methods=["GET"])
@jwt_required(auth_service)
@role_required("ADMIN")
def get_login_history():

    history = login_history_repo.get_all_login_history()

    return jsonify(
        [
            record.to_dict()
            for record in history
        ]
    ), 200
    

@app.route('/me')
@jwt_required(auth_service)
def me():

    user = users_repo.get_user_by_id(
        g.user["id"]
    )

    return jsonify(user.to_dict()), 200
    

# ======================================================
# Product endpoints
# ======================================================


@app.route("/products", methods=["GET"])
@jwt_required(auth_service)
@role_required("ADMIN")
def get_products():

        products = products_repo.get_products()

        return jsonify(
            [product.to_dict() for product in products]
        ), 200


@app.route("/products/<int:product_id>", methods=["GET"])
@jwt_required(auth_service)
@role_required("ADMIN")
def get_product_by_id(product_id):

        cached_data = cache_manager.get_data(f"product:{product_id}")

        if cached_data is None:

            product = products_repo.get_product_by_id(product_id)

            product_data = product.to_dict()

            cache_manager.store_data(f"product:{product_id}", json.dumps(product_data))

            return jsonify(product_data), 200

        return jsonify(json.loads(cached_data)), 200


@app.route("/products", methods=["POST"])
@jwt_required(auth_service)
@role_required("ADMIN")
def create_product():

        data = request.get_json()

        new_product = products_repo.insert_product(data)

        return jsonify(new_product.to_dict()), 201


@app.route("/products/<int:product_id>", methods=["PUT"])
@jwt_required(auth_service)
@role_required("ADMIN")
def update_product_by_id(product_id):

        data = request.get_json()

        updated_product = products_repo.update_product(
            product_id,
            data
        )

        cache_manager.delete_data(f"product:{updated_product.id}")

        return jsonify(updated_product.to_dict()), 200


@app.route("/products/<int:product_id>", methods=["DELETE"])
@jwt_required(auth_service)
@role_required("ADMIN")
def delete_product_by_id(product_id):

        deleted_product = products_repo.delete_product(product_id)

        cache_manager.delete_data(f"product:{deleted_product.id}")

        return jsonify(deleted_product), 200


@app.route("/purchase", methods=["POST"])
@jwt_required(auth_service)
def purchase():

    invoice = purchase_service.purchase(
        user_id=g.user["id"],
        products=request.get_json()["products"]
    )

    return jsonify(invoice.to_dict()), 201


@app.route("/invoices", methods=["GET"])
@jwt_required(auth_service)
def get_my_invoices():

    invoices = invoices_repo.get_invoices_by_user(g.user["id"])

    return jsonify(
        [invoice.to_dict() for invoice in invoices]
    ), 200


@app.route("/admin/invoices", methods=["GET"])
@jwt_required(auth_service)
@role_required("ADMIN")
def get_all_invoices():

    invoices = invoices_repo.get_all_invoices()

    return jsonify(
        [invoice.to_dict() for invoice in invoices]
        ), 200


# ======================================================
# Contacts endpoints
# ======================================================


@app.route("/contacts", methods=["GET"])
@jwt_required(auth_service)
def get_user_contacts():

    contacts = contact_repo.get_contacts_by_user(g.user["id"])

    return jsonify(
        [contact.to_dict() for contact in contacts]
    ), 200


@app.route("/contacts", methods=["POST"])
@jwt_required(auth_service)
def create_contact():

    data = request.get_json()

    contact = contact_repo.insert_contact(
        user_id=g.user["id"],
        data=data
    )

    return jsonify(contact.to_dict()), 201


@app.route("/contacts/<contact_id>", methods=["PUT"])
@jwt_required(auth_service)
def update_contact(contact_id):

    data = request.get_json()

    contact = contact_repo.update_contact_by_user(
        contact_id=contact_id,
        user_id=g.user["id"],
        data=data
    )

    return jsonify(contact.to_dict()), 200


@app.route("/contacts/<int:contact_id>", methods=["DELETE"])
@jwt_required(auth_service)
def delete_user_contact(contact_id):

    deleted_contact = contact_repo.delete_contact_by_user(
        contact_id=contact_id,
        user_id=g.user["id"]
    )

    return jsonify(deleted_contact), 200


@app.route("/admin/contacts", methods=["GET"])
@jwt_required(auth_service)
@role_required("ADMIN")
def get_all_contacts():

    contacts = contact_repo.get_all_contacts()

    return jsonify(
        [contact.to_dict() for contact in contacts]
    ), 200


@app.route("/admin/contacts/<contact_id>", methods=["DELETE"])
@jwt_required(auth_service)
@role_required("ADMIN")
def delete_contact(contact_id):

    deleted_contact = contact_repo.delete_contact(contact_id)

    return jsonify(deleted_contact), 200


# ======================================================
# Application entry point
# ======================================================


if __name__ == "__main__":
    app.run(host="localhost", debug=True)