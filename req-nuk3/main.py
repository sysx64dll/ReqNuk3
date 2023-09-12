# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledzkTmoB.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar, 
    QSizePolicy, QSpinBox, QStatusBar, QTextEdit,
    QWidget, QPushButton)

from req import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 352)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.JsonTypeCB = QComboBox(self.centralwidget)
        icon = QIcon()
        iconThemeName = u"face-smile"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.JsonTypeCB.addItem("")
        self.JsonTypeCB.addItem("")
        self.JsonTypeCB.addItem("")
        self.JsonTypeCB.addItem("")
        self.JsonTypeCB.setObjectName(u"JsonTypeCB")
        self.JsonTypeCB.setGeometry(QRect(10, 30, 291, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 121, 16))
        self.JsonEB = QTextEdit(self.centralwidget)
        self.JsonEB.setObjectName(u"JsonEB")
        self.JsonEB.setGeometry(QRect(10, 60, 291, 241))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(310, 130, 471, 23))
        self.progressBar.setValue(0)
        self.HowManySB = QSpinBox(self.centralwidget)
        self.HowManySB.setObjectName(u"HowManySB")
        self.HowManySB.setGeometry(QRect(310, 30, 181, 22))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 10, 71, 20))
        self.AgLevelCB = QComboBox(self.centralwidget)
        self.AgLevelCB.addItem("")
        self.AgLevelCB.addItem("")
        self.AgLevelCB.addItem("")
        self.AgLevelCB.addItem("")
        self.AgLevelCB.setObjectName(u"AgLevelCB")
        self.AgLevelCB.setGeometry(QRect(500, 30, 281, 22))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(500, 10, 101, 16))
        self.UrlLE = QLineEdit(self.centralwidget)
        self.UrlLE.setObjectName(u"UrlLE")
        self.UrlLE.setGeometry(QRect(340, 60, 441, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 60, 21, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 100, 471, 20))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(450, 250, 331, 51))
        self.label_6.setStyleSheet(u"font: 700 24pt \"Segoe UI\";\n"
"color: rgb(255, 7, 11);")
        self.ResponseEB = QTextEdit(self.centralwidget)
        self.ResponseEB.setObjectName(u"ResponseEB")
        self.ResponseEB.setGeometry(QRect(310, 170, 441, 81))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.startReqBtn = QPushButton(self.centralwidget)
        self.startReqBtn.setObjectName(u"pushButton")
        self.startReqBtn.setGeometry(QRect(320, 260, 100, 50))
        self.startReqBtn.setText("Nuk3 req!")
        #self.startReqBtn.click = lambda: send_json_request(self.UrlLE.text(),self.JsonEB.text())
        self.startReqBtn.clicked.connect(lambda: send_json_request(self.UrlLE.text(),self.JsonEB.toPlainText(),self.ResponseEB,self.progressBar,self.HowManySB.value()))

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.JsonTypeCB.setItemText(0, QCoreApplication.translate("MainWindow", u"JSON REQUEST", None))
        self.JsonTypeCB.setItemText(1, QCoreApplication.translate("MainWindow", u"ANY REQUEST", None))
        self.JsonTypeCB.setItemText(2, QCoreApplication.translate("MainWindow", u"NUKE REQUEST", None))
        self.JsonTypeCB.setItemText(3, QCoreApplication.translate("MainWindow", u"XML REQUEST", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Choose request type:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"How many:", None))
        self.AgLevelCB.setItemText(0, QCoreApplication.translate("MainWindow", u"low", None))
        self.AgLevelCB.setItemText(1, QCoreApplication.translate("MainWindow", u"medium", None))
        self.AgLevelCB.setItemText(2, QCoreApplication.translate("MainWindow", u"high", None))
        self.AgLevelCB.setItemText(3, QCoreApplication.translate("MainWindow", u"critical", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Aggression level:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Url:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"status", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"reqnuk3 version 1.0.0", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

def startApp():
    app = QApplication([])

    ui = Ui_MainWindow()

    window = QMainWindow()
    ui.setupUi(window)
    window.show()
    app.exec()

startApp()