# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/cus_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from functools import partial

import pymongo

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QTableWidgetItem

from ucwblib import GetDatabase
import CusCheckout
import CusMyOrder


class Ui_frm_cus_main(object):

    def setupUi(self, frm_cus_main):
        frm_cus_main.setObjectName("frm_cus_main")
        frm_cus_main.setWindowModality(QtCore.Qt.ApplicationModal)
        frm_cus_main.resize(1080, 720)
        frm_cus_main.setMinimumSize(QtCore.QSize(1080, 720))
        frm_cus_main.setMaximumSize(QtCore.QSize(1080, 720))
        frm_cus_main.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(frm_cus_main)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_item = QtWidgets.QFrame(self.centralwidget)
        self.frame_item.setGeometry(QtCore.QRect(250, 70, 811, 611))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        self.frame_item.setFont(font)
        self.frame_item.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_item.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_item.setObjectName("frame_item")
        self.tbl_item = QtWidgets.QTableWidget(self.frame_item)
        self.tbl_item.setGeometry(QtCore.QRect(0, 60, 811, 551))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(11)
        self.tbl_item.setFont(font)
        self.tbl_item.setObjectName("tbl_item")
        self.tbl_item.setColumnCount(5)
        self.tbl_item.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_item.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_item.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_item.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_item.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_item.setHorizontalHeaderItem(4, item)
        self.cmb_brand = QtWidgets.QComboBox(self.frame_item)
        self.cmb_brand.setGeometry(QtCore.QRect(10, 30, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.cmb_brand.setFont(font)
        self.cmb_brand.setObjectName("cmb_brand")
        self.cmb_brand.addItem("")
        self.lbl_brand = QtWidgets.QLabel(self.frame_item)
        self.lbl_brand.setGeometry(QtCore.QRect(10, 0, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_brand.setFont(font)
        self.lbl_brand.setObjectName("lbl_brand")
        self.lbl_spec = QtWidgets.QLabel(self.frame_item)
        self.lbl_spec.setGeometry(QtCore.QRect(150, 0, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_spec.setFont(font)
        self.lbl_spec.setObjectName("lbl_spec")
        self.cmb_spec = QtWidgets.QComboBox(self.frame_item)
        self.cmb_spec.setGeometry(QtCore.QRect(150, 30, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.cmb_spec.setFont(font)
        self.cmb_spec.setObjectName("cmb_spec")
        self.cmb_spec.addItem("")
        self.lbl_sortby = QtWidgets.QLabel(self.frame_item)
        self.lbl_sortby.setGeometry(QtCore.QRect(290, 0, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.lbl_sortby.setFont(font)
        self.lbl_sortby.setObjectName("lbl_sortby")
        self.cmb_sortby = QtWidgets.QComboBox(self.frame_item)
        self.cmb_sortby.setGeometry(QtCore.QRect(290, 30, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.cmb_sortby.setFont(font)
        self.cmb_sortby.setObjectName("cmb_sortby")
        self.cmb_sortby.addItem("")
        self.cmb_sortby.addItem("")
        self.cmb_sortby.addItem("")
        self.cmb_sortby.addItem("")
        self.cmb_sortby.addItem("")
        self.cmb_sortby.addItem("")
        self.btn_search = QtWidgets.QPushButton(self.frame_item)
        self.btn_search.setGeometry(QtCore.QRect(730, 20, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(12)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.txt_search = QtWidgets.QLineEdit(self.frame_item)
        self.txt_search.setGeometry(QtCore.QRect(482, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.txt_search.setFont(font)
        self.txt_search.setObjectName("txt_search")
        self.frame_header = QtWidgets.QFrame(self.centralwidget)
        self.frame_header.setGeometry(QtCore.QRect(0, 0, 1081, 61))
        self.frame_header.setStyleSheet("background-color: rgb(0, 148, 217);")
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setObjectName("frame_header")
        self.lbl_title = QtWidgets.QLabel(self.frame_header)
        self.lbl_title.setGeometry(QtCore.QRect(20, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(20)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_hi = QtWidgets.QLabel(self.frame_header)
        self.lbl_hi.setGeometry(QtCore.QRect(760, 10, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.lbl_hi.setFont(font)
        self.lbl_hi.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbl_hi.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_hi.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_hi.setObjectName("lbl_hi")
        self.frame_menubar = QtWidgets.QFrame(self.centralwidget)
        self.frame_menubar.setGeometry(QtCore.QRect(10, 70, 231, 611))
        self.frame_menubar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menubar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menubar.setObjectName("frame_menubar")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_menubar)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 211, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_cpu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.btn_cpu.setFont(font)
        self.btn_cpu.setObjectName("btn_cpu")
        self.verticalLayout.addWidget(self.btn_cpu)
        self.btn_mainboard = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.btn_mainboard.setFont(font)
        self.btn_mainboard.setObjectName("btn_mainboard")
        self.verticalLayout.addWidget(self.btn_mainboard)
        self.btn_vgacard = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.btn_vgacard.setFont(font)
        self.btn_vgacard.setObjectName("btn_vgacard")
        self.verticalLayout.addWidget(self.btn_vgacard)
        self.btn_memory = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.btn_memory.setFont(font)
        self.btn_memory.setObjectName("btn_memory")
        self.verticalLayout.addWidget(self.btn_memory)
        self.btn_harddisk = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.btn_harddisk.setFont(font)
        self.btn_harddisk.setObjectName("btn_harddisk")
        self.verticalLayout.addWidget(self.btn_harddisk)
        self.btn_ssd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.btn_ssd.setFont(font)
        self.btn_ssd.setObjectName("btn_ssd")
        self.verticalLayout.addWidget(self.btn_ssd)
        self.btn_psu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.btn_psu.setFont(font)
        self.btn_psu.setObjectName("btn_psu")
        self.verticalLayout.addWidget(self.btn_psu)
        self.btn_case = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.btn_case.setFont(font)
        self.btn_case.setObjectName("btn_case")
        self.verticalLayout.addWidget(self.btn_case)
        self.btn_cpucooler = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.btn_cpucooler.setFont(font)
        self.btn_cpucooler.setObjectName("btn_cpucooler")
        self.verticalLayout.addWidget(self.btn_cpucooler)
        self.btn_monitor = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_monitor.sizePolicy().hasHeightForWidth())
        self.btn_monitor.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.btn_monitor.setFont(font)
        self.btn_monitor.setObjectName("btn_monitor")
        self.verticalLayout.addWidget(self.btn_monitor)
        self.btn_build = QtWidgets.QPushButton(self.frame_menubar)
        self.btn_build.setGeometry(QtCore.QRect(10, 510, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.btn_build.setFont(font)
        self.btn_build.setStyleSheet("background:rgb(255, 124, 10);\n"
                                     "color: rgb(255, 255, 255);")
        self.btn_build.setObjectName("btn_build")
        self.lbl_total = QtWidgets.QLabel(self.frame_menubar)
        self.lbl_total.setGeometry(QtCore.QRect(75, 470, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(18)
        self.lbl_total.setFont(font)
        self.lbl_total.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_total.setObjectName("lbl_total")
        self.lbl_totaltxt = QtWidgets.QLabel(self.frame_menubar)
        self.lbl_totaltxt.setGeometry(QtCore.QRect(10, 470, 50, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(18)
        self.lbl_totaltxt.setFont(font)
        self.lbl_totaltxt.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbl_totaltxt.setObjectName("lbl_totaltxt")
        self.btn_settings = QtWidgets.QPushButton(self.frame_menubar)
        self.btn_settings.setGeometry(QtCore.QRect(10, 570, 211, 39))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(14)
        self.btn_settings.setFont(font)
        self.btn_settings.setObjectName("btn_settings")
        frm_cus_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frm_cus_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        frm_cus_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frm_cus_main)
        self.statusbar.setObjectName("statusbar")
        frm_cus_main.setStatusBar(self.statusbar)

        self.retranslateUi(frm_cus_main)
        QtCore.QMetaObject.connectSlotsByName(frm_cus_main)

        # var
        self.total = 0
        self.cat_total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cat_selected = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

        self.setUsername()
        self.showProducts()

        # Event-Driven
        # Product Categories button clicked
        self.btn_cpu.clicked.connect(lambda: self.showProducts(cat='101'))
        self.btn_mainboard.clicked.connect(lambda: self.showProducts(cat='102'))
        self.btn_vgacard.clicked.connect(lambda: self.showProducts(cat='103'))
        self.btn_memory.clicked.connect(lambda: self.showProducts(cat='104'))
        self.btn_harddisk.clicked.connect(lambda: self.showProducts(cat='105'))
        self.btn_ssd.clicked.connect(lambda: self.showProducts(cat='106'))
        self.btn_psu.clicked.connect(lambda: self.showProducts(cat='107'))
        self.btn_case.clicked.connect(lambda: self.showProducts(cat='108'))
        self.btn_cpucooler.clicked.connect(lambda: self.showProducts(cat='109'))
        self.btn_monitor.clicked.connect(lambda: self.showProducts(cat='110'))
        self.btn_search.clicked.connect(lambda: self.searchProducts(cat=self.current_cat))

        self.btn_build.clicked.connect(self.buildNow)
        self.btn_settings.clicked.connect(self.myOrder)

        # self.tbl_item.mousePressEvent = self.getSelectItem
        frm_cus_main.keyPressEvent = self.ctrlKey_press
        frm_cus_main.keyReleaseEvent = self.ctrlKey_release

    def ctrlKey_press(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.btn_build.setText("Clear All")

    def ctrlKey_release(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.btn_build.setText("Build Now")

    def showProducts(self, cat='101'):
        self.current_cat = cat

        # with pymongo.MongoClient(CONN_STR) as conn:
        with GetDatabase() as conn:
            db = conn.get_database('myShop')
            condition = {'cat': cat}
            count = db.products.count_documents(condition)
            cursor = db.products.find(condition)
            # cursor = list(db.products.find(condition))

            # สร้างตาราง
            self.setupTable(count)

            # เอาข้อมูลใน cursor ไปใส่เป็น item
            self.addToTable(cursor)

            # self.current_catTable = cursor

    def addToTable(self, cursor, same_page=False):
        brands = set()
        keywords = set()
        self.widget_spin = list()

        for i, v in enumerate(cursor):
            brand = v['brand']
            brands.add(brand)
            keywords.add(v['keyword'])
            pid = v['pid']

            # Spinner สำหรับเลือกจำนวนสินค้า
            self.widget_spin.append(QtWidgets.QSpinBox())
            # ตรวจสอบว่าสินค้านี้เคยถูกเลือกไปแล้วหรือเปล่า
            current_cat_index = int(self.current_cat) % 100 - 1
            if pid in self.cat_selected[current_cat_index]:
                qty_value = self.cat_selected[current_cat_index][pid]
                self.widget_spin[i].setValue(qty_value[0])
            else:
                self.widget_spin[i].setValue(0)
            self.widget_spin[i].setLocale(QLocale("en-us"))
            self.widget_spin[i].valueChanged.connect(partial(self.getSelectItem, i, self.current_cat))
            self.tbl_item.setCellWidget(i, 0, self.widget_spin[i])

            self.tbl_item.setItem(i, 1, QTableWidgetItem("{}".format(v['name'])))
            self.tbl_item.setItem(i, 2, QTableWidgetItem("{}".format(v['desc'])))
            self.tbl_item.setItem(i, 3, QTableWidgetItem("{}".format(brand)))

            item_price = QTableWidgetItem("{:,.2f}".format(v['price']))
            item_price.setTextAlignment(QtCore.Qt.AlignRight)
            self.tbl_item.setItem(i, 4, item_price)

            self.tbl_item.setItem(i, 5, QTableWidgetItem("{}".format(v['pid'])))

        if not same_page:
            self.setCombobox(brands, keywords)

    def searchProducts(self, cat='101'):
        search_txt = self.txt_search.text()
        brand = str(self.cmb_brand.currentText())
        keyword = str(self.cmb_spec.currentText())
        sortby = self.cmb_sortby.currentIndex()

        conditions = [{'cat': cat}]
        if search_txt != "":
            # con1 = {'name': {"$regex": f'{search_txt}', "$options": "i"}}
            con1 = {'$or': [{'name': {"$regex": f'{search_txt}',
                                      "$options": "i"}},
                            {'desc': {"$regex": f'{search_txt}',
                                      "$options": "i"}},
                            {'keyword': {"$regex": f'{search_txt}',
                                         "$options": "i"}}
                            ]}
            conditions.append(con1)
        if self.cmb_brand.currentIndex() > 0:
            con2 = {'brand': brand}
            conditions.append(con2)
        if self.cmb_spec.currentIndex() > 0:
            con3 = {'keyword': keyword}
            conditions.append(con3)
        # print(conditions)

        sort_con = []
        if sortby == 1:
            sort_con.append(('name', pymongo.ASCENDING))
        elif sortby == 2:
            sort_con.append(('name', pymongo.DESCENDING))
        elif sortby == 3:
            sort_con.append(('date_added', pymongo.DESCENDING))
        elif sortby == 4:
            sort_con.append(('price', pymongo.ASCENDING))
        elif sortby == 5:
            sort_con.append(('price', pymongo.DESCENDING))
        else:
            sort_con.append(('id', pymongo.ASCENDING))
        # print(sort_con)

        with GetDatabase() as conn:
            db = conn.get_database('myShop')

            where = {'$and': conditions}  # if len(conditions) > 0 else {}

            count = db.products.count_documents(where)
            cursor = db.products.find(where).sort(sort_con)

            self.setupTable(count)
            self.addToTable(cursor, same_page=True)

        # print("search  = {}".format(search_txt))
        # print("brand   = {}".format(brand))
        # print("keyword = {}".format(keyword))
        # print("sort by = {}".format(sortby))
        # print("FOUND   = {}\n".format(count))

    def getSelectItem(self, index, cat):
        try:
            value = self.widget_spin[index].value()
            price = float(self.tbl_item.item(index, 4).text().replace(',', ''))

            cat_index = int(cat) % 100 - 1
            # self.cat_total[cat_index] = value * price
            self.cat_selected[cat_index][self.tbl_item.item(index, 5).text()] = (value, price)
            self.calTotal()
            # print(self.cat_selected)

        except Exception as e:
            print(e)

        # print("value = {}".format(value))
        # print("price = {}".format(price))
        # print("total = {}".format(total))

    def calTotal(self):
        for i, cat_dict in enumerate(self.cat_selected):
            pid_list = cat_dict.keys()
            sum_cat = 0
            for pid in pid_list:
                sum_cat += cat_dict[pid][0] * cat_dict[pid][1]
                # print("{} = {}".format(cat_dict[pid], cat_dict[pid][0] * cat_dict[pid][1]))
            self.cat_total[i] = sum_cat
        # print()
        self.total = sum(self.cat_total)
        self.lbl_total.setText("{:,.2f}".format(self.total))

    def setupTable(self, count):
        # Table Widget
        self.tbl_item.setRowCount(count)
        self.tbl_item.setColumnCount(6)
        self.tbl_item.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # Table Read-only

        # สร้าง Header
        header1 = QtWidgets.QTableWidgetItem("QTY")
        header2 = QtWidgets.QTableWidgetItem("ชื่อ")
        header3 = QtWidgets.QTableWidgetItem("รายละเอียด")
        header4 = QtWidgets.QTableWidgetItem("ยี่ห้อ")
        header5 = QtWidgets.QTableWidgetItem("ราคาต่อหน่วย")
        header6 = QtWidgets.QTableWidgetItem("ID")

        # ใส่ Header ให้ Table
        self.tbl_item.setHorizontalHeaderItem(0, header1)
        self.tbl_item.setHorizontalHeaderItem(1, header2)
        self.tbl_item.setHorizontalHeaderItem(2, header3)
        self.tbl_item.setHorizontalHeaderItem(3, header4)
        self.tbl_item.setHorizontalHeaderItem(4, header5)
        self.tbl_item.setHorizontalHeaderItem(5, header6)

        # ตั้งค่าความกว้าง column
        self.tbl_item.setColumnWidth(0, 50)
        self.tbl_item.setColumnWidth(1, 240)
        self.tbl_item.setColumnWidth(2, 300)
        self.tbl_item.setColumnWidth(5, 70)

    def setCombobox(self, brands=set(), keywords=set()):
        brands = sorted(brands, key=str.casefold)
        keywords = sorted(keywords, key=str.casefold)

        self.cmb_sortby.setCurrentIndex(0)

        self.cmb_brand.clear()
        self.cmb_brand.addItem("Show All")
        for brand in brands:
            self.cmb_brand.addItem(brand)

        self.cmb_spec.clear()
        self.cmb_spec.addItem("Show All")
        for keyword in keywords:
            self.cmb_spec.addItem(keyword)

    def setUsername(self):
        self.lbl_hi.setText("Hi, {}".format(USERNAME))

    def buildNow(self):
        if self.btn_build.text() == "Build Now":
            CusCheckout.frm_cus_checkout.exec_()
        else:
            self.lbl_total.setText("0.00")
            for _dict in self.cat_selected:
                _dict.clear()
            self.showProducts()

    def myOrder(self):
        CusMyOrder.frm_cus_myorder.exec_()

    def retranslateUi(self, frm_cus_main):
        _translate = QtCore.QCoreApplication.translate
        frm_cus_main.setWindowTitle(_translate("frm_cus_main", "You Choose, We Build"))
        item = self.tbl_item.horizontalHeaderItem(1)
        item.setText(_translate("frm_cus_main", "ชื่อ"))
        item = self.tbl_item.horizontalHeaderItem(2)
        item.setText(_translate("frm_cus_main", "รายละเอียด"))
        item = self.tbl_item.horizontalHeaderItem(3)
        item.setText(_translate("frm_cus_main", "ยี่ห้อ"))
        item = self.tbl_item.horizontalHeaderItem(4)
        item.setText(_translate("frm_cus_main", "ราคาต่อหน่วย"))
        self.cmb_brand.setItemText(0, _translate("frm_cus_main", "Show All"))
        self.lbl_brand.setText(_translate("frm_cus_main", "Brand"))
        self.lbl_spec.setText(_translate("frm_cus_main", "Specification"))
        self.cmb_spec.setItemText(0, _translate("frm_cus_main", "Show All"))
        self.lbl_sortby.setText(_translate("frm_cus_main", "Sort by"))
        self.cmb_sortby.setItemText(0, _translate("frm_cus_main", "..."))
        self.cmb_sortby.setItemText(1, _translate("frm_cus_main", "ชื่อ A-Z"))
        self.cmb_sortby.setItemText(2, _translate("frm_cus_main", "ชื่อ Z-A"))
        self.cmb_sortby.setItemText(3, _translate("frm_cus_main", "ล่าสุด"))
        self.cmb_sortby.setItemText(4, _translate("frm_cus_main", "ราคาต่ำสุด"))
        self.cmb_sortby.setItemText(5, _translate("frm_cus_main", "ราคาสูงสุด"))
        self.btn_search.setText(_translate("frm_cus_main", "ค้นหา"))
        self.lbl_title.setText(_translate("frm_cus_main", "You Choose, We Build"))
        self.lbl_hi.setText(_translate("frm_cus_main", "Hi, username!"))
        self.btn_cpu.setText(_translate("frm_cus_main", "CPU"))
        self.btn_mainboard.setText(_translate("frm_cus_main", "Mainboard"))
        self.btn_vgacard.setText(_translate("frm_cus_main", "VGA Card"))
        self.btn_memory.setText(_translate("frm_cus_main", "Memory"))
        self.btn_harddisk.setText(_translate("frm_cus_main", "Harddisk"))
        self.btn_ssd.setText(_translate("frm_cus_main", "Solid State Drive"))
        self.btn_psu.setText(_translate("frm_cus_main", "Power Supply"))
        self.btn_case.setText(_translate("frm_cus_main", "Case"))
        self.btn_cpucooler.setText(_translate("frm_cus_main", "CPU Cooler"))
        self.btn_monitor.setText(_translate("frm_cus_main", "Monitor"))
        self.btn_build.setText(_translate("frm_cus_main", "Build Now"))
        self.lbl_total.setText(_translate("frm_cus_main", "0.00"))
        self.lbl_totaltxt.setText(_translate("frm_cus_main", "Total"))
        self.btn_settings.setText(_translate("frm_cus_main", "My Orders"))


USERNAME = "{username}"

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    frm_cus_main = QtWidgets.QMainWindow()
    ui = Ui_frm_cus_main()
    ui.setupUi(frm_cus_main)
    frm_cus_main.show()
    sys.exit(app.exec_())
else:
    import sys

    app = QtWidgets.QApplication(sys.argv)
    frm_cus_main = QtWidgets.QMainWindow()
    # ui = Ui_frm_cus_main()
    # ui.setupUi(frm_cus_main)


def setup_ui():
    ui = Ui_frm_cus_main()
    ui.setupUi(frm_cus_main)
