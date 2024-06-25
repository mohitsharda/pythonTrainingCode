
from session11 import Customer

print("----------------------------------------")

print("WELCOME TO CUSTOMER MANAGEMEMT SYSTEM")

print("----------------------------------------")

while True:  
    print("1 : ADD CUSTOMER : ")
    print("2 : VIEW CUSTOMER : ")
    print("3 : QUIT : ")

    choice = int(input("ENTER YOUR CHOICE : "))
    print("YOU SELECTED : ", choice)
    
    if choice == 1:
        file = open("customer.csv", "a")
        customer = Customer()
        customer.addCustomerDetails()
        customer.show()

        data = customer.toCsv()
        file.write(data)
        print("DATA WRITTEN :", data)
      
    elif choice == 2:
        file = open("customer.csv", "r")
        lines = file.readlines()

        for line in lines:
            print(line)

    elif choice == 0:
        print("----------------------------------------")
        print("THANKYOU FOR USING CUSTOMER MANAGEMENT SYSTEM")
        print("----------------------------------------")
        file.close()
        break

