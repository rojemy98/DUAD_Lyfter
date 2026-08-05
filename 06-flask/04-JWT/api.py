from flask import Flask, jsonify, request, g

# Database
from database.database_connection import DatabaseConnection

# Repositories
from repositories.users_repository import UsersRepository
from repositories.products_repository import ProductsRepository
from repositories.invoices_repository import InvoicesRepository
from repositories.invoice_products_repository import InvoiceProductsRepository
from repositories.contacts_repository import ContactsRepository

# Services
from services.purchase_service import PurchaseService

# Authentication
from authentication.auth_service import JWT_Manager
from authentication.auth_decorators import jwt_required, role_required

from database.models import UserRole


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


@app.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    data["role"] = UserRole.USER
    user = users_repo.insert_user(data)
    token = auth_service.encode({
        "id": user.id,
        "role": user.role
    })
    return jsonify(token=token), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if(data.get('email') == None or data.get('password') == None):
        return jsonify(status=400), 400
    else:
        result = users_repo.get_user(data.get('email'), data.get('password'))

        if(result == None):
            return jsonify(status=401), 401
        else:
            token = auth_service.encode({
                "id": result.id,
                "role": result.role
            })
            return jsonify(token=token), 200
        

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


@app.route("/products")
@jwt_required(auth_service)
@role_required("ADMIN")
def get_products():

        products = products_repo.get_products()

        return jsonify(
            [product.to_dict() for product in products]
        ), 200


@app.route("/products/<int:product_id>")
@jwt_required(auth_service)
@role_required("ADMIN")
def get_product_by_id(product_id):

        product = products_repo.get_product_by_id(product_id)

        return jsonify(product.to_dict()), 200


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

        return jsonify(updated_product.to_dict()), 200


@app.route("/products/<int:product_id>", methods=["DELETE"])
@jwt_required(auth_service)
@role_required("ADMIN")
def delete_product_by_id(product_id):

        deleted_product = products_repo.delete_product(product_id)

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


@app.route("contacts", methods=["GET"])
def get_user_contacts():

    contacts = contact_repo.get_contacts_by_user(g.user["id"])

    return jsonify(
        [contact.to_dict() for contact in contacts]
    ), 200


@app.route("contacts", methods=["POST"])
def create_contact():
    pass


@app.route("contacts/<contact_id>", methods=["PUT"])
def update_contact(contact_id):
    pass


@app.route("contacts/<contact_id>", methods=["DELETE"])
def delete_user_contact(contact_id):
    pass


@app.route("/admin/contacts", methods=["GET"])
def get_all_contacts():
    pass


@app.route("contacts/<contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    pass

# ======================================================
# Application entry point
# ======================================================


if __name__ == "__main__":
    app.run(host="localhost", debug=True)