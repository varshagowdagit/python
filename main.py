from flask import Flask, request, jsonify, make_response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from functools import wraps

app = Flask(__name__)

# Secret key for JWT (replace with a secure key in production)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Sample data to simulate a database
users = {
    1: {"id": 1, "username": "john_doe", "password": "password123", "role": "user"},
    2: {"id": 2, "username": "admin", "password": "adminpass", "role": "admin"}
}

# Sample roles for RBAC
roles = {
    "user": ["read"],
    "admin": ["read", "write", "delete"]
}

# Function to generate a unique user ID
def generate_user_id():
    return max(users.keys()) + 1 if users else 1

# Decorator for role-based authorization
def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user['role'] not in allowed_roles:
                return jsonify({"message": "Access forbidden. Insufficient role."}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator

# User Sign Up
@app.route('/signup', methods=['POST'])
def user_signup():
    data = request.get_json()
    existing_user = next((user for user in users.values() if user["username"] == data["username"]), None)
    if existing_user:
        return jsonify({"message": "Username already exists. Please choose another."}), 400

    user_id = generate_user_id()
    data['id'] = user_id
    users[user_id] = data
    return jsonify({"message": "User created successfully", "user_id": user_id}), 201

# User Sign In
@app.route('/signin', methods=['POST'])
def user_signin():
    data = request.get_json()
    user = next((user for user in users.values() if user["username"] == data["username"] and user["password"] == data["password"]), None)
    if user:
        access_token = create_access_token(identity={"id": user["id"], "username": user["username"], "role": user["role"]})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Forgot Password (Just a placeholder, in real-world scenario, this should send a reset link to the user's email)
@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    user = next((user for user in users.values() if user["username"] == data["username"]), None)
    if user:
        return jsonify({"message": "Password reset link sent to the registered email"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

# Sample endpoint requiring authentication and specific role
@app.route('/secure-endpoint', methods=['GET'])
@jwt_required()
@role_required(allowed_roles=["admin"])
def secure_endpoint():
    return jsonify({"message": "You have access to this secure endpoint"}), 200

if __name__ == '__main__':
    app.run(debug=True)
