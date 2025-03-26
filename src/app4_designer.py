# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app4_designer.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(661, 310)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbNome = QLabel(self.centralwidget)
        self.lbNome.setObjectName(u"lbNome")
        self.lbNome.setGeometry(QRect(20, 25, 131, 16))
        self.leNome = QLineEdit(self.centralwidget)
        self.leNome.setObjectName(u"leNome")
        self.leNome.setGeometry(QRect(70, 25, 241, 21))
        self.pbIntroduzir = QPushButton(self.centralwidget)
        self.pbIntroduzir.setObjectName(u"pbIntroduzir")
        self.pbIntroduzir.setGeometry(QRect(320, 20, 100, 32))
        self.pbIntroduzir.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 661, 43))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Exemplo Designer", None))
        self.lbNome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.leNome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome completo...", None))
        self.pbIntroduzir.setText(QCoreApplication.translate("MainWindow", u"Introduzir", None))
    # retranslateUi

