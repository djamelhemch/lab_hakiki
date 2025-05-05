from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
import requests

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Connexion")
        self.setGeometry(400, 200, 400, 200)

        # Layout for the login dialog
        self.layout = QVBoxLayout()

        # Label that displays login instruction or error message
        self.label = QLabel("Veuillez entrer vos identifiants")
        self.layout.addWidget(self.label)

        # Username input field
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Nom d'utilisateur")
        self.layout.addWidget(self.username_input)

        # Password input field (masked input)
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Mot de passe")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        # Login button to trigger the authentication
        self.login_button = QPushButton("Se connecter")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        # Set the layout for the dialog window
        self.setLayout(self.layout)

    def login(self):
        # Get the username and password entered by the user
        username = self.username_input.text()
        password = self.password_input.text()

        # Call the validate_credentials function to authenticate the user
        if self.validate_credentials(username, password):
            self.accept()  # Close the login dialog on successful login
        else:
            # Display an error message if the credentials are incorrect
            self.label.setText("Identifiants incorrects!")

    def validate_credentials(self, username, password):
        # Send a POST request to the Flask backend to validate credentials
        response = requests.post('http://127.0.0.1:5000/api/login', json={
            'username': username,
            'password': password
        })
        
        # Check the response from the Flask backend
        if response.status_code == 200:
            return True
        else:
            return False
