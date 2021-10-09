# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QInputDialog, QLineEdit

import Register
import CusMain
from AdminMain import Ui_frm_admin_main
from ucwblib import GetDatabase, HashPassword, ICON_PATH, QMessageBox


class Ui_frm_login(object):
    def setupUi(self, frm_login):
        frm_login.setObjectName("frm_login")
        # frm_login.resize(500, 350)
        # frm_login.setMinimumSize(QtCore.QSize(500, 350))
        # frm_login.setMaximumSize(QtCore.QSize(500, 350))
        frm_login.setFixedSize(QtCore.QSize(500, 350))

        frm_login.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint)

        # Set window icon
        frm_login.setWindowIcon(QtGui.QIcon(ICON_PATH))

        self.formLayoutWidget = QtWidgets.QWidget(frm_login)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 110, 321, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.layout_loginForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layout_loginForm.setContentsMargins(0, 0, 0, 0)
        self.layout_loginForm.setHorizontalSpacing(15)
        self.layout_loginForm.setVerticalSpacing(20)
        self.layout_loginForm.setObjectName("layout_loginForm")
        self.lbl_username = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName("lbl_username")
        self.layout_loginForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_username)
        self.txt_username = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_username.setFont(font)
        self.txt_username.setObjectName("txt_username")
        self.layout_loginForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_username)
        self.lbl_password = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")
        self.layout_loginForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_password)
        self.txt_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_password.setFont(font)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.layout_loginForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_password)
        self.verticalLayoutWidget = QtWidgets.QWidget(frm_login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 220, 240, 93))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_btn = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_btn.setContentsMargins(0, 0, 0, 0)
        self.layout_btn.setObjectName("layout_btn")
        self.btn_login = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(11)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("background:rgb(255, 124, 10);\n"
                                     "color: rgb(255, 255, 255);")
        self.btn_login.setObjectName("btn_login")
        self.layout_btn.addWidget(self.btn_login)
        self.btn_register = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(11)
        self.btn_register.setFont(font)
        self.btn_register.setObjectName("btn_register")
        self.layout_btn.addWidget(self.btn_register)
        self.lbl_forgotPwd = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(8)
        self.lbl_forgotPwd.setFont(font)
        self.lbl_forgotPwd.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_forgotPwd.setObjectName("lbl_forgotPwd")
        self.layout_btn.addWidget(self.lbl_forgotPwd)
        self.frame_header = QtWidgets.QFrame(frm_login)
        self.frame_header.setGeometry(QtCore.QRect(0, 0, 501, 61))
        self.frame_header.setStyleSheet("background-color: rgb(0, 148, 217);")
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setObjectName("frame_header")
        self.lbl_title = QtWidgets.QLabel(self.frame_header)
        self.lbl_title.setGeometry(QtCore.QRect(0, 10, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(20)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")

        self.retranslateUi(frm_login)
        QtCore.QMetaObject.connectSlotsByName(frm_login)

        # Event-Driven
        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.register)
        self.lbl_forgotPwd.mousePressEvent = self.forgotPassword

    def login(self):
        login_code = 0
        try:
            username = self.txt_username.text()
            password = self.txt_password.text()

            if username == "" or password == "":
                return False

            # with pymongo.MongoClient(CONN_STR) as conn:
            with GetDatabase() as conn:
                db = conn.get_database('ucwb')
                condition = {'username': {"$regex": f'^{username}$', "$options": "i"}}
                found = db.users.count_documents(condition)
                if found:
                    cursor = db.users.find(condition)

                    # password จาก database
                    pwd_chunk = HashPassword(cursor[0]['password'])
                    salt = pwd_chunk.getSaltFromChunk()
                    key = pwd_chunk.getKeyFromChunk()
                    # password ที่กรอกจากหน้า login
                    pwd = HashPassword(password).getHashedKey(salt)

                    if key == pwd:
                        login_code = 1
                        setTo = {'$set': {'last_access': datetime.now()}}
                        db.users.update_one(condition, setTo)

        except Exception as e:
            print(e)

        finally:
            msg = QMessageBox()
            msg.setWindowTitle("Login")
            msg.setStyleSheet("QLabel{min-width: 50px;}")
            if login_code == 0:
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error!")
                msg.exec_()
            else:
                msg.setIcon(QMessageBox.Information)
                msg.setText("Success!")
                msg.exec_()
                frm_login.close()
                self.showMainWindow(username)
            self.clearTextbox()

    def __login_legacy(self):
        try:
            username = self.txt_username.text()
            password = self.txt_password.text()

            msg = QMessageBox()
            msg.setWindowTitle("Login")
            msg.setStyleSheet("QLabel{min-width: 50px;}")

            if username == "" or password == "":
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error!")
                msg.exec_()
                return False

            # with pymongo.MongoClient(CONN_STR) as conn:
            with GetDatabase() as conn:
                db = conn.get_database('ucwb')
                con1 = {'username': {"$regex": f'^{username}$', "$options": "i"}}
                con2 = {'password': password}
                where = {'$and': [con1, con2]}
                found = db.users.count_documents(where)
                if found:
                    # cursor = db.users.find(where)

                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Success!")

                    setTo = {'$set': {'last_access': datetime.now()}}
                    db.users.update_one(where, setTo)

                    msg.exec_()
                    frm_login.close()
                    self.showMainWindow(username)
                else:
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error!")
                    msg.exec_()
        except Exception as e:
            print(e)
        finally:
            # msg.exec_()
            self.clearTextbox()

    def isPasswordValid(self):
        pass

    def register(self):
        frm_login.hide()
        self.clearTextbox()
        try:
            frm_register = QtWidgets.QDialog()
            _ui = Register.Ui_frm_register()
            _ui.setupUi(frm_register)
            Register.frm_register = frm_register
            frm_register.exec_()
            # Register.frm_register.exec_()
        except Exception as e:
            print(e)
        finally:
            frm_login.show()

    def forgotPassword(self, event):
        try:
            win_title = "ลืมรหัสผ่าน"
            msg = QMessageBox()
            msg.setWindowTitle(win_title)
            username, ok = QInputDialog.getText(frm_login, win_title, "กรุณากรอก Username ของท่าน")
            if ok:
                with GetDatabase() as conn:
                    db = conn.get_database('ucwb')
                    condition = {'username': {"$regex": f'^{username}$', "$options": "i"}}
                    found = db.users.count_documents(condition)
                    if found:
                        cursor = db.users.find(condition)
                        sq = cursor[0]['sq']
                        question = sq['question']
                        _ans, ok = QInputDialog.getText(frm_login, win_title, "กรุณาตอบคำถามรักษาความปลอดภัย\n\n"
                                                                              "> {}".format(question))
                        if ok:
                            answer = sq['answer']
                            # answer จาก database
                            ans_chunk = HashPassword(answer)
                            salt = ans_chunk.getSaltFromChunk()
                            key = ans_chunk.getKeyFromChunk()
                            # answer ที่กรอกจากหน้า forgot password
                            ans = HashPassword(_ans.lower()).getHashedKey(salt)
                            if key == ans:
                                new_pwd, ok = QInputDialog.getText(frm_login, win_title, "กรุณากรอกรหัสผ่านใหม่",
                                                                   QLineEdit.Password)
                                if ok:
                                    renew_pwd, ok = QInputDialog.getText(frm_login, win_title,
                                                                         "กรุณากรอกรหัสผ่านใหม่อีกครั้ง",
                                                                         QLineEdit.Password)
                                    if new_pwd != renew_pwd:
                                        msg.setIcon(msg.Warning)
                                        msg.setText("รหัสผ่านไม่ตรงกัน\nกรุณาลองใหม่อีกครั้ง")
                                        msg.exec_()
                                    else:
                                        # เปลี่ยน password ใหม่
                                        hashed_pwd = HashPassword(new_pwd)
                                        setTo = {'$set': {'password': hashed_pwd.getSaltAndHashChunk()}}
                                        db.users.update_one(condition, setTo)
                                        msg.setIcon(msg.Information)
                                        msg.setText("เปลี่ยนรหัสผ่านใหม่สำเร็จ")
                                        msg.exec_()
                            else:
                                msg.setIcon(msg.Critical)
                                msg.setText("คำตอบไม่ถูกต้อง\nกรุณาลองใหม่อีกครั้ง")
                                msg.exec_()
                    else:
                        msg.setIcon(msg.Warning)
                        msg.setText("ขออภัย ไม่พบ Username ในระบบ")
                        msg.exec_()
        except Exception as e:
            print(e)
        finally:
            self.clearTextbox()

    def clearTextbox(self):
        self.txt_username.clear()
        self.txt_password.clear()

    def showMainWindow(self, username):
        if username == "admin":
            # Shows Admin Dashboard
            try:
                frm_admin_main = QtWidgets.QMainWindow()
                _ui = Ui_frm_admin_main()
                _ui.setupUi(frm_admin_main)
                CusMain.frm_admin_main = frm_admin_main
                frm_admin_main.show()
            except Exception as e:
                print(e)
        else:
            # Shows Customer Main windows
            try:
                # CusMain.USERNAME = username
                frm_cus_main = QtWidgets.QMainWindow()
                _ui = CusMain.Ui_frm_cus_main(username)
                _ui.setupUi(frm_cus_main)
                CusMain.frm_cus_main = frm_cus_main
                frm_cus_main.show()
            except Exception as e:
                print(e)

    def retranslateUi(self, frm_login):
        _translate = QtCore.QCoreApplication.translate
        frm_login.setWindowTitle(_translate("frm_login", "UCWB - Login"))
        self.lbl_username.setText(_translate("frm_login", "Username"))
        self.lbl_password.setText(_translate("frm_login", "Password"))
        self.btn_login.setText(_translate("frm_login", "Login"))
        self.btn_register.setText(_translate("frm_login", "Register"))
        self.lbl_forgotPwd.setText(_translate("frm_login", "ลืมรหัสผ่าน"))
        self.lbl_title.setText(_translate("frm_login", "You Choose, We Build"))


frm_login = None
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    frm_login = QtWidgets.QDialog()
    ui = Ui_frm_login()
    ui.setupUi(frm_login)
    frm_login.show()
    sys.exit(app.exec_())
