from flask import Flask, jsonify, request
from utils import load_json_file_to_python, save_python_to_json_file, validate_allowed_status_in_request

app = Flask(__name__)


# Get all tasks
@app.route("/tasks")
def return_all_tasks():

    status = request.args.get("status")

    tasks = load_json_file_to_python("tasks_list.json")

    if status:
        filtered_tasks = []

        for task in tasks:
            if task["Status"] == status:
                filtered_tasks.append(task)

        return jsonify(filtered_tasks)

    return jsonify(tasks)


# Create a new task
@app.route("/tasks", methods=["POST"])
def insert_task():

    # Read request body
    new_task = request.get_json()

    # Basic validation: body must exist
    if not new_task:
        return jsonify({"message": "Invalid request body"}), 400

    # Required fields validation
    required_fields = ["Id", "Title", "Description", "Status"]

    for field in required_fields:
        if field not in new_task:
            return jsonify({"message": f"Missing field: {field}"}), 400

        # Prevent empty values
        if new_task[field] is None or str(new_task[field]).strip() == "":
            return jsonify({"message": f"Field '{field}' cannot be empty"}), 400

    # Validate allowed status values
    validate_allowed_status_in_request(new_task)

    # Load existing tasks
    tasks = load_json_file_to_python("tasks_list.json")

    # Check duplicate ID
    for task in tasks:
        if task["Id"] == new_task["Id"]:
            return jsonify({"message": "Task with this ID already exists"}), 400

    # Add new task
    tasks.append(new_task)

    # Save file
    save_python_to_json_file(tasks, "tasks_list.json")

    return jsonify({
        "message": "Task added successfully",
        "task": new_task
    }), 201


# Edit a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def edit_task(task_id):

    # Read JSON data sent in the request body
    updated_data = request.get_json()

    # Validate allowed status values
    validate_allowed_status_in_request(updated_data)

    # Load existing tasks from the JSON file
    tasks = load_json_file_to_python("tasks_list.json")

    # Search for the task by ID and update its fields
    for task in tasks:
        if task["Id"] == task_id:

            # Update only provided fields (keep old values if not sent)
            task["Title"] = updated_data.get("Title", task["Title"])
            task["Description"] = updated_data.get("Description", task["Description"])
            task["Status"] = updated_data.get("Status", task["Status"])

            break
    else:
        # Return error if task is not found
        return jsonify({"message": "Task not found"}), 404

    # Save updated tasks list back to the JSON file
    save_python_to_json_file(tasks, "tasks_list.json")

    # Return success response
    return jsonify({
        "message": "Task updated successfully",
        "task": task
    })


# Delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    # Load existing tasks from the JSON file
    tasks = load_json_file_to_python("tasks_list.json")

    # Search for the task to delete
    for task in tasks:
        if task["Id"] == task_id:
            tasks.remove(task)
            break
    else:
        # Return error if task is not found
        return jsonify({"message": "Task not found"}), 404

    # Save updated list after deletion
    save_python_to_json_file(tasks, "tasks_list.json")

    # Return success response
    return jsonify({
        "message": "Task deleted successfully",
        "deleted_id": task_id
    })


if __name__ == "__main__":
    # Run Flask application in debug mode for development
    app.run(host="localhost", debug=True)