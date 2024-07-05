#Customer Object -> name, phone, email, age, gender, createdOn

"""
   create table Customer(
       cId int primary key auto_increment,
       name varchar(256),
       phone varchar(256),
       email varchar(256),
       age int,
       gender varchar(20),
       created_on datetime
    );

"""
import datetime

class Customer:
    
    def __init__(self, cId = 0, name = "", phone = "" , email = "", age = 0, gender = ""):
        self.cId = cId
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        self.createdOn = datetime.datetime.now()

    def addCustomerDetail(self):
        self.name = input("ENTER CUSTOMER NAME: ")
        self.phone = input("ENTER CUSTOMER PHONENUMBER: ")
        self.email = input("ENTER CUSTOMER EMAIL : ")
        self.age = int(input("ENTER CUSTOMER AGE: "))
        self.gender = input("ENTER CUSTOMER GENDER : ")

        #we will not get input from created ON
        # Created on is a system data time stamp

    def updateCustomerDetail(self):
        name = input("EMTER CUSTOMER NAME:  ")
        if len(name) != 0:
            self.name = name

        phone = input("EMTER PHONE-NUMBER:  ")
        if len(phone) != 0:
            self.phone = phone

        email = input("EMTER EMAIL:  ")
        if len(email) != 0:
            self.email = email

        age = input("EMTER AGE:  ")
        if len(age) != 0:
            self.age = int(age)

        gender = input("EMTER GENDER:  ")
        if len(gender) != 0:
            self.gender = gender
        
    # def updateCustomerDetail(self):
        
    #     self.name = input("ENTER CUSTOMER NAME: ")
    #     self.phone = input("ENTER CUSTOMER PHONENUMBER: ")
    #     self.email = input("ENTER CUSTOMER EMAIL : ")
    #     self.age = int(input("ENTER CUSTOMER AGE: "))
    #     self.gender = input("ENTER CUSTOMER GENDER : ")
    
    def show(self):
        print("\n------------- CUSTOMER DETAIL --------------")
        print("CID: {}".format(self.cId))
        print("NAME: {} | PHONENUMBER: {}".format(self.name, self.phone))
        print("EMAIL: {} | AGE: {}".format(self.email, self.age))
        print("GENDER: {}".format(self.gender))
        print("--------------------------")
