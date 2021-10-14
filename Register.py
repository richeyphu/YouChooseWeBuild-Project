# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import re
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QInputDialog

from ucwblib import GetDatabase, HashPassword, ICON_PATH, QMessageBox, REGEX_EMAIL, REGEX_TEL, REGEX_USERNAME, \
    REGEX_PASSWORD


class Ui_frm_register(object):
    def setupUi(self, frm_register):
        frm_register.setObjectName("frm_register")
        frm_register.resize(500, 450)
        frm_register.setMinimumSize(QtCore.QSize(500, 450))
        frm_register.setMaximumSize(QtCore.QSize(500, 450))

        frm_register.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint)

        # Set window icon
        frm_register.setWindowIcon(QtGui.QIcon(ICON_PATH))

        self.formLayoutWidget = QtWidgets.QWidget(frm_register)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 100, 381, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.layout_registerForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layout_registerForm.setContentsMargins(0, 0, 0, 0)
        self.layout_registerForm.setHorizontalSpacing(15)
        self.layout_registerForm.setVerticalSpacing(10)
        self.layout_registerForm.setObjectName("layout_registerForm")
        self.lbl_password = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")
        self.layout_registerForm.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_password)
        self.lbl_email = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_email.setFont(font)
        self.lbl_email.setObjectName("lbl_email")
        self.layout_registerForm.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_email)
        self.lbl_name = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_name.setFont(font)
        self.lbl_name.setObjectName("lbl_name")
        self.layout_registerForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_name)
        self.lbl_tel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_tel.setFont(font)
        self.lbl_tel.setObjectName("lbl_tel")
        self.layout_registerForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_tel)
        self.lbl_repassword = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_repassword.setFont(font)
        self.lbl_repassword.setObjectName("lbl_repassword")
        self.layout_registerForm.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_repassword)
        self.lbl_username = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName("lbl_username")
        self.layout_registerForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_username)

        self.txt_username = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_username.setFont(font)
        self.txt_username.setObjectName("txt_username")
        self.layout_registerForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_username)

        self.txt_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_name.setFont(font)
        self.txt_name.setObjectName("txt_name")
        self.layout_registerForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_name)

        self.txt_tel = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_tel.setFont(font)
        self.txt_tel.setObjectName("txt_tel")
        self.layout_registerForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_tel)

        self.txt_email = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_email.setFont(font)
        self.txt_email.setObjectName("txt_email")
        self.layout_registerForm.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_email)

        self.txt_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_password.setFont(font)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.layout_registerForm.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txt_password)

        self.txt_repassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_repassword.setFont(font)
        self.txt_repassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_repassword.setObjectName("txt_repassword")
        self.layout_registerForm.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txt_repassword)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(frm_register)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 350, 240, 68))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layout_btn = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_btn.setContentsMargins(0, 0, 0, 0)
        self.layout_btn.setObjectName("layout_btn")
        self.btn_register = QtWidgets.QPushButton(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(11)
        self.btn_register.setFont(font)
        self.btn_register.setStyleSheet("background:rgb(255, 124, 10);\n"
                                        "color: rgb(255, 255, 255);")
        self.btn_register.setObjectName("btn_register")
        self.layout_btn.addWidget(self.btn_register)
        self.btn_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(11)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.layout_btn.addWidget(self.btn_cancel)
        self.frame_header = QtWidgets.QFrame(frm_register)
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

        self.retranslateUi(frm_register)
        QtCore.QMetaObject.connectSlotsByName(frm_register)

        ###
        self.txt_username.setValidator(QRegExpValidator(QRegExp(REGEX_USERNAME)))
        self.txt_tel.setValidator(QRegExpValidator(QRegExp(REGEX_TEL)))
        self.txt_email.setValidator(QRegExpValidator(QRegExp(REGEX_EMAIL)))

        # Event_Driven
        self.btn_register.clicked.connect(self.register)
        self.btn_cancel.clicked.connect(self.cancel)

    def register(self):
        try:
            username = self.txt_username.text().strip()
            name = self.txt_name.text().strip().title()
            tel = self.txt_tel.text().strip()
            email = self.txt_email.text().strip().lower()
            password = self.txt_password.text()
            # re_password = self.txt_repassword.text()

            msg = QMessageBox()
            msg.setWindowTitle("Register")
            msg.setStyleSheet("QLabel{min-width: 50px;}")

            if self.checkRegisterInfo():
                sq = self.createSecurityQuestion()
                if sq is not None:
                    hashed_pwd = HashPassword(password)
                    # with pymongo.MongoClient(CONN_STR) as conn:
                    with GetDatabase() as conn:
                        db = conn.get_database('ucwb')
                        db.users.insert_one({'username': username,
                                             'password': hashed_pwd.getSaltAndHashChunk(),
                                             'email': email,
                                             'sq': sq,
                                             'joined_date': datetime.now(),
                                             'last_access': datetime.now(),
                                             'shipping_info': {'name': name,
                                                               'tel': tel,
                                                               'address': ''}
                                             })

                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Success!")
                        msg.exec_()
                        frm_register.close()

        except Exception as e:
            print(e)
        finally:
            pass

    def createSecurityQuestion(self):
        win_title = "Security Question"
        msg = QMessageBox()
        msg.setWindowTitle(win_title)
        while True:
            question, ok = QInputDialog.getText(frm_register, win_title, "กรุณาตั้งคำถามรักษาความปลอดภัยของท่าน\n"
                                                                         "(ไม่สามารถเปลี่ยนในภายหลังได้)")
            if ok:
                question = question.strip()
                if question == "":
                    msg.setIcon(msg.Warning)
                    msg.setText("กรุณากรอกคำถามให้ถูกต้อง")
                    msg.exec_()
                    continue
                else:
                    while True:
                        answer, ok = QInputDialog.getText(frm_register, win_title, "กรุณากรอกคำตอบของท่าน")
                        if ok:
                            answer = answer.strip()
                            if answer == "":
                                msg.setIcon(msg.Warning)
                                msg.setText("กรุณากรอกคำตอบให้ถูกต้อง")
                                msg.exec_()
                                continue
                            else:
                                confirm = msg.question(msg, win_title, "ยืนยันการตั้งคำถามรักษาความปลอดภัย\n\n"
                                                                       "Q : {}\n"
                                                                       "A : {}".format(question, answer),
                                                       msg.Yes | msg.No)
                                if confirm == msg.Yes:
                                    hashed_ans = HashPassword(answer.lower())
                                    sq = {'question': question,
                                          'answer': hashed_ans.getSaltAndHashChunk()}
                                    return sq
                        break
            return None

    def checkRegisterInfo(self):
        username = self.txt_username.text().strip()
        name = self.txt_name.text().strip().title()
        tel = self.txt_tel.text().strip()
        email = self.txt_email.text().strip().lower()
        password = self.txt_password.text()
        re_password = self.txt_repassword.text()

        msg = QMessageBox()
        msg.setWindowTitle("Register")
        msg.setIcon(QMessageBox.Warning)

        if username.isspace() or name.isspace() or tel.isspace() or email.isspace() or password.isspace() or re_password.isspace():
            msg.setText("กรุณากรอกข้อมูลให้ครบถ้วน")
            msg.exec_()
            return False
        if self.isUsernameDuplicated(username) or username == '':
            msg.setText("ไม่สามารถใช้ Username นี้ได้")
            msg.exec_()
            return False
        if name == '':
            msg.setText("กรุณากรอก 'ชื่อ-นามสกุล' ให้ถูกต้อง")
            msg.exec_()
            return False
        if not bool(re.match(REGEX_TEL, tel)):
            msg.setText("กรุณากรอก 'เบอร์โทรศัพท์' ให้ถูกต้อง")
            msg.exec_()
            return False
        if not bool(re.match(REGEX_EMAIL, email)):
            msg.setText("กรุณากรอก 'อีเมล' ให้ถูกต้อง")
            msg.exec_()
            return False
        if not bool(re.match(REGEX_PASSWORD, password)):
            msg.setText("กรุณาตั้งรหัสผ่านที่มีความยาวตั้งแต่ 8 ตัวอักษรขึ้นไป\n"
                        "และต้องประกอบไปด้วยอักขระดังต่อไปนี้\n\t- ตัวพิมพ์เล็ก\n\t- ตัวพิมพ์ใหญ่\n\t- ตัวเลข")
            msg.exec_()
            return False
        if not self.isPasswordValid(password, re_password):
            msg.setText("กรุณากรอก 'รหัสผ่าน' ใหม่อีกครั้ง")
            msg.exec_()
            return False

        return True

    def isUsernameDuplicated(self, username):
        # with pymongo.MongoClient(CONN_STR) as conn:
        with GetDatabase() as conn:
            db = conn.get_database('ucwb')
            condition = {'username': {"$regex": f'^{username}$', "$options": "i"}}
            found = db.users.count_documents(condition)
            if found:
                return True
        return False

    # def isNameValid(self, name):
    #     return all(x.isalpha or x == "" for x in name)

    def isPasswordValid(self, p1, p2):
        return p1 == p2

    def cancel(self):
        try:
            # frm_register.close()
            frm_register.hide()
        except Exception as e:
            print(e)

    def retranslateUi(self, frm_register):
        _translate = QtCore.QCoreApplication.translate
        frm_register.setWindowTitle(_translate("frm_register", "UCWB - Register"))
        self.lbl_password.setText(_translate("frm_register", "Password"))
        self.lbl_email.setText(_translate("frm_register", "Email"))
        self.lbl_name.setText(_translate("frm_register", "Name"))
        self.lbl_tel.setText(_translate("frm_register", "Tel"))
        self.lbl_repassword.setText(_translate("frm_register", "Re-Password"))
        self.lbl_username.setText(_translate("frm_register", "Username"))
        self.btn_register.setText(_translate("frm_register", "Register"))
        self.btn_cancel.setText(_translate("frm_register", "Cancel"))
        self.lbl_title.setText(_translate("frm_register", "You Choose, We Build"))


frm_register = None
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    frm_register = QtWidgets.QDialog()
    ui = Ui_frm_register()
    ui.setupUi(frm_register)
    frm_register.show()
    sys.exit(app.exec_())
