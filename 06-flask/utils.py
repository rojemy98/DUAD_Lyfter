from flask import jsonify
import json

def load_json_file_to_python(path):
    """
    Read a JSON file and return its contents as a Python object.
    """
    with open(path, "r") as file:
        return json.load(file)


def save_python_to_json_file(data, path):
    """
    Save a Python object to a JSON file.
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def validate_allowed_status_in_request(data):
    """
    Validates that the Status value provided in the request
    is one of the allowed task statuses (Todo, In Progress, Completed).
    """
    valid_status = ["Todo", "In Progress", "Completed"]

    if data["Status"] not in valid_status:
        return jsonify({
            "message": "Invalid status value",
            "valid_status": valid_status
        }), 400