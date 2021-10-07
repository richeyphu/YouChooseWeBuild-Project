import datetime
import hashlib
import os
import bson
from base64 import b64encode

"""

Add Package 1.) PyQt5-stubs ,  2.) pyqt5-tools , 3.) PyQt5
คำสั่งแปลง  Terminal →  pyuic5 -x FileUI.ui -o FilePython.py

"""


def ppTest():
    account = "0809167238"
    path = "temp/qrtest.png"

    from pypromptpay import qr_code

    data = qr_code(account, one_time=True, path_qr_code="", country="TH", money="1", currency="THB")
    print(">> {}".format(data))

    import qrcode

    img = qrcode.make(data)
    imgload = open(path, 'wb')  # สร้างไฟล์ไบต์ใหม่ขึ้นมา กำหนดสิทธิ์เขียนไฟล์ได้
    img.save(imgload, 'PNG')  # บันทึกค่า QR Code เข้าไปยังไฟล์
    imgload.close()  # ปิดไฟล์


def sha256Test():
    string = "temp"
    encoded = string.encode()
    result = hashlib.sha256(encoded)

    print("String : {}".format(string))
    print("Hash Value : {}".format(result))
    print("Hexadecimal equivalent: {}".format(result.hexdigest()))
    print("Digest Size : {}".format(result.digest_size))
    print("Block Size : {}".format(result.block_size))


def pwdEncryptTest():
    # txt = input("Enter password : ")
    txt = "temp"
    encoded_txt = txt.encode()
    hashed_txt = hashlib.sha256(encoded_txt).hexdigest()

    pwd = "temp"
    encoded_pwd = pwd.encode()
    hashed_pwd = hashlib.sha256(encoded_pwd).hexdigest()

    print()
    print(hashed_txt)
    print(hashed_pwd)
    print()

    if hashed_pwd == hashed_txt:
        print("Valid")
    else:
        print("Invalid")


def hmacTest():
    # https://nitratine.net/blog/post/how-to-hash-passwords-in-python/

    salt = os.urandom(32)  # Remember this
    password = 'password123'

    key = hashlib.pbkdf2_hmac('sha256',  # The hash digest algorithm for HMAC
                              password.encode('utf-8'),  # Convert the password to bytes
                              salt,  # Provide the salt
                              100000  # It is recommended to use at least 100,000 iterations of SHA-256
                              )

    # Store them as:
    storage = (salt + key)

    # Getting the values back out
    salt_from_storage = storage[:32]  # 32 is the length of the salt
    key_from_storage = storage[32:]

    print(storage)
    print(salt_from_storage)
    print(key_from_storage)

    print()

    storage = storage.hex()
    salt_from_storage = storage[:64]
    key_from_storage = storage[64:]
    print(salt_from_storage)
    print(key_from_storage)
    print(bytearray(salt_from_storage.encode()))
    print(bytearray(key_from_storage.encode()))


def testFindDB():
    search_txt = "temp"
    brand = ""
    keyword = ""


if __name__ == '__main__':
    pass

    # ppTest()

    # sha256Test()

    # pwdEncryptTest()

    # hmacTest()

    # testFindDB()
    date = datetime.datetime.now().replace(microsecond=0)
    print(date)
