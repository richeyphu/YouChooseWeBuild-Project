# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/cus_uploadslip.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

from ucwblib import ICON_PATH, GetDatabase, QMessageBox

import gridfs


class Ui_frm_cus_uploadslip(object):
    def __init__(self, username="", oid=None):
        self.username = username
        self.oid = oid
        self.filepath = None

    def setupUi(self, frm_cus_uploadslip):
        frm_cus_uploadslip.setObjectName("frm_cus_uploadslip")
        # frm_cus_uploadslip.resize(375, 480)
        # frm_cus_uploadslip.setMinimumSize(QtCore.QSize(375, 480))
        # frm_cus_uploadslip.setMaximumSize(QtCore.QSize(375, 480))
        frm_cus_uploadslip.setFixedSize(QtCore.QSize(375, 480))

        frm_cus_uploadslip.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        # Set window icon
        frm_cus_uploadslip.setWindowIcon(QtGui.QIcon(ICON_PATH))

        self.lbl_filearea = QtWidgets.QLabel(frm_cus_uploadslip)
        self.lbl_filearea.setGeometry(QtCore.QRect(30, 100, 321, 301))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.lbl_filearea.setFont(font)
        self.lbl_filearea.setStyleSheet("")
        self.lbl_filearea.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_filearea.setObjectName("lbl_filearea")
        self.frame_header = QtWidgets.QFrame(frm_cus_uploadslip)
        self.frame_header.setGeometry(QtCore.QRect(0, 0, 381, 91))
        self.frame_header.setStyleSheet("background-color: rgb(0, 148, 217);")
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setObjectName("frame_header")
        self.lbl_title = QtWidgets.QLabel(self.frame_header)
        self.lbl_title.setGeometry(QtCore.QRect(0, 10, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.horizontalLayoutWidget = QtWidgets.QWidget(frm_cus_uploadslip)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 420, 241, 39))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(14)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.btn_confirm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(14)
        self.btn_confirm.setFont(font)
        self.btn_confirm.setStyleSheet("background:rgb(255, 124, 10);\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout.addWidget(self.btn_confirm)
        self.frame_header.raise_()
        self.lbl_filearea.raise_()
        self.horizontalLayoutWidget.raise_()

        self.retranslateUi(frm_cus_uploadslip)
        QtCore.QMetaObject.connectSlotsByName(frm_cus_uploadslip)

        # Event-Driven
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_confirm.clicked.connect(self.confirm)
        self.lbl_filearea.mousePressEvent = self.selectFile
        # Makes label supported drag-and-drop
        self.lbl_filearea.setAcceptDrops(True)
        self.lbl_filearea.dragEnterEvent = self.fileDragEntered
        self.lbl_filearea.dragMoveEvent = self.fileDragMoved
        self.lbl_filearea.dropEvent = self.fileDropped

    def selectFile(self, event):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(frm_cus_uploadslip, "Upload Payment Slip", "",
                                                  "Image files (*.jpg *.jpeg *.png)", options=options)
        if filename and self.isFileExtensionValid(self.getFileExtension(filename)):
            self.filepath = filename
            # self.lbl_filearea.setText(filename.split('/')[-1])
            self.displaySelectedImage()

    def fileDragEntered(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ingore()

    def fileDragMoved(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ingore()

    def fileDropped(self, event):
        # for url in event.mimeData().urls():
        #     path = url.toLocalFile()
        path = event.mimeData().urls()[0].toLocalFile()
        if self.isFileExtensionValid(self.getFileExtension(path)):
            self.filepath = path
            self.displaySelectedImage()
            # print(self.filepath)
        else:
            event.ignore()

    def getFileExtension(self, path):
        return path.split('.')[-1].lower()

    def isFileExtensionValid(self, name):
        return name.lower() in ('jpg', 'jpeg', 'png')

    def displaySelectedImage(self):
        pixmap = QPixmap(self.filepath)
        pixmap = pixmap.scaled(self.lbl_filearea.width(), self.lbl_filearea.height(), QtCore.Qt.KeepAspectRatio)
        self.lbl_filearea.setPixmap(pixmap)

    def confirm(self):
        msg = QMessageBox()
        msg.setWindowTitle("Upload Slip")
        msg.setIcon(msg.Warning)
        if self.filepath is None:
            msg.setText("???????????????????????????????????????????????????????????????????????????????????????????????????")
            msg.exec_()
        else:
            ans = msg.question(msg, "Upload Slip", "????????????????????????????????????????????????????????????", msg.Yes | msg.No)
            if ans == msg.Yes:
                self.uploadSlip()
                frm_cus_uploadslip.hide()

    def uploadSlip(self):
        msg = QMessageBox()
        msg.setWindowTitle("Upload Slip")

        file_location = self.filepath
        if os.path.exists(file_location):
            file_extension = self.getFileExtension(file_location)
            file_data = open(file_location, "rb")  # Reads file in binary
            data = file_data.read()

            with GetDatabase() as conn:
                db = conn.get_database('ucwb')

                fs = gridfs.GridFS(db)
                fs.put(data, filename=self.oid, extension=file_extension, uploader=self.username, type="payslip")

                where = {'oid': self.oid}
                setTo = {'$set': {'status': '2'}}
                db.orders.update_one(where, setTo)

                msg.setIcon(QMessageBox.Information)
                msg.setText("???????????????????????????????????????????????????!")
                msg.exec_()
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.setText("????????????????????????????????????????????????????????????????????????????????????\n"
                        "????????????????????????????????????????????????????????????")
            msg.exec_()

    def cancel(self):
        frm_cus_uploadslip.hide()

    def retranslateUi(self, frm_cus_uploadslip):
        _translate = QtCore.QCoreApplication.translate
        frm_cus_uploadslip.setWindowTitle(_translate("frm_cus_uploadslip", "UCWB - Payment Proof"))
        self.lbl_filearea.setText(_translate("frm_cus_uploadslip", "Drag and Drop\n"
                                                                   "???????????????????????????????????????????????????????????????\n"
                                                                   "(jpg/png)"))
        self.lbl_title.setText(_translate("frm_cus_uploadslip", "????????????????????????????????????\n"
                                                                "??????????????????????????????????????????????????????"))
        self.btn_cancel.setText(_translate("frm_cus_uploadslip", "??????????????????"))
        self.btn_confirm.setText(_translate("frm_cus_uploadslip", "??????????????????"))


frm_cus_uploadslip = None
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    frm_cus_uploadslip = QtWidgets.QDialog()
    ui = Ui_frm_cus_uploadslip()
    ui.setupUi(frm_cus_uploadslip)
    frm_cus_uploadslip.show()
    sys.exit(app.exec_())
