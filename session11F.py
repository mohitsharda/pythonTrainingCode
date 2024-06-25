from session10C import Customer
from session10B import Driver
from session10A import Vehicle
from session11E import Ride

#driver application
driver = Driver()
driver.addDriverDetails()


#customer application
customer = Customer()
customer.addCustomerDetails()

#server
ride = Ride()
ride.addRideDetails()
ride.linkCustomer(customer)
ride.linkDriver(driver)

print("RIDE BOOKED...")
ride.show()
