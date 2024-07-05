#customer management app

from session15 import Customer
from session15A  import Database
from tabulate import tabulate    # pip install tabulate


def main():
    print("--------------------------------------")
    print("WElCOME TO CUSTOMER MANAGEMENT APP : ")
    print("--------------------------------------")

    db = Database()

    while True:
        print("1. ADD NEW CUSTOMER: ")
        print("2. UPDATE EXISTING CUSTOMER: ")
        print("3. DELETE EXISTING CUSTOMER: ")
        print("4. VIEW CUSTOMER BY PHONE: ")
        print("5. VIEW CUSTOMER BY CID: ")
        print("6. VIEW ALL CUSTOMER: ")
        print("0 : TO QUIT: ")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            customer = Customer()
            customer.addCustomerDetail()
            sql = "insert into customer values(null, '{name}', '{phone}', '{email}', '{age}', '{gender}', '{createdOn}')".format_map(vars(customer))
            db.write(sql)
            print("[CMS APP]", customer.name, "SAVED IN DATABASE :")

        elif choice == 2:
            id = int(input("ENTER CUSTOMER ID TO UPDATE  : "))
            sql = "select * from customer where cId = '{}'".format(id)
            rows = db.read(sql)

            print(rows)
            customer = Customer(cId= rows[0][0], name= rows[0][1], phone= rows[0][2], email= rows[0][3], age= rows[0][4], gender= rows[0][5])

            print("Customer to update: ")
            customer.show()
            customer.updateCustomerDetail()

            sql = "update customer set name = '{name}', phone = '{phone}', email = '{email}', age = '{age}', gender = '{gender}', createdOn = '{creatonOn}' where cid = {cid}".format_map(vars((customer)))
            db.write(sql)

            customer.show()
            
        elif choice == 3:
            cId = int(input("ENTER CUSTOMER ID TO BE DELETED: (YES/NO) "))
            sql = "DELETE FROM CUSTOMER WHERE CID = '{}'".format(cId)

            ask = input("ARE YOU SURE TO DELETE: ")
            if ask == "yes":
                db.write(sql)
                print("[CMS APP]", cId, "DELETED FROM DATABASE:")
            else:
                print("not: ")

            
        elif choice == 4:
            phone = input("ENTER YOUR PHONE-NUMBER: ")
            sql = "select * from customer where phone = '{}'".format(phone)
            rows = db.read(sql)

            columns = ['cId', 'name', 'phone', 'email', 'age', 'gender', 'created_on']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            

        elif choice == 5:
            cid = int(input("ENTER CUSTOMER CID : "))
            sql = "select * from customer where cId = '{}'".format(cid)
            rows = db.read(sql)

            columns = ['cId', 'name', 'phone', 'email', 'age', 'gender', 'created_on']
            print(tabulate(rows, headers=columns, tablefmt="grid"))


        elif choice == 6:
            sql = "select * from customer "
            rows = db.read(sql)

            columns = ['cId', 'name', 'phone', 'email', 'age', 'gender', 'created_on']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            # for row  in rows:
            #     print(row)

        elif choice == 0:
            break

        else:
            print("[CMS APP] INVALID CHOICE: ")


if __name__ == "__main__":
    main()