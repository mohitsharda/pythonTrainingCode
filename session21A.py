import datetime
import hashlib

class User:

    def __init__(self, name="", phone="", email="", passWord="", age="", gender=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.passWord = passWord
        self.age = age
        self.gender = gender
        self.createdOn = datetime.datetime.now()

    def addUserDetail(self):
        self.name = input("ENTER YOUR NAME :")
        self.phone = input("ENTER YOUR PHONE :")
        self.email = input("ENTER YOUR EMAIL :")

        self.passWord = input("ENTER YOUR PASS-WORD :").encode('utf-8')
        self.passWord = hashlib.sha256(self.passWord).hexdigest()

        self.age = input("ENTER YOUR AGE :")        
        self.gender = input("ENTER YOUR GENDER :")        

# users = User()
# users.addUserDetail()
# print(vars(user))