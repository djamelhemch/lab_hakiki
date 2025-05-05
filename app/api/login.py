from flask import Flask, request, jsonify
import bcrypt
app = Flask(__name__)

# Example user data for testing
users = {
    'testuser': {
        'password_hash': '$2b$12$KIXHJ1bHhp.Sz3IQZRAfbeY52P4g8J17mnCUx3bntDAod.eM5wHNS',  # bcrypt hashed password
    }
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    # Check if the user exists and validate password
    if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]['password_hash'].encode('utf-8')):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
