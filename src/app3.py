#!/usr/bin/env python

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    default_size = QSize(400, 300)

    def __init__(self, title: str):
        super().__init__()
        self.setWindowTitle(title)
        self.button = QPushButton("Carregar aqui!")
        self.button.clicked.connect(self.onButtonClickedTerminal)
        self.button.clicked.connect(self.onButtonClickedGUI)
        self.setFixedSize(MainWindow.default_size)
        self.setCentralWidget(self.button)

    def onButtonClickedTerminal(self):
        print("Olá a todos!")

    def onButtonClickedGUI(self):
        QMessageBox.warning(self, "Cumprimentar", "Olá a todos")
        # mb = QMessageBox(QMessageBox.Information, "Cumprimentar", "Olá a todos!")
        # mb.exec()
#:

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow("App2: Exemplo de PySide6")
    window.show()
    app.exec()
