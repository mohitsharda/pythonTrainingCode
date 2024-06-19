"""
   Code 3 objects
   1. Dish : name, price, rating
   2. Menu : name, numberOfDishes, Dishes
      1. Menu can have many dishes (1 to many)
    3. Restaurant : name, phone, email, address, operatingHours, ratings, menu
       1. Restaurants can have 1 many(1 to 1)

"""

from session8 import Dish
from session9 import Menu

class Restaurant:

    def __init__(self, name = "NA", phone = "NA", email = "NA", address = "NA", operatingHours = "10:00 - 23:00", rating = 2.5, menu = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.operatingHours = operatingHours
        self.rating = rating
        self.menu = menu
    
    def show(self):
        print("RESTAURANT : ")
        print("----------------------------------------")
        print("Restaurant :, {} | {} | {}".format(self.name, self.phone, self.email))
        print("Address :, {} | {}".format(self.address, self.operatingHours, self.rating))
        print("----------------------------------------")

        self.menu.show()


# restaurant = Restaurant(name = "Ludhiana Veggie Delight",
#                         phone = "7309292999",
#                         email="ludhiana@gmail.com",
#                         address="krishna nagar", 
#                         rating=2.5,
#                         menu=Menu(
#                             name="Indian Veggie Delight", 
#                             numberOfDishes=3, 
#                             menuDishes=[
#                                         Dish(), 
#                                         Dish("Dal Makhani", 250, 4.5),
#                                         Dish(name="Paneer Masala", price=350, rating=4.5)
#                                     ])
#                         )
# restaurant.show()

Restaurant(name="Ludhiana Veggie Delight",
                        phone="+91 99999 11111",
                        email="veggies@abc.com",
                        address="Krishna Nagar", 
                        rating=4.5,
                        menu=Menu(
                            name="Indian Veggie Delight", 
                            numberOfDishes=3, 
                            menuDishes=[
                                        Dish(), 
                                        Dish("Dal Makhani", 250, 4.5),
                                        Dish(name="Paneer Masala", price=350, rating=4.5)
                                    ])
                        ).show()