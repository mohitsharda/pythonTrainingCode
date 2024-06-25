"""
    1. Execute Some SQL commands

       Object Relational Mapping (ORM)       

       # 1. list database
       show databases; 

       # 2.create database:
       create Database project;

       # 3.Select the database in which you wish to create your table
       use project;

        create table Customer( 
            cId int primary key auto_increment,
            name varchar(256), 
            phone varchar(50), 
            email varchar(256), 
            age int, 
            gender varchar(10)
       );

       # 4.check if table is created in database
       show tables;

       # 5.check the table structure
       describer customer;

       # 6.create customer in table
       insert into customer(null, 'john'........)

       creat table Address( 
            cId int primary key auto_increment,
            houseNo varchar(256), 
            addreseLine1 varchar(50), 
            city varchar(256), 
            state varchar(256),
            zipCode int, 
            landMark varchar(10)
       );

           2. Work With Virtual Env
    3. Installation of Driver
    4. SQL Connection  with python

    Customer : name, phone, email, age, gender etc
    Address : houseNo, addreseLine1, city, state, zipCode, landMark

    PlayStore : forYou, topCharts, kids, premium, games, apps, offers, books, wallet

       create table Playstore( 
            cId int primary key auto_increment,
            forYou varchar(256), 
            topCharts varchar(50), 
            kids varchar(256), 
            premium varchar(256),
            games varchar(256), 
            apps varchar(256),
            offers varchar(256),
            books varchar(256),
            wallet float
       );

        # 6. insert into playstore values(null, "Recommeded", "trending", "kids",
                        "premium", "games ", "apps", "available",
                        "books", 120000.22);

        # 7. insert into playstore values(null, "Recommeded Items", "trending items", "items for kids",
                            "premium items", "games option", "apps option", "available offers",
                          "books option", 120000.22);

        # 8. fetch data from customer

        select * from customer;
        select * from customer where email = "....";
        select * from customer where cid = "2";

        # 9.update operation
        update customer set name = "johnny", email = "john@example.com" where cid = 1;

        # 10. delete customer
        delete customer where cid = 1;

"""

class Customer:

    def __init__(self, name, phone, email, age, gender):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender

    def show(self):
        pass


class Address:

    def __init__(self, houseNo, addreseLine1, city, state, zipCode, landMark):
        self.houseNo = houseNo
        self.addreseLine1 = addreseLine1
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.landMark = landMark


class PlayStore :

    def __init__(self, forYou = "", topCharts = "", kids = "", premium = "", games = "", apps = "", offers = "", books= "", wallet = 00.0):
        self.forYou = forYou
        self.topCharts = topCharts
        self.kids = kids
        self.premium = premium
        self.games = games
        self.apps = apps
        self.offers = offers
        self.books = books
        self.wallet = wallet

    def addPlaystoreDetail(self):
        self.forYou = input("ENTER FORYOU : ")
        self.topCharts = input("ENTER topCharts : ")
        self.kids = input("ENTER kids : ")
        self.premium = input("ENTER premium : ")
        self.games = input("ENTER games : ")
        self.apps = input("ENTER apps : ")
        self.offers = input("ENTER offers : ")
        self.books = input("ENTER books : ")
        self.wallet = input("ENTER wallet : ")


playstore = PlayStore(forYou="Recommeded Items", topCharts="trending items", kids="items for kids",
                      premium="premium items", games="games option", apps="apps option", offers="available offers",
                      books="books option", wallet=120000.22)