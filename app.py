from flask import Flask, jsonify, request

app = Flask(__name__)

# ---------------- Sample employee dataset ----------------
employees = [
    {"id": 401, "name": "Arun",   "designation": "Manager"},
    {"id": 402, "name": "Priya",  "designation": "Developer"},
    {"id": 403, "name": "Kumar",  "designation": "Analyst"},
    {"id": 404, "name": "Divya",  "designation": "HR Executive"},
    {"id": 405, "name": "Sanjay", "designation": "Software Engineer"},
    {"id": 406, "name": "Mari",   "designation": "Database Administrator"},
]


def find_employee(emp_id):
    """Return the employee dict for the given ID, or None."""
    return next((e for e in employees if e["id"] == emp_id), None)


@app.route("/")
def home():
    return jsonify({
        "message": "Employee Management REST API is running",
        "endpoints": {
            "GET    /employees": "Get all employees",
            "GET    /employees/<id>": "Get one employee",
            "POST   /employees": "Add an employee",
            "PUT    /employees/<id>": "Update name and designation",
            "DELETE /employees/<id>": "Delete an employee",
        },
    }), 200


# 1. GET - all employees
@app.route("/employees", methods=["GET"])
def get_all_employees():
    return jsonify({
        "status": "success",
        "message": "Employee details retrieved successfully",
        "count": len(employees),
        "employees": employees,
    }), 200


# 2. GET - single employee by ID
@app.route("/employees/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    emp = find_employee(emp_id)
    if emp is None:
        return jsonify({"status": "error",
                        "message": f"Employee with ID {emp_id} not found"}), 404
    return jsonify({"status": "success",
                    "message": "Employee details retrieved successfully",
                    "employee": emp}), 200


# 3. POST - add new employee
@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json(silent=True)
    if not data or not all(k in data for k in ("id", "name", "designation")):
        return jsonify({"status": "error",
                        "message": "id, name and designation are required"}), 400
    if not isinstance(data["id"], int):
        return jsonify({"status": "error",
                        "message": "id must be an integer"}), 400
    if find_employee(data["id"]) is not None:
        return jsonify({"status": "error",
                        "message": f"Employee with ID {data['id']} already exists"}), 409

    new_emp = {"id": data["id"],
               "name": str(data["name"]).strip(),
               "designation": str(data["designation"]).strip()}
    employees.append(new_emp)
    return jsonify({"status": "success",
                    "message": "Employee added successfully",
                    "employee": new_emp}), 201


# 4. PUT - update name and designation
@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    emp = find_employee(emp_id)
    if emp is None:
        return jsonify({"status": "error",
                        "message": f"Employee with ID {emp_id} not found"}), 404

    data = request.get_json(silent=True)
    if not data or "name" not in data or "designation" not in data:
        return jsonify({"status": "error",
                        "message": "name and designation are required"}), 400

    emp["name"] = str(data["name"]).strip()
    emp["designation"] = str(data["designation"]).strip()
    return jsonify({"status": "success",
                    "message": "Employee updated successfully",
                    "employee": emp}), 200


# 5. DELETE - remove employee
@app.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    emp = find_employee(emp_id)
    if emp is None:
        return jsonify({"status": "error",
                        "message": f"Employee with ID {emp_id} not found"}), 404
    employees.remove(emp)
    return jsonify({"status": "success",
                    "message": f"Employee with ID {emp_id} deleted successfully"}), 200


@app.errorhandler(404)
def not_found(_):
    return jsonify({"status": "error", "message": "URL not found"}), 404


@app.errorhandler(405)
def method_not_allowed(_):
    return jsonify({"status": "error", "message": "HTTP method not allowed"}), 405


if __name__ == "__main__":
    app.run(debug=True, port=5000)
