class Customer:

    def __init__(self, Name = "NA", phoneNumber = "NA", Address = "NA", email = "NA", gender = "NA", age = 0):
        self.Name = Name
        self.phoneNumber = phoneNumber
        self.Address = Address
        self.email = email
        self.gender = gender
        self.age = age

    def addCustomerDetails(self):
        print(">>>> ENTER CUSTOMER DETAILS")
        self.Name = input("ENTER CUSTOMER NAME: ")
        self.phoneNumber = input("ENTER CUSTOMER PHONENUMBER: ")
        self.Address = input("ENTER CUSTOMER ADDRESS : ")
        self.email = input("ENTER CUSTOMER EMAIL: ")
        self.gender = input("ENTER CUSTOMER GENDER : ")
        self.age = input("ENTER CUSTOMER AGE : ")

    def show(self):
        print("\n------------- CUSTOMER DETAIL --------------")
        print("NAME: {} | PHONENUMBER: {}".format(self.Name, self.phoneNumber))
        print("ADDRESS: {} | EMAIL: {}".format(self.Address, self.email))
        print("GENDER: {} | AGE: ".format(self.gender, self.age))


    def toCsv(self):
        data = "{}, {}, {}, {}, {}, {}\n".format(self.Name, self.phoneNumber, self.email, self.Address, self.gender, self.age)

        return data