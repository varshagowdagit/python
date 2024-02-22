from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample user data
users = [
    {"id": 1, "name": "User1", "age": 25, "email": "user1@example.com"},
    {"id": 2, "name": "User2", "age": 30, "email": "user2@example.com"},
]

# 1. Create Users
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the User API"})

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify({"message": "User created successfully", "user": new_user}), 201

# 2. Read User Data
@app.route('/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# 3. Update User Data
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        user.update(request.get_json())
        return jsonify({"message": "User updated successfully", "user": user})
    return jsonify({"message": "User not found"}), 404

# 4. Delete a Few Attributes of User Data
@app.route('/users/<int:user_id>/delete-attributes', methods=['PATCH'])
def delete_user_attributes(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        attributes_to_delete = request.get_json().get('attributes', [])
        for attribute in attributes_to_delete:
            user.pop(attribute, None)
        return jsonify({"message": "Attributes deleted successfully", "user": user})
    return jsonify({"message": "User not found"}), 404

# 5. Delete User Records Completely
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
