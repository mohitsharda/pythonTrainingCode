# Dish -> name, price, rating

class Dish:

    def __init__(self,  name, price, rating):
        self.name = name
        self.price = price        
        self.rating = rating

    
    def show(self):
        print("-----------DISH-----------")
        print("{} | {} | {}".format(self.name, self.price, self.rating))
        print("---------------------------")

def bubbleSort(data):

    for i in range(0, len(data) - 1):
        for j in range(i+1, len(data)):
            if data[i].price > data[j].price:
                data[i],data[j] = data[j],data[i]    
    
   
#LIST OF DISH OBJECT:
# dish1 = Dish(name = "DAL MAKHANI", price = 200, rating = 2)
# dish2 = Dish(name = "PANEER", price = 400, rating = 3)
# dish3 = Dish(name = "BURGER", price = 50, rating = 5)
# dish4 = Dish(name = "NOODLES", price = 100, rating = 2.5)
# dish5 = Dish(name = "PIZZA", price = 160, rating = 1.5)

#dishse = [dish1, dish2, dish3, dish4, dish5]

dishes = [Dish(name = "DAL MAKHANI", price = 200, rating = 2),
          Dish(name = "PANEER", price = 400, rating = 3),
          Dish(name = "BURGER", price = 50, rating = 5),
          Dish(name = "NOODLES", price = 100, rating = 2.5),
          Dish(name = "PIZZA", price = 160, rating = 1.5) ]

# for i in range(len(dishes)):
#     dishes[i].show

# print("DISHES :")
# for dish in dishes:
#     dish.show()

# bubbleSort(dishes)

# print("\nSORTED DISHES :")
# for dish in dishes:
#     dish.show()


