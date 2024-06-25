from session12 import Customer
from session12A import Dish
from session12B import Order

dishMenu = [Dish(name = "DAL MAKHANI", price = 200, rating = 2),
          Dish(name = "PANEER", price = 400, rating = 3),
          Dish(name = "BURGER", price = 50, rating = 5),
          Dish(name = "NOODLES", price = 100, rating = 2.5),
          Dish(name = "PIZZA", price = 160, rating = 1.5) ]

customer1 = Customer(name = "John", phoneNumber="9191919199", email="john@exmaple.com", Address="kingslanding")
customer2 = Customer(name = "hell", phoneNumber="243555354", email="hell@exmaple.com", Address="winterfell")

# # HARD CODING STATEMENTS
# order1 = Order(oId=1, Dishes=[dishMenu[0], dishMenu[2]], customer=customer1, total=250)
# order2 = Order(oId=2, Dishes=[dishMenu[1], dishMenu[3]], customer=customer1, total=500)

order1 = Order(oId=1)
order1 .linkCustomer(customer1)
order1.linkDishes([dishMenu[0], dishMenu[2]])

order1.show()
