from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import cv2
import os

name = 0
File = 0

class Ui_Dialog1():
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(800, 600)
        self.dialog=Dialog1
        self.pushButton = QtWidgets.QPushButton(Dialog1)
        self.pushButton.setGeometry(QtCore.QRect(140, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "Dialog"))
        self.pushButton.setText(_translate("Dialog1", "Jump to main"))
        self.pushButton.clicked.connect(self.jump_to_main)

    def jump_to_main(self):
        self.dialog.close()
