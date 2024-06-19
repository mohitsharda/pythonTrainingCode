"""
   Driver has a vehicle
   Customer can book Ride(s)

   1.Driver  -  Name, phoneNumber, vehicleType [1 - 1], licenceNumber, rating, gender, Age 
                1 driver has 1 vehicle

   2.Vehicle - regNumber, Brand, model, color

   3.Customer - Name , phoneNumber, Address, email, gender, age

   4. Ride - customer [1 - 1], date, time, fromLoaction,  toLocation, distance, fare, driver[1 - 1], Destination
                1 ride has 1 customer 
                1 ride has 1 driver

"""

from session10B import Driver
from session10A import Vehicle

driver = Driver()
driver.addDriverDetails()
driver.show


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
        self.Age = int(input("ENTER CUSTOMER AGE : "))

    def show(self):
        print("\n------------- CUSTOMER DETAIL --------------")
        print("NAME: {} | PHONENUMBER: {}".format(self.Name, self.phoneNumber))
        print("ADDRESS: {} | EMAIL: {}".format(self.Address, self.email))
        print("GENDER: {} | AGE: ".format(self.gender, self.age))


vehicle = Vehicle()
vehicle.show


driver = Driver()
driver.show

customer = Customer()
customer.addCustomerDetails()
customer.show()