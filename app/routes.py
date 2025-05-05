from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:test123@localhost/lab_management_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return jsonify({"status": "success", "message": "Login successful"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401

# Example endpoint for adding a new patient
@app.route('/api/patient', methods=['POST'])
def add_patient():
    data = request.json
    # Normally you would validate and process data
    patient = Patient(name=data['name'], email=data['email'])
    db.session.add(patient)
    db.session.commit()
    return jsonify({"status": "success", "message": "Patient added"}), 201

if __name__ == '__main__':
    db.create_all()  # Creates database tables
    app.run(debug=True)
