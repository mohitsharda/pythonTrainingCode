"""
   Code 3 objects
   1. Dish : name, price, rating
   2. Menu : name, numberOfDishes, Dishes
      1. Menu can have many dishes (1 to many)
    3. Restaurant : name, phone, email, address, operatingHours, ratings, menu
       1. Restaurants can have 1 many(1 to 1)

"""
# Class for the dish
class Dish:
    # Parameterised Constructor, with default values of argument passed to it
    def __init__(self, name = "Na", price = 0, rating = 1.5):
        self.name = name  # Copy the contents of name (input to constructor) into self.name
        self.price = price
        self.rating = rating

    def show(self):
        print("-----------------------------------------")
        print("Dish :, {},{},{}".format(self.name, self.price, self.rating))
        print("-----------------------------------------")


# dish1 = Dish()
# print("dish1 :", hex(id(dish1)))


# dish2 = Dish("Dal Makhani", 250, 4.5)
# print("dish2 :", hex(id(dish2)))

# dish3 = Dish("Paneer", 400, 5.0)
# print("dish3 :", hex(id(dish3)))

# dishes = [dish1, dish2, dish3]

# dishes = [
#     Dish(),
#     Dish("Dal Makhani", 250, 4.5),
#     Dish("Paneer", 400, 5.0)
# ]

# print("DISHES ARE : \n")
# for index in range(len(dishes)):
#     dishes[index].show()