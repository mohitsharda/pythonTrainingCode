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

class Vehicle:

    def __init__(self, regNumber ="NA", Brand ="NA", model ="NA", color = "white"):
        self.regNumber = regNumber
        self.Brand = Brand
        self.model = model
        self.color = color

    def addVehicleDetails(self):
        print(">>>> ENTER VEHICLE DETAILS")
        self.regNumber = input("ENTER VEHICLE REGISTRATION DETAIL: ")
        self.Brand = input("ENTER VEHICLE BRAND : ")
        self.model = input("ENTER VEHICLE  MODEL : ")
        self.color = input("ENTER VEHICLE  COLOR : ")

    def show(self):
        print("\n------------- VEHICLE --------------")
        print("NUMBER: {} | BRAND: {}".format(self.regNumber, self.Brand))
        print("MODEL: {} | COLOR: {}".format(self.model, self.color))
        print("------------- VEHICLE --------------\n")

# vehicle = Vehicle()
# vehicle.addVehicleDetails()
# vehicle.show()
