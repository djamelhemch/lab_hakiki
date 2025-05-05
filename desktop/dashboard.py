from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget
from PyQt5.QtCore import Qt

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tableau de bord")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.label = QLabel("Bienvenue sur le tableau de bord")
        self.layout.addWidget(self.label)

        # Add buttons for different features
        self.patients_button = QPushButton("Gestion des patients")
        self.samples_button = QPushButton("Gestion des échantillons")
        self.reports_button = QPushButton("Rapports")

        self.layout.addWidget(self.patients_button)
        self.layout.addWidget(self.samples_button)
        self.layout.addWidget(self.reports_button)

        # Set central widget
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
