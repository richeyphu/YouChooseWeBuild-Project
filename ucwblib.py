# Welcome to YouChooseWeBuild-Project's Library
# Created by Phurit D.

from pymongo import MongoClient

from hashlib import pbkdf2_hmac
from os import urandom

# CONNECTION_STRING = "mongodb+srv://<...>"
# CONNECTION_STRING = "mongodb+srv://admin:NOCvZLbzSxi8IsCB@cluster0.cc3d8.mongodb.net/myShop?retryWrites=true&w=majority"
CONNECTION_STRING = "mongodb+srv://tni:zfqN44SoOI7dBwSm@cluster0.cc3d8.mongodb.net/myShop?retryWrites=true&w=majority"


# Connect to cloud database
class GetDatabase(object):

    def __init__(self, conn_str=CONNECTION_STRING):
        self.conn_str = conn_str

    def __enter__(self):
        self.client = MongoClient(self.conn_str)
        return self.client

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
