#!/usr/bin/env python

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

from app4_designer import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbIntroduzir.clicked.connect(self.onIntroduzirClicked)

    def onIntroduzirClicked(self):
        txt = self.leNome.text()
        QMessageBox.information(self, "", f"Introduziu: {txt}")  # type: ignore


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
