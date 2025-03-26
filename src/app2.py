#!/usr/bin/env python

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App2: Exemplo de PySide6")
        self.button = QPushButton("Carregar aqui!")
        self.setCentralWidget(self.button)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
