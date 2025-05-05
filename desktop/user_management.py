from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, 
                            QPushButton, QLabel, QMessageBox)
from PyQt5.QtCore import Qt
import sqlite3

class AddUserDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ajouter un utilisateur")
        self.setGeometry(200, 200, 400, 300)
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Username
        username_layout = QHBoxLayout()
        self.username_label = QLabel("Nom d'utilisateur:")
        self.username_input = QLineEdit()
        username_layout.addWidget(self.username_label)
        username_layout.addWidget(self.username_input)
        
        # Email
        email_layout = QHBoxLayout()
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        email_layout.addWidget(self.email_label)
        email_layout.addWidget(self.email_input)
        
        # Password
        password_layout = QHBoxLayout()
        self.password_label = QLabel("Mot de passe:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Enregistrer")
        self.cancel_button = QPushButton("Annuler")
        self.save_button.clicked.connect(self.save_user)
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)
        
        # Add all layouts to main layout
        layout.addLayout(username_layout)
        layout.addLayout(email_layout)
        layout.addLayout(password_layout)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def save_user(self):
        username = self.username_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        
        if not all([username, email, password]):
            QMessageBox.warning(self, "Erreur", "Tous les champs sont obligatoires!")
            return
        
        try:
            # Connect to SQLite database
            conn = sqlite3.connect('lab_database.db')
            cursor = conn.cursor()
            
            # Create users table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL)
            ''')
            
            # Insert new user
            cursor.execute('''
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
            ''', (username, email, password))
            
            conn.commit()
            QMessageBox.information(self, "Succès", "Utilisateur ajouté avec succès!")
            self.accept()
            
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Erreur", "Nom d'utilisateur ou email déjà existant!")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Une erreur est survenue: {str(e)}")
        finally:
            conn.close()