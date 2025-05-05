import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt
from login_dialogue import LoginDialog # Assuming this is the login dialog file
from dashboard import DashboardWindow  # Assuming this is your dashboard file
# Add this import at the top
from user_management import AddUserDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Système de gestion de laboratoire")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
       
        # Adding a simple label and button to demonstrate
        self.label = QLabel("Bienvenue au système de gestion de laboratoire")
        self.layout.addWidget(self.label)
        self.add_user_button = QPushButton("Ajouter un utilisateur")
        self.add_user_button.clicked.connect(self.open_user_management)
        self.layout.addWidget(self.add_user_button)

        self.button = QPushButton("Se connecter")
        self.button.clicked.connect(self.open_login_dialog)
        self.layout.addWidget(self.button)

        # Set central widget
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

    def open_login_dialog(self):
        self.login_dialog = LoginDialog(self)
        if self.login_dialog.exec_() == 1:  # If login is successful
            self.open_dashboard()

    def open_dashboard(self):
        self.dashboard_window = DashboardWindow()
        self.dashboard_window.show()
    def open_user_management(self):
        dialog = AddUserDialog(self)
        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Initialize the QApplication
    main_window = MainWindow()  # Create the MainWindow instance
    main_window.show()  # Show the main window
    sys.exit(app.exec_())  # Start the event loop
