# Welcome to YouChooseWeBuild-Project's Library
# Created by Phurit D.

import ssl
import certifi
from PyQt5 import QtWidgets, QtGui

from pymongo import MongoClient, errors as mongoError
from hashlib import pbkdf2_hmac
from os import urandom

ICON_PATH = "resource/logo/icon.ico"
ICON_PATH_ADMIN = "resource/logo/icon_admin.ico"

CONNECTION_STRING = "mongodb+srv://<...>"

ORDER_STATUS = {'-2': 'ไม่ผ่านการตรวจสอบ',
                '-1': 'ยกเลิกแล้ว',
                '0': 'รอการชำระเงิน',
                '1': 'รอแจ้งชำระเงิน',
                '2': 'กำลังตรวจสอบ',
                '3': 'รอการจัดส่ง',
                '4': 'จัดส่งแล้ว'}

REGEX_USERNAME = "^[A-Za-z0-9_-]*$"  # only contains letters, numbers, underscores and dashes
REGEX_TEL = "^[0-9]{3}-[0-9]{3}-[0-9]{4}$"  # for tel no.
REGEX_EMAIL = "^\\w+([\\.-]?\\w+)*@\\w+([\\.-]?\\w+)*(\\.\\w{2,3})+$"  # for email
REGEX_PASSWORD = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z\\d]{8,}$"  # length >= 8, uppercase & lowercase & number >= 1
REGEX_INT_0_100 = "\\b([0-9]|[1-9][0-9]|100)\\b"  # integer 0-100


# Connects to cloud database
class GetDatabase(object):

    def __init__(self, conn_str=CONNECTION_STRING):
        self.conn_str = conn_str
        self.client = None

    def __enter__(self):
        self.client = MongoClient(self.conn_str)
        # self.client = MongoClient(self.conn_str, tlsCAFile=certifi.where())  # In case of SSL error
        # self.testConn()
        return self.client

    # In case of [SSL: CERTIFICATE_VERIFY_FAILED]
    def testConn(self):
        try:
            db = self.client.get_database('ucwb')
            db.settings.count_documents({})
        except mongoError.ServerSelectionTimeoutError as e:
            print("ServerSelectionTimeoutError: {}".format(e))
            self.client = MongoClient(self.conn_str, tlsCAFile=certifi.where())  # for Windows
            # self.client = MongoClient(self.conn_str, ssl_cert_reqs=ssl.CERT_NONE)  # Secondary

    def __exit__(self, *args):
        self.client.close()


# Hashing password using HMAC-SHA256 method
class HashPassword:

    def __init__(self, pwd=""):
        self.password = pwd

    def getSaltAndHashChunk(self, salt=""):
        if salt == "":
            salt = urandom(32)  # Remember this
        password = self.password
        key = pbkdf2_hmac('sha256',  # The hash digest algorithm for HMAC
                          password.encode('utf-8'),  # Convert the password to bytes
                          salt,  # Provide the salt
                          100000  # It is recommended to use at least 100,000 iterations of SHA-256
                          )
        # Store them as:
        chunk = (salt + key)
        return chunk

    def getHashedKey(self, salt=""):
        password = self.password
        key = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return key

    def getSaltFromChunk(self, chunk=""):
        if chunk == "":
            chunk = self.password
        salt_from_chunk = chunk[:32]  # 32 is the length of the salt
        return salt_from_chunk

    def getKeyFromChunk(self, chunk=""):
        if chunk == "":
            chunk = self.password
        key_from_chunk = chunk[32:]
        return key_from_chunk


class QMessageBox(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon(ICON_PATH))


class AdminQMessageBox(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon(ICON_PATH_ADMIN))


def getSettings():
    settings = dict()
    with GetDatabase() as conn:
        db = conn.get_database('ucwb')
        # condition = {'name': 'shipping_fee'}
        # condition = {'name': 'tax_rate'}
        cursor = db.settings.find({})
        settings['shipping_fee'] = cursor[0]['value']
        settings['tax_rate'] = cursor[1]['value']
        settings['payment_detail'] = cursor[2]['value']
    return settings


def getCouponValue(code: str, no_check=False):
    value = 0
    with GetDatabase() as conn:
        db = conn.get_database('ucwb')
        con = {'code': code.upper()}
        found = db.coupons.count_documents(con)
        if found:
            cursor = db.coupons.find(con)
            coupon = cursor[0]
            if coupon['status'] or no_check:
                value = coupon['value']
    return value


def getOrderStatus(code):
    code = str(code)
    try:
        status = ORDER_STATUS[code]
    except KeyError:
        status = "N/A"
    return status
