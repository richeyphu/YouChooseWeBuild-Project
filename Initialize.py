# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/splash.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import threading
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget

import Login
from ucwblib import ICON_PATH


class Ui_frm_splash(object):
    def setupUi(self, frm_splash):
        frm_splash.setObjectName("frm_splash")
        frm_splash.resize(510, 415)
        # frm_splash.setMinimumSize(QtCore.QSize(515, 415))
        # frm_splash.setMaximumSize(QtCore.QSize(515, 415))

        # Makes frameless window
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        frm_splash.setWindowFlags(flags)

        # Make window center
        qtRectangle = frm_splash.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        frm_splash.move(qtRectangle.topLeft())

        # Set window icon
        frm_splash.setWindowIcon(QtGui.QIcon(ICON_PATH))

        self.frame_header = QtWidgets.QFrame(frm_splash)
        self.frame_header.setGeometry(QtCore.QRect(0, 0, 521, 415))
        self.frame_header.setStyleSheet("background-color: rgb(0, 148, 217);")
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setObjectName("frame_header")
        self.lbl_title = QtWidgets.QLabel(self.frame_header)
        self.lbl_title.setGeometry(QtCore.QRect(0, 10, 511, 380))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(20)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")

        self.retranslateUi(frm_splash)
        QtCore.QMetaObject.connectSlotsByName(frm_splash)

    def retranslateUi(self, frm_splash):
        _translate = QtCore.QCoreApplication.translate
        frm_splash.setWindowTitle(_translate("frm_splash", "UCWB - Welcome"))
        self.lbl_title.setText(_translate("frm_splash", "You Choose, We Build"))


def showLoginForm():
    frm_login = QtWidgets.QDialog()
    _ui = Login.Ui_frm_login()
    _ui.setupUi(frm_login)
    Login.frm_login = frm_login
    frm_login.open()
    # Login.frm_login.open()
    # Login.frm_login.exec_()


def transition():
    sleep(2)
    for i in range(100, -1, -2):
        frm_splash.setWindowOpacity(i/100)
        sleep(0.01)
    frm_splash.close()


def init():
    global frm_splash
    global app

    try:
        # Creates Form
        app = QtWidgets.QApplication(sys.argv)
        frm_splash = QtWidgets.QDialog()
        ui = Ui_frm_splash()
        ui.setupUi(frm_splash)

        t1 = threading.Thread(target=transition)
        t1.start()
        showLoginForm()
    except Exception as e:
        print(e)

    frm_splash.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    init()
