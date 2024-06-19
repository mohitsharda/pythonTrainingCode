"""
   Code 3 objects
   1. Dish : name, price, rating
   2. Menu : name, numberOfDishes, Dishes
      1. Menu can have many dishes (1 to many)
    3. Restaurant : name, phone, email, address, operatingHours, ratings, menu
       1. Restaurants can have 1 many(1 to 1)

"""
from session8 import Dish

class Menu:

    def __init__(self, name = "Na", numberOfDishes = 0, menuDishes = []):
        self.name = name  # Copy the contents of name (input to constructor) into self.name
        self.numberOfDishes = numberOfDishes
        self.menuDishes = menuDishes

    def show(self):
        print("-----------------------------------------")
        print("Menu : {} | {}".format(self.name, self.numberOfDishes))
        print("-----------------------------------------")

        print("DISHES ARE: ")
        for index in range(len(self.menuDishes)):
            self.menuDishes[index].show()


# dishes = [
#     Dish(),
#     Dish("Dal Makhani", 250, 4.5),
#     Dish("Paneer", 400, 5.0)
# ]


# menu = Menu(
#     name = "Indian Veggie Delight",
#     numberOfDishes = len(dishes),
#     menuDishes = dishes
# )

# menu.show()