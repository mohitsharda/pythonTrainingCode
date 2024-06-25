"""
   Driver has a vehicle
   Customer can book Ride(s)

   1.Driver  -  Name, phoneNumber, vehicleType [1 - 1], licenceNumber, rating, gender, Age 
                1 driver has 1 vehicle

   2.Vehicle - regNumber, Brand, model, color

   3.Customer - Name , phoneNumber, Address, email, gender, age

   4. Ride - customer [1 - 1], date, time, fromLoaction,  toLocation, distance, fare, driver[1 - 1]
                1 ride has 1 customer 
                1 ride has 1 driver

"""

from session10C import Customer
from session10B import Driver
from session10A import Vehicle

class Ride:

    def __init__(self, customer = None, date = "20June 2024", time = "12:00", fromLoaction = "Work",  toLocation = "Home", distance = 4, fare = 200, driver = None):
        self.customer = customer
        self.date = date
        self.time = time
        self.fromLoaction = fromLoaction
        self.toLocation = toLocation
        self.distance = distance
        self.fare = fare
        self.driver = driver

    def addRideDetails(self):
        print(">>>> RIDE DETAILS")
        self.fromLoactiont = input("ENTER FROM LOCATION: ")
        self.toLocation = input("ENTER TO LOCATION: ")
    
    def linkCustomer(self, customer):
        self.customer = customer

    def linkDriver(self, driver):
        self.driver = driver

    def show(self):
        self.customer.show()

        print("\n------------- RIDE DETAIL --------------")

        print("FROMLOCATION: {} | TOLOCATION: {}".format(self.fromLoactiont, self.toLocation))
        print("DISTANCE: {} | FARE: {}".format(self.distance, self.fare))
        print("DATE: {} | TIME: {}".format(self.date, self.time))
        print("----------------------------")

        self.driver.show()

                
