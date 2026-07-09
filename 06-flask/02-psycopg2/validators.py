from flask import request, jsonify


def validate_json():
    """
    Validates that the request contains a valid JSON body.

    Returns:
        tuple:
            - request_body (dict): The parsed JSON body.
            - error (tuple | None): Flask response if validation fails.
    """

    request_body = request.get_json(silent=True)

    if request_body is None:
        return None, (
            jsonify({
                "message": "Body must be valid JSON"
            }),
            400
        )

    if not request_body:
        return None, (
            jsonify({
                "message": "Request body is required"
            }),
            400
        )

    return request_body, None


def validate_required_fields(request_body, required_fields):
    """
    Validates that all required fields are present in the request body.

    Args:
        request_body (dict): JSON payload from the request.
        required_fields (list): List of required field names.

    Returns:
        tuple | None:
            Returns a Flask error response if a field is missing,
            otherwise returns None.
    """

    for field in required_fields:

        if field not in request_body:

            return (
                jsonify({
                    "message": f"{field} is required"
                }),
                400
            )

    return None


def validate_status(request_body, field_name, valid_status):
    """
    Validates that a status field exists and contains a valid value.

    Args:
        request_body (dict): JSON payload from the request.
        field_name (str): Name of the status field.
        valid_status (list): List of accepted status values.

    Returns:
        tuple | None:
            Returns a Flask error response if validation fails,
            otherwise returns None.
    """

    if field_name not in request_body:

        return (
            jsonify({
                "message": f"{field_name} is required"
            }),
            400
        )

    if request_body[field_name] not in valid_status:

        return (
            jsonify({
                "message": "Invalid status value",
                "valid_status": valid_status
            }),
            400
        )

    return None