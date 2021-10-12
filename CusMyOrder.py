# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/cus_myorder.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import webbrowser
from functools import partial

import pymongo
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QTableWidgetItem, QInputDialog, QLineEdit

import CusPayment
import CusUploadSlip
from ucwblib import GetDatabase, getSettings, getOrderStatus, ICON_PATH, QMessageBox, HashPassword


class Ui_frm_cus_myorder(object):
    def __init__(self, username: str = None):
        self.username = username
        self.username = 'a'  # testing
        self.orders = None
        self.orders_count = 0
        self.btn_view = list()
        self.current_oid = None
        self.current_net_total = 0
        self.tax_rate = 0
        self.shipping_fee = 0
        self.temp_cusInfo = tuple()

    def setupUi(self, frm_cus_myorder):
        frm_cus_myorder.setObjectName("frm_cus_myorder")
        # frm_cus_myorder.resize(900, 600)
        # frm_cus_myorder.setMinimumSize(QtCore.QSize(900, 600))
        # frm_cus_myorder.setMaximumSize(QtCore.QSize(900, 600))
        frm_cus_myorder.setFixedSize(QtCore.QSize(900, 600))

        frm_cus_myorder.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        # frm_cus_myorder.setFixedSize(QtCore.QSize(900, 600))

        # Set window icon
        frm_cus_myorder.setWindowIcon(QtGui.QIcon(ICON_PATH))

        self.frame_header = QtWidgets.QFrame(frm_cus_myorder)
        self.frame_header.setGeometry(QtCore.QRect(0, 0, 901, 61))
        self.frame_header.setStyleSheet("background-color: rgb(0, 148, 217);")
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setObjectName("frame_header")
        self.lbl_title = QtWidgets.QLabel(self.frame_header)
        self.lbl_title.setGeometry(QtCore.QRect(20, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(20)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_title_2 = QtWidgets.QLabel(self.frame_header)
        self.lbl_title_2.setGeometry(QtCore.QRect(600, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(20)
        self.lbl_title_2.setFont(font)
        self.lbl_title_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_title_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_title_2.setObjectName("lbl_title_2")
        self.lbl_order_list = QtWidgets.QLabel(frm_cus_myorder)
        self.lbl_order_list.setGeometry(QtCore.QRect(30, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(14)
        self.lbl_order_list.setFont(font)
        self.lbl_order_list.setObjectName("lbl_order_list")
        self.tbl_order = QtWidgets.QTableWidget(frm_cus_myorder)
        self.tbl_order.setGeometry(QtCore.QRect(30, 110, 481, 411))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(11)
        self.tbl_order.setFont(font)
        self.tbl_order.setObjectName("tbl_order")
        self.tbl_order.setColumnCount(4)
        self.tbl_order.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_order.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_order.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_order.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_order.setHorizontalHeaderItem(3, item)
        self.lbl_cus_detail = QtWidgets.QLabel(frm_cus_myorder)
        self.lbl_cus_detail.setGeometry(QtCore.QRect(530, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(14)
        self.lbl_cus_detail.setFont(font)
        self.lbl_cus_detail.setObjectName("lbl_cus_detail")
        self.btn_confirm = QtWidgets.QPushButton(frm_cus_myorder)
        self.btn_confirm.setGeometry(QtCore.QRect(720, 530, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(14)
        self.btn_confirm.setFont(font)
        self.btn_confirm.setStyleSheet("background:rgb(255, 124, 10);\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_confirm.setObjectName("btn_confirm")
        self.formLayoutWidget = QtWidgets.QWidget(frm_cus_myorder)
        self.formLayoutWidget.setGeometry(QtCore.QRect(530, 120, 341, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.frmLayout_cusDetail = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.frmLayout_cusDetail.setContentsMargins(0, 0, 0, 0)
        self.frmLayout_cusDetail.setVerticalSpacing(12)
        self.frmLayout_cusDetail.setObjectName("frmLayout_cusDetail")
        self.lbl_name = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_name.setFont(font)
        self.lbl_name.setObjectName("lbl_name")
        self.frmLayout_cusDetail.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_name)
        self.txt_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_name.setFont(font)
        self.txt_name.setObjectName("txt_name")
        self.frmLayout_cusDetail.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_name)
        self.txt_tel = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_tel.setFont(font)
        self.txt_tel.setObjectName("txt_tel")
        self.frmLayout_cusDetail.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_tel)
        self.lbl_tel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_tel.setFont(font)
        self.lbl_tel.setObjectName("lbl_tel")
        self.frmLayout_cusDetail.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_tel)
        self.txt_email = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_email.setFont(font)
        self.txt_email.setObjectName("txt_email")
        self.frmLayout_cusDetail.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_email)
        self.lbl_email = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_email.setFont(font)
        self.lbl_email.setObjectName("lbl_email")
        self.frmLayout_cusDetail.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_email)
        self.txt_address = QtWidgets.QTextEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_address.setFont(font)
        self.txt_address.setObjectName("txt_address")
        self.frmLayout_cusDetail.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_address)
        self.lbl_address = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_address.setFont(font)
        self.lbl_address.setObjectName("lbl_address")
        self.frmLayout_cusDetail.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_address)
        self.btn_changeCus = QtWidgets.QPushButton(frm_cus_myorder)
        self.btn_changeCus.setGeometry(QtCore.QRect(770, 350, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_changeCus.sizePolicy().hasHeightForWidth())
        self.btn_changeCus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.btn_changeCus.setFont(font)
        self.btn_changeCus.setObjectName("btn_changeCus")
        self.btn_cancelChange = QtWidgets.QPushButton(frm_cus_myorder)
        self.btn_cancelChange.setGeometry(QtCore.QRect(660, 350, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancelChange.sizePolicy().hasHeightForWidth())
        self.btn_cancelChange.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.btn_cancelChange.setFont(font)
        self.btn_cancelChange.setObjectName("btn_cancelChange")
        self.btn_changePwd = QtWidgets.QPushButton(frm_cus_myorder)
        self.btn_changePwd.setGeometry(QtCore.QRect(530, 350, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_changePwd.sizePolicy().hasHeightForWidth())
        self.btn_changePwd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.btn_changePwd.setFont(font)
        self.btn_changePwd.setObjectName("btn_changePwd")
        self.btn_back = QtWidgets.QPushButton(frm_cus_myorder)
        self.btn_back.setGeometry(QtCore.QRect(360, 530, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(14)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.btn_showQR = QtWidgets.QPushButton(frm_cus_myorder)
        self.btn_showQR.setGeometry(QtCore.QRect(720, 480, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_showQR.sizePolicy().hasHeightForWidth())
        self.btn_showQR.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(14)
        self.btn_showQR.setFont(font)
        self.btn_showQR.setObjectName("btn_showQR")
        self.btn_cancelOrder = QtWidgets.QPushButton(frm_cus_myorder)
        self.btn_cancelOrder.setGeometry(QtCore.QRect(560, 530, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancelOrder.sizePolicy().hasHeightForWidth())
        self.btn_cancelOrder.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(14)
        self.btn_cancelOrder.setFont(font)
        self.btn_cancelOrder.setObjectName("btn_cancelOrder")
        self.btn_viewMore = QtWidgets.QPushButton(frm_cus_myorder)
        self.btn_viewMore.setGeometry(QtCore.QRect(200, 530, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_viewMore.sizePolicy().hasHeightForWidth())
        self.btn_viewMore.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(14)
        self.btn_viewMore.setFont(font)
        self.btn_viewMore.setObjectName("btn_viewMore")
        self.lbl_orderId = QtWidgets.QLabel(frm_cus_myorder)
        self.lbl_orderId.setGeometry(QtCore.QRect(30, 530, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(13)
        self.lbl_orderId.setFont(font)
        self.lbl_orderId.setObjectName("lbl_orderId")

        self.retranslateUi(frm_cus_myorder)
        QtCore.QMetaObject.connectSlotsByName(frm_cus_myorder)

        ###
        self.btn_cancelChange.setEnabled(False)
        self.btn_cancelOrder.setEnabled(False)
        # self.btn_confirm.setEnabled(False)
        self.btn_showQR.setEnabled(False)
        self.btn_viewMore.setEnabled(False)
        self.btn_back.setEnabled(False)

        self.txt_tel.setValidator(QRegExpValidator(QRegExp("^[0-9]{3}-[0-9]{3}-[0-9]{4}$")))
        self.txt_email.setValidator(QRegExpValidator(QRegExp("^\\w+([\\.-]?\\w+)*@\\w+([\\.-]?\\w+)*(\\.\\w{2,3})+$")))

        self.getPriceSettings()
        self.getCusOrders()
        self.setupTable()
        self.addToTable()
        self.getCusInfo()

        # Event-Driven
        self.btn_confirm.clicked.connect(self.confirmPayment)
        self.btn_back.clicked.connect(self.backClicked)
        self.btn_changeCus.clicked.connect(self.editCusInfo)
        self.btn_cancelChange.clicked.connect(self.cancelEditCusInfo)
        self.btn_cancelOrder.clicked.connect(self.cancelOrder)
        self.btn_changePwd.clicked.connect(self.changePassword)
        self.btn_showQR.clicked.connect(self.showQrDialog)
        self.btn_viewMore.clicked.connect(self.showTrackingInfo)

    def getCusOrders(self):
        with GetDatabase() as conn:
            db = conn.get_database('ucwb')
            con = {'username': {"$regex": f'^{self.username}$',
                                "$options": "i"}}
            found = db.orders.count_documents(con)
            if found:
                cursor = db.orders.find(con).sort('oid', pymongo.DESCENDING)
                self.orders = list(cursor)
                self.orders_count = found

    def getCusInfo(self):
        self.setCusInfoReadOnly(boolean=True)
        with GetDatabase() as conn:
            db = conn.get_database('ucwb')
            con = {'username': {"$regex": f'^{self.username}$',
                                "$options": "i"}}
            # con2 = {'shipping_info': {'$exists': True,
            #                           '$ne': None}}
            # where = {'$and': [con1, con2]}
            found = db.users.count_documents(con)
            if found:
                cursor = db.users.find(con)
                self.txt_email.setText(cursor[0]['email'])
                if "shipping_info" in cursor[0]:
                    shipping_info = cursor[0]['shipping_info']
                    self.txt_name.setText(shipping_info['name'])
                    self.txt_tel.setText(shipping_info['tel'])
                    self.txt_address.setText(shipping_info['address'])

    def setupTable(self):
        # Table Widget
        self.tbl_order.setRowCount(0)  # Reset Row
        self.tbl_order.setColumnCount(0)  # Reset Column
        self.tbl_order.setRowCount(self.orders_count)
        self.tbl_order.setColumnCount(5)
        self.tbl_order.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # Table Read-only

        # สร้าง Header
        header0 = QTableWidgetItem("")
        header1 = QTableWidgetItem("OID")
        header2 = QTableWidgetItem("วันที่สั่งซื้อ")
        header3 = QTableWidgetItem("ราคารวม")
        header4 = QTableWidgetItem("สถานะ")

        # ใส่ Header ให้ Table
        self.tbl_order.setHorizontalHeaderItem(0, header0)
        self.tbl_order.setHorizontalHeaderItem(1, header1)
        self.tbl_order.setHorizontalHeaderItem(2, header2)
        self.tbl_order.setHorizontalHeaderItem(3, header3)
        self.tbl_order.setHorizontalHeaderItem(4, header4)

        # ตั้งค่าความกว้าง column
        self.tbl_order.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.tbl_order.horizontalHeader().setSectionResizeMode(0)
        self.tbl_order.setColumnWidth(0, 30)
        self.tbl_order.setColumnWidth(1, 100)
        self.tbl_order.setColumnWidth(2, 90)
        # self.tbl_order.setColumnWidth(4, 135)
        self.tbl_order.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

    def addToTable(self):
        self.btn_view = list()
        try:
            for i, v in enumerate(self.orders):
                oid = v['oid']
                date = v['date']
                # Net Total
                total = 0
                for item in v['cart']:
                    total += item['price'] * item['qty']
                # ภาษีมูลค่าเพิ่ม
                vat = total * self.tax_rate / 100
                total += vat
                # ค่าจัดส่ง
                if v['shipping_info']['shipping']:
                    total += self.shipping_fee
                # คูปองส่วนลด
                # discount = 0 if v['coupon'] == "" else self.getCouponValue(v['coupon'])
                discount = float(v['coupon']['value'])
                total -= discount
                # สถานะ order
                # status = ORDER_STATUS["{}".format(v['status'])]
                status = getOrderStatus(v['status'])

                # Button สำหรับเลือก Order
                self.btn_view.append(QtWidgets.QPushButton("ดู"))
                order_info = (v['cart'], v['shipping_info'], v['coupon'], v['status'], total)
                self.btn_view[i].clicked.connect(partial(self.getSelectedOrder, i, oid, order_info))
                self.tbl_order.setCellWidget(i, 0, self.btn_view[i])

                self.tbl_order.setItem(i, 1, QTableWidgetItem("{}".format(oid)))

                self.tbl_order.setItem(i, 2, QTableWidgetItem("{}".format(date.replace(microsecond=0))))

                item_price = QTableWidgetItem("{:,.2f}".format(total))
                item_price.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                self.tbl_order.setItem(i, 3, item_price)

                item_status = QTableWidgetItem("{}".format(status))
                item_status.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                self.tbl_order.setItem(i, 4, item_status)

        except TypeError:
            pass  # สำหรับผู้ใช้ที่ไม่เคยมี Order มาก่อน

        finally:
            self.tbl_order.resizeRowsToContents()

    def getPriceSettings(self):
        settings = getSettings()
        self.shipping_fee = settings['shipping_fee']
        self.tax_rate = settings['tax_rate']

    # แสดง Order ที่กด 'ดู'
    def getSelectedOrder(self, i, oid, data):
        if not self.btn_cancelChange.isEnabled():
            # self.current_index = i
            self.current_oid = oid
            self.current_net_total = data[4]
            self.btn_view[i].setEnabled(False)
            self.setOrderBtnEnabled(True, data[3])
            # print("Order ID = {}".format(oid))
            self.lbl_orderId.setText("Order ID :\n{}".format(oid))
            self.lbl_order_list.setText("ข้อมูลคำสั่งซื้อ")
            self.lbl_cus_detail.setText("ข้อมูลในการจัดส่ง")
            self.txt_email.setDisabled(True)
            self.saveTempCusInfo()
            try:
                self.showOrderDetailTable(data)
            except Exception as e:
                print(e)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("ดูรายการคำสั่งซื้อ")
            msg.setIcon(msg.Warning)
            msg.setText("กรุณาทำการแก้ไขข้อมูลลูกค้าให้เรียบร้อยก่อน")
            msg.exec_()

    def showOrderDetailTable(self, data):
        cart = data[0]
        shipping = data[1]['shipping']
        coupon_code = "ไม่มี" if data[2]['code'] == "" else data[2]['code']
        discount = data[2]['value']

        num_row = len(cart) + 4
        self.setupOrderDetailTable(num_row)
        self.showShippingInfo(data[1])

        net_total = 0
        for i, v in enumerate(cart):
            price = v['price']
            qty = v['qty']
            total = price * qty
            net_total += total

            self.tbl_order.setItem(i, 0, QTableWidgetItem("{}".format(v['name'])))
            item_price = QTableWidgetItem("{:,.2f}".format(price))
            item_price.setTextAlignment(QtCore.Qt.AlignRight)
            self.tbl_order.setItem(i, 1, item_price)
            item_qty = QTableWidgetItem("{}".format(qty))
            item_qty.setTextAlignment(QtCore.Qt.AlignRight)
            self.tbl_order.setItem(i, 2, item_qty)
            item_total = QTableWidgetItem("{:,.2f}".format(total))
            item_total.setTextAlignment(QtCore.Qt.AlignRight)
            self.tbl_order.setItem(i, 3, item_total)
        # ภาษีมูลค่าเพิ่ม
        vat = net_total * self.tax_rate / 100
        net_total += vat
        self.tbl_order.setItem(num_row - 4, 0, QTableWidgetItem("ภาษี ({:g}%)".format(self.tax_rate)))
        item_shipping = QTableWidgetItem("{:,.2f}".format(vat))
        item_shipping.setTextAlignment(QtCore.Qt.AlignRight)
        self.tbl_order.setItem(num_row - 4, 3, item_shipping)
        # ค่าจัดส่ง
        shipping_fee = self.shipping_fee if shipping else 0
        net_total += shipping_fee
        shipping_text = "ส่งด่วน" if shipping_fee > 0 else "รับที่ร้าน"
        self.tbl_order.setItem(num_row - 3, 0, QTableWidgetItem("ค่าจัดส่ง ({})".format(shipping_text)))
        item_shipping = QTableWidgetItem("{:,.2f}".format(shipping_fee))
        item_shipping.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.tbl_order.setItem(num_row - 3, 3, item_shipping)
        # คูปองส่วนลด
        net_total -= discount if discount <= net_total else 0
        self.tbl_order.setItem(num_row - 2, 0, QTableWidgetItem("ส่วนลด ({})".format(coupon_code)))
        item_shipping = QTableWidgetItem("-{:,.2f}".format(discount))
        item_shipping.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.tbl_order.setItem(num_row - 2, 3, item_shipping)
        # Display 'net_total'
        font = QtGui.QFont()
        font.setBold(True)
        self.tbl_order.setItem(num_row - 1, 0, QTableWidgetItem("ราคาสุทธิ"))
        self.tbl_order.item(num_row - 1, 0).setFont(font)
        item_net_total = QTableWidgetItem("{:,.2f}".format(net_total))
        item_net_total.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        item_net_total.setFont(font)
        self.tbl_order.setItem(num_row - 1, 3, item_net_total)

    def setupOrderDetailTable(self, num_row):
        # Table Widget
        self.tbl_order.setRowCount(0)  # Reset Row
        self.tbl_order.setColumnCount(0)  # Reset Column
        self.tbl_order.setRowCount(num_row)
        self.tbl_order.setColumnCount(4)
        self.tbl_order.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # Table Read-only

        # สร้าง Header
        header1 = QtWidgets.QTableWidgetItem("รายการ")
        header2 = QtWidgets.QTableWidgetItem("ราคา/หน่วย")
        header3 = QtWidgets.QTableWidgetItem("จำนวน")
        header4 = QtWidgets.QTableWidgetItem("รวม")

        # ใส่ Header ให้ Table
        self.tbl_order.setHorizontalHeaderItem(0, header1)
        self.tbl_order.setHorizontalHeaderItem(1, header2)
        self.tbl_order.setHorizontalHeaderItem(2, header3)
        self.tbl_order.setHorizontalHeaderItem(3, header4)

        # ตั้งค่าความกว้าง column
        self.tbl_order.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Interactive)
        self.tbl_order.horizontalHeader().setStretchLastSection(True)
        # self.tbl_order.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tbl_order.setColumnWidth(0, 220)
        self.tbl_order.setColumnWidth(1, 90)
        self.tbl_order.setColumnWidth(2, 50)
        self.tbl_order.setColumnWidth(4, 60)

    def showShippingInfo(self, shipping_data):
        self.txt_name.setText(shipping_data['name'])
        self.txt_tel.setText(shipping_data['tel'])
        self.txt_address.setText(shipping_data['address'])

    def cancelOrder(self):
        oid = self.current_oid
        msg = QMessageBox()
        msg.setWindowTitle("ยกเลิกคำสั่งซื้อ")
        ans = msg.question(msg, "ยกเลิกคำสั่งซื้อ",
                           "คุณแน่ใจที่จะต้องการ 'ยกเลิกคำสั่งซื้อ' ใช่หรือไม่\n\nหากยกเลิกแล้วจะไม่สามารถย้อนกลับได้",
                           msg.Yes | msg.No)
        if ans == msg.Yes:
            with GetDatabase() as conn:
                db = conn.get_database('ucwb')
                con = {'oid': oid}
                found = db.orders.count_documents(con)
                if found:
                    setTo = {'$set': {'status': '-1'}}
                    db.orders.update_one(con, setTo)
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("ยกเลิกคำสั่งซื้อสำเร็จ!")
                    self.getCusOrders()  # Update Orders Table
                else:
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error: Cannot cancel your order...")
                msg.exec_()

    def showQrDialog(self):
        frm_cus_payment = QtWidgets.QDialog()
        _ui = CusPayment.Ui_frm_cus_payment(self.current_net_total, self.current_oid)
        # _ui.setAmount(self.current_net_total)
        _ui.setupUi(frm_cus_payment)
        CusPayment.frm_cus_payment = frm_cus_payment
        frm_cus_payment.exec_()

    def showTrackingInfo(self):
        oid = self.current_oid
        tracking_no = None
        msg = QMessageBox()
        msg.setWindowTitle("ข้อมูลการจัดส่ง")
        with GetDatabase() as conn:
            db = conn.get_database('ucwb')
            con = {'oid': oid}
            found = db.orders.count_documents(con)
            if found:
                cursor = db.orders.find(con)
                if "tracking_no" in cursor[0]['shipping_info']:
                    tracking_no = cursor[0]['shipping_info']['tracking_no']
                    tracking_no = None if tracking_no == "" else tracking_no
                if tracking_no is None:
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("ไม่พบข้อมูลการจัดส่ง")
                    msg.exec_()
                else:
                    confirm = msg.question(msg, "ข้อมูลการจัดส่ง",
                                           "Tracking No. : {} (คัดลอกแล้ว)\n\n"
                                           "ต้องการไปที่เว็บไซต์ตรวจสอบหมายเลขพัสดุหรือไม่".format(
                                               tracking_no), msg.Yes | msg.No)
                    pyperclip.copy(tracking_no)
                    if confirm == msg.Yes:
                        url = "https://track.thailandpost.co.th/?trackNumber={}".format(tracking_no)
                        webbrowser.open(url, new=0, autoraise=True)
            else:
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error: Order ID not found...")
                msg.exec_()

    # ยกเลิกดู Order Detail
    def backClicked(self):
        # self.btn_view[self.current_index].setEnabled(True)
        self.setOrderBtnEnabled(False)
        # self.current_index = None
        self.current_oid = None
        self.lbl_orderId.setText("Order ID :\n")
        self.lbl_order_list.setText("รายการคำสั่งซื้อ")
        self.lbl_cus_detail.setText("ข้อมูลลูกค้า")
        self.txt_email.setDisabled(False)
        # Load orders table
        try:
            self.loadTempCusInfo()
            # self.getCusOrders()
            self.setupTable()
            self.addToTable()
        except Exception as e:
            print(e)

    def confirmPayment(self):
        if self.current_oid is not None:
            frm_cus_uploadslip = QtWidgets.QDialog()
            _ui = CusUploadSlip.Ui_frm_cus_uploadslip(username=self.username, oid=self.current_oid)
            _ui.setupUi(frm_cus_uploadslip)
            CusUploadSlip.frm_cus_uploadslip = frm_cus_uploadslip
            frm_cus_uploadslip.exec_()
            self.getCusOrders()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("My Orders")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("กรุณาคลิกเลือกดูรายการคำสั่งซื้อก่อน")
            msg.exec_()

    def editCusInfo(self):
        if self.btn_changeCus.text() == "แก้ไขข้อมูล":
            self.btn_changeCus.setText("ยืนยัน")
            self.btn_cancelChange.setEnabled(True)
            self.setCusInfoReadOnly(boolean=False)
            self.saveTempCusInfo()
        else:
            msg = QMessageBox()
            confirm = msg.question(msg, "ยืนยันการแก้ไข", "ท่านต้องการบันทึกการแก้ไขข้อมูลลูกค้าใช่หรือไม่",
                                   msg.Yes | msg.No)
            if confirm == msg.Yes:
                self.saveCusInfo()
                self.btn_changeCus.setText("แก้ไขข้อมูล")
                self.btn_cancelChange.setEnabled(False)
                self.setCusInfoReadOnly(boolean=True)
                self.temp_cusInfo = tuple()

    def cancelEditCusInfo(self):
        msg = QMessageBox()
        confirm = msg.question(msg, "ยืนยันการยกเลิก", "ท่านต้องการยกเลิกการแก้ไขข้อมูลลูกค้าใช่หรือไม่",
                               msg.Yes | msg.No)
        if confirm == msg.Yes:
            self.btn_cancelChange.setEnabled(False)
            self.btn_changeCus.setText("แก้ไขข้อมูล")
            self.setCusInfoReadOnly(boolean=True)
            self.loadTempCusInfo()

    def saveTempCusInfo(self):
        self.temp_cusInfo = (self.txt_name.text(),
                             self.txt_tel.text(),
                             self.txt_email.text(),
                             self.txt_address.toPlainText())

    def loadTempCusInfo(self):
        self.txt_name.setText(self.temp_cusInfo[0])
        self.txt_tel.setText(self.temp_cusInfo[1])
        self.txt_email.setText(self.temp_cusInfo[2])
        self.txt_address.setText(self.temp_cusInfo[3])

    def saveCusInfo(self):
        name = self.txt_name.text().strip()
        tel = self.txt_tel.text().strip()
        email = self.txt_email.text().strip()
        address = self.txt_address.toPlainText().strip()
        msg = QMessageBox()
        msg.setWindowTitle("บันทึกข้อมูลลูกค้า")
        with GetDatabase() as conn:
            db = conn.get_database('ucwb')
            con = {'username': {"$regex": f'^{self.username}$', "$options": "i"}}
            found = db.users.count_documents(con)
            if found:
                setTo = {'$set': {'email': email,
                                  'shipping_info': {'name': name,
                                                    'tel': tel,
                                                    'address': address}}}
                db.users.update_one(con, setTo)
                msg.setIcon(QMessageBox.Information)
                msg.setText("บันทึกข้อมูลลูกค้าสำเร็จ!")
            else:
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error: Cannot save shipping info\nPlease login again...")
            msg.exec_()

    def setOrderBtnEnabled(self, boolean=True, status=None):
        self.btn_back.setEnabled(boolean)
        self.btn_viewMore.setEnabled(boolean)
        self.btn_changeCus.setVisible(not boolean)
        self.btn_changePwd.setVisible(not boolean)
        self.btn_cancelChange.setVisible(not boolean)
        if boolean and status is not None:
            boolean = True if '0' <= status <= '1' else False
            self.btn_confirm.setEnabled(boolean)
            self.btn_cancelOrder.setEnabled(boolean)
            self.btn_showQR.setEnabled(boolean)
        else:
            self.btn_confirm.setEnabled(boolean)
            self.btn_cancelOrder.setEnabled(boolean)
            self.btn_showQR.setEnabled(boolean)

    def setCusInfoReadOnly(self, boolean=True):
        self.txt_name.setReadOnly(boolean)
        self.txt_tel.setReadOnly(boolean)
        self.txt_email.setReadOnly(boolean)
        self.txt_address.setReadOnly(boolean)

    def changePassword(self):
        win_title = "เปลี่ยนรหัสผ่าน"
        msg = QMessageBox()
        msg.setWindowTitle(win_title)
        old_pwd, ok = QInputDialog.getText(frm_cus_myorder, win_title, "กรุณากรอกรหัสผ่านเดิม",
                                           QLineEdit.Password)
        if ok:
            with GetDatabase() as conn:
                db = conn.get_database('ucwb')
                condition = {'username': {"$regex": f'^{self.username}$', "$options": "i"}}
                found = db.users.count_documents(condition)
                if found:
                    cursor = db.users.find(condition)
                    # password จาก database
                    pwd_chunk = HashPassword(cursor[0]['password'])
                    salt = pwd_chunk.getSaltFromChunk()
                    key = pwd_chunk.getKeyFromChunk()
                    # password ที่เพิ่งกรอก
                    pwd = HashPassword(old_pwd).getHashedKey(salt)
                    if key != pwd:
                        msg.setIcon(msg.Critical)
                        msg.setText("รหัสผ่านไม่ถูกต้อง")
                        msg.exec_()
                    else:
                        new_pwd, ok = QInputDialog.getText(frm_cus_myorder, win_title, "กรุณากรอกรหัสผ่านใหม่",
                                                           QLineEdit.Password)
                        if ok:
                            renew_pwd, ok = QInputDialog.getText(frm_cus_myorder, win_title,
                                                                 "กรุณากรอกรหัสผ่านใหม่อีกครั้ง", QLineEdit.Password)
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

    def retranslateUi(self, frm_cus_myorder):
        _translate = QtCore.QCoreApplication.translate
        frm_cus_myorder.setWindowTitle(_translate("frm_cus_myorder", "UCWB - My Orders"))
        self.lbl_title.setText(_translate("frm_cus_myorder", "You Choose, We Build"))
        self.lbl_title_2.setText(_translate("frm_cus_myorder", "My Orders"))
        self.lbl_order_list.setText(_translate("frm_cus_myorder", "รายการคำสั่งซื้อ"))
        item = self.tbl_order.horizontalHeaderItem(0)
        item.setText(_translate("frm_cus_myorder", "ID"))
        item = self.tbl_order.horizontalHeaderItem(1)
        item.setText(_translate("frm_cus_myorder", "วันที่สั่งซื้อ"))
        item = self.tbl_order.horizontalHeaderItem(2)
        item.setText(_translate("frm_cus_myorder", "ราคารวม"))
        item = self.tbl_order.horizontalHeaderItem(3)
        item.setText(_translate("frm_cus_myorder", "สถานะ"))
        self.lbl_cus_detail.setText(_translate("frm_cus_myorder", "ข้อมูลลูกค้า"))
        self.btn_confirm.setText(_translate("frm_cus_myorder", "แจ้งการชำระเงิน"))
        self.lbl_name.setText(_translate("frm_cus_myorder", "ชื่อ-นามสกุล"))
        self.lbl_tel.setText(_translate("frm_cus_myorder", "เบอร์โทรศัพท์"))
        self.lbl_email.setText(_translate("frm_cus_myorder", "อีเมล"))
        self.lbl_address.setText(_translate("frm_cus_myorder", "ที่อยู่"))
        self.btn_changeCus.setText(_translate("frm_cus_myorder", "แก้ไขข้อมูล"))
        self.btn_cancelChange.setText(_translate("frm_cus_myorder", "ยกเลิก"))
        self.btn_changePwd.setText(_translate("frm_cus_myorder", "เปลี่ยนรหัสผ่าน"))
        self.btn_back.setText(_translate("frm_cus_myorder", "ย้อนกลับ"))
        self.btn_showQR.setText(_translate("frm_cus_myorder", "แสดง QR Code"))
        self.btn_cancelOrder.setText(_translate("frm_cus_myorder", "ยกเลิกคำสั่งซื้อ"))
        self.btn_viewMore.setText(_translate("frm_cus_myorder", "ข้อมูลการจัดส่ง"))
        self.lbl_orderId.setText(_translate("frm_cus_myorder", "Order ID :\n"))


frm_cus_myorder = None
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    frm_cus_myorder = QtWidgets.QDialog()
    ui = Ui_frm_cus_myorder()
    ui.setupUi(frm_cus_myorder)
    frm_cus_myorder.show()
    sys.exit(app.exec_())
