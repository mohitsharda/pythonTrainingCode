"""
   OOPS CASE STUDY
 
   Customer -> name, phoneNumber, email, Address, Gender, Age
   Dish -> 
   Order ->

   1 Customer can place many order
   1 Order can have many Dishes

"""

class Customer:
    
    def __init__(self, name = "NA", phoneNumber = "NA", email = "NA", Address = "NA"):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.Address = Address
        # self.Gender = Gender
        # self.Age = Age

    # def addCustomerDetails(self):
    #     self.name = input("ENTER CUSTOMER NAME: ")
    #     self.phoneNumber = input("ENTER CUSTOMER PHONE-NUMBER: ")
    #     self.email = input("ENTER CUSTOMER EMAIL: ")
    #     self.Address = input("ENTER CUSTOMER ADDRESS: ")
        # self.Gender = input("ENTER CUSTOMER GENDER: ")
        # self.Age = int(input("ENTER CUSTOMER AGE: "))

    def show(self):
        print("-------------CUSTOMER DETAIL--------------")
        print("Name: {} | PHONE-NUMBER {}".format(self.name, self.phoneNumber))
        print("EMAIL: {} | ADDRESS: {}".format(self.email, self.Address))
        # print("GENDER: {} | AGE {}".format(self.Gender, self.Age))
        print("-------------CUSTOMER DETAIL--------------")


# customer = Customer()
# customer.addCustomerDetails()
# customer.show()


