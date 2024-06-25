name = input("ENTER CUSTOMER NAME: ")
phone = input("ENTER CUSTOMER PHONE: ")
email = input("ENTER CUSTOMER EMAIL: ")

customerDetail = "{}, {}, {}\n".format(name, phone, email)

file = open("CUSTOMERS.csv", "a")
file.write(customerDetail)

print("CUSTOMER DATA SAVED...")\

file.close()
