from flask import Flask, jsonify, request

from db import PgManager

from repositories import (
    UserRepository,
    CarRepository,
    RentalRepository
)

from validators import (
    validate_json,
    validate_required_fields,
    validate_status
)

from constants import (
    CAR_STATUS,
    USER_STATUS,
    RENTAL_STATUS
)


app = Flask(__name__)
app.json.sort_keys = False


# Database configuration
db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="Nyjah2022_",
    host="localhost"
)


# Repository instances
users_repo = UserRepository(db_manager)
cars_repo = CarRepository(db_manager)
rentals_repo = RentalRepository(db_manager)


# ======================================================
# User endpoints
# ======================================================

@app.route("/users", methods=["POST"])
def create_user():
    """
    Create a new user.
    """

    request_body, error = validate_json()

    if error:
        return error

    error = validate_required_fields(
        request_body,
        [
            "name",
            "last_name",
            "username",
            "email",
            "password",
            "birthdate"
        ]
    )

    if error:
        return error

    new_user = users_repo.create_user(request_body)

    if not new_user:
        return jsonify({
            "message": "Error creating user"
        }), 500

    return jsonify(new_user), 201


# ======================================================
# Car endpoints
# ======================================================

@app.route("/cars", methods=["POST"])
def create_car():
    """
    Create a new car.
    """

    request_body, error = validate_json()

    if error:
        return error

    error = validate_required_fields(
        request_body,
        [
            "brand",
            "model",
            "manufacturing_year"
        ]
    )

    if error:
        return error

    new_car = cars_repo.create_car(request_body)

    if not new_car:
        return jsonify({
            "message": "Error creating car"
        }), 500

    return jsonify(new_car), 201


# ======================================================
# Rental endpoints
# ======================================================

@app.route("/rentals", methods=["POST"])
def create_rental():
    """
    Create a new rental.
    """

    request_body, error = validate_json()

    if error:
        return error

    error = validate_required_fields(
        request_body,
        [
            "user_id",
            "car_id"
        ]
    )

    if error:
        return error

    if "rental_status" in request_body:

        error = validate_status(
            request_body,
            "rental_status",
            RENTAL_STATUS
        )

        if error:
            return error

    new_rental = rentals_repo.create_rental(request_body)

    if not new_rental:
        return jsonify({
            "message": "Error creating rental"
        }), 400

    return jsonify(new_rental), 201

# ======================================================
# Update car status
# ======================================================

@app.route("/cars/<int:car_id>/status", methods=["PUT"])
def update_car_status(car_id):
    """
    Update the status of an existing car.
    """

    request_body, error = validate_json()

    if error:
        return error

    error = validate_status(
        request_body,
        "car_status",
        CAR_STATUS
    )

    if error:
        return error

    updated_car = cars_repo.update_car_status(
        car_id,
        request_body["car_status"]
    )

    if not updated_car:
        return jsonify({
            "message": "Error updating car status"
        }), 400

    return jsonify(updated_car), 200


# ======================================================
# Update user status
# ======================================================

@app.route("/users/<int:user_id>/status", methods=["PUT"])
def update_user_status(user_id):
    """
    Update the status of an existing user.
    """

    request_body, error = validate_json()

    if error:
        return error

    error = validate_status(
        request_body,
        "user_status",
        USER_STATUS
    )

    if error:
        return error

    updated_user = users_repo.update_user_status(
        user_id,
        request_body["user_status"]
    )

    if not updated_user:
        return jsonify({
            "message": "Error updating user status"
        }), 400

    return jsonify(updated_user), 200


# ======================================================
# Complete rental
# ======================================================

@app.route("/rentals/<int:rental_id>/complete", methods=["PUT"])
def complete_rental(rental_id):
    """
    Mark a rental as completed.
    """

    completed_rental = rentals_repo.complete_rental(rental_id)

    if not completed_rental:
        return jsonify({
            "message": "Error completing rental"
        }), 400

    return jsonify(completed_rental), 200


# ======================================================
# Update rental status
# ======================================================

@app.route("/rentals/<int:rental_id>/status", methods=["PUT"])
def update_rental_status(rental_id):
    """
    Update the status of an existing rental.
    """

    request_body, error = validate_json()

    if error:
        return error

    error = validate_status(
        request_body,
        "rental_status",
        RENTAL_STATUS
    )

    if error:
        return error

    updated_rental = rentals_repo.update_rental_status(
        rental_id,
        request_body["rental_status"]
    )

    if not updated_rental:
        return jsonify({
            "message": "Error updating rental status"
        }), 400

    return jsonify(updated_rental), 200


# ======================================================
# Suspend user
# ======================================================

@app.route("/users/<int:user_id>/suspend", methods=["PUT"])
def suspend_user(user_id):
    """
    Suspend an existing user.
    """

    request_body, error = validate_json()

    if error:
        return error

    error = validate_status(
        request_body,
        "user_status",
        USER_STATUS
    )

    if error:
        return error

    if request_body["user_status"] != "Suspended":
        return jsonify({
            "message": "User status must be 'Suspended'"
        }), 400

    suspended_user = users_repo.update_user_status(
        user_id,
        request_body["user_status"]
    )

    if not suspended_user:
        return jsonify({
            "message": "Error suspending user"
        }), 400

    return jsonify(suspended_user), 200

# ======================================================
# Get all users
# ======================================================

@app.route("/users", methods=["GET"])
def return_all_users():
    """
    Retrieve all users with optional filters.
    """

    filters = request.args.to_dict()

    users = users_repo.get_all(filters)

    return jsonify(users), 200


# ======================================================
# Get all cars
# ======================================================

@app.route("/cars", methods=["GET"])
def return_all_cars():
    """
    Retrieve all cars with optional filters.
    """

    filters = request.args.to_dict()

    cars = cars_repo.get_all(filters)

    return jsonify(cars), 200

# ======================================================
# Get all rentals
# ======================================================

@app.route("/rentals", methods=["GET"])
def return_all_rentals():
    """
    Retrieve all rentals with optional filters.
    """

    filters = request.args.to_dict()

    rentals = rentals_repo.get_all(filters)

    return jsonify(rentals), 200


# ======================================================
# Application entry point
# ======================================================

if __name__ == "__main__":
    app.run(
        host="localhost",
        debug=True
    )