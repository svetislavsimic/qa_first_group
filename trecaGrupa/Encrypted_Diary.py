# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GUI Python\DiaryTestv1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet
import ctypes
user32 = ctypes.windll.user32
key = b'F8z-KuTE1YqpwSp412SMMJuZPHaTH60d_8HYG4eKMpo='
arb = Fernet(key)
# Aplikacija ima par problema: 1. kad se klikne na x u gornjem desnom uglu, aplikacija se ugasi cak i ako se klikne cancel(nisam znao kako to da promenim)
# 2. resize-ovanje ne radi kako treba, aplikacija bi trebalo da normalno radi kad je maximizovana jer pronadje rezoluciju korisnikovog kompjutera i onda na osnovu toga podesi velicinu svega.
# to takodje nisam znao kako da popravim. 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(
            QtCore.QRect(0, 0, user32.GetSystemMetrics(0) * 0.97, user32.GetSystemMetrics(1) * 0.90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, user32.GetSystemMetrics(0), 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFont = QtWidgets.QMenu(self.menubar)
        self.menuFont.setObjectName("menuFont")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFont = QtWidgets.QAction(MainWindow)
        self.actionFont.setObjectName("actionFont")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuFont.addAction(self.actionFont)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFont.menuAction())
        self.actionExit.triggered.connect(self.close_app)
        self.actionFont.triggered.connect(self.change_font)
        self.actionOpen.triggered.connect(self.file_open)
        self.actionSave.triggered.connect(self.file_save)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.password = "123456789"
        app.aboutToQuit.connect(self.close_app)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encrypted Diary"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFont.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionFont.setText(_translate("MainWindow", "Font"))

    def close_app(self):
        msg_yesnocancel = QtWidgets.QMessageBox.question(MainWindow, 'PyQt5 message', "Do you want to save?",
                                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel,
                                                         QtWidgets.QMessageBox.Cancel)
        if msg_yesnocancel == QtWidgets.QMessageBox.Yes:
            self.file_save()
            sys.exit()
        if msg_yesnocancel == QtWidgets.QMessageBox.No:
            sys.exit()
        if msg_yesnocancel == QtWidgets.QMessageBox.Cancel:
            print('Cancel')

    def change_font(self):
        font, ok = QtWidgets.QFontDialog.getFont()
        print(font, ok)
        if ok:
            self.plainTextEdit.setFont(font)

    def file_open(self):
        self.passcheck()
        if self.password == self.password_query:
            msg_encrypted = QtWidgets.QMessageBox.question(MainWindow, 'PyQt5 message', "Is your file encrypted?",
                                                           QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel,
                                                           QtWidgets.QMessageBox.Cancel)
            if msg_encrypted == QtWidgets.QMessageBox.Cancel:
                pass
            else:
                fileName = QtWidgets.QFileDialog.getOpenFileName(MainWindow, str("Open"))
                print(fileName)
                print(fileName[0])
                if fileName[0]:
                    f = open(fileName[0], 'r')
                    with f:
                        data = f.read()
                        print(data)
                        datatoken = bytes(data, 'utf-8')
                        print(datatoken)
                        if msg_encrypted == QtWidgets.QMessageBox.Yes:
                            self.plainTextEdit.setPlainText((arb.decrypt(datatoken).decode('utf-8')))
                        if msg_encrypted == QtWidgets.QMessageBox.No:
                            self.plainTextEdit.setPlainText(data)
        else:
            pass

    def file_save(self):
        fileNamn, _ = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "Save", "",
                                                            "Text Files (*.txt);;All Files (*)")
        if fileNamn:
            f = open(fileNamn, 'w')
            token = arb.encrypt(bytes(QtWidgets.QPlainTextEdit.toPlainText(self.plainTextEdit), 'utf-8'))
            f.write(token.decode('utf-8'))
            print(fileNamn)
            print(QtWidgets.QPlainTextEdit.toPlainText(self.plainTextEdit))

    def passcheck(self):
        self.password_query, okPressed = QtWidgets.QInputDialog.getText(MainWindow, "Password:", "Password:",
                                                                        QtWidgets.QLineEdit.Normal, "")
        if okPressed and self.password_query != '':
            print(self.password_query)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
