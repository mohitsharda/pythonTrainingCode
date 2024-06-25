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

from session10A import Vehicle

class Driver:

    def __init__(self, Name = "NA", phoneNumber = 0, email = "NA", licenceNumber = "NA", rating = 2.5, gender = "NA", Age = 18, vehicle = None):
        self.Name = Name
        self.phoneNumber = phoneNumber
        self.email = email
        self.licenceNumber = licenceNumber
        self.rating = rating
        self.gender = gender
        self.Age = Age
        self.vehicle = vehicle

    def addDriverDetails(self):
        print(">>>> ENTER DRIVER DETAILS")
        self.Name = input("ENTER NAME: ")
        self.phoneNumber = input("ENTER PHONENUMBER: ")
        self.email = input("ENTER EMAIL: ")
        self.licenceNumber = input("ENTER LICENSENUMBER : ")
        self.rating = float(input("ENTER RATING: "))
        self.gender = input("ENTER GENDER : ")
        self.Age = int(input("ENTER AGE : "))

        # 1 to 1 MAPPING
        # 1 driver has 1 vehicle
        self.vehicle = Vehicle() # object CONSTRUCTION
        self.vehicle.addVehicleDetails()


    def show(self):
        print("\n------------- DRIVER --------------")
        print("NAME: {} | PHONENUMBER: {}".format(self.Name, self.phoneNumber))
        print("EMAIL: {} | LICENSE NUMBER: {}".format(self.email, self.licenceNumber))
        print("RATING: {} | GENDER: {} | AGE: {}".format(self.rating, self.gender, self.Age))
        print("------------- DRIVER --------------")
        self.vehicle.show()

# vehicle = Vehicle()
# vehicle.show

# driver = Driver()
# driver.addDriverDetails()
# driver.show()

