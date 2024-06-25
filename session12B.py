# 1 Order can have many Dishes
# 1 Order can have 1 customer

class Order:

    def __init__(self,  oId = 0, Dishes = None, customer = None, total = 0): # None will store hashcode of some other object
        self.oId = oId
        self.Dishes = Dishes        
        self.customer = customer
        self.total = total

    
    def show(self):
        print("-----------ORDER-----------")
        print("{} | {} ".format(self.oId, self.total))
        print("---------------------------")

        print("ORDER PLACED BY: ")
        self.customer.show()

        print("-------------ORDER DISHES-----------")
        for dish in self.Dishes:
            dish.show()
        print("-------------------------------------")

    def linkDishes(self, Dishes):
        self.Dishes = Dishes

        for dish in self.Dishes:
            self.total += dish.price

    def linkCustomer(self, customer):
        self.customer = customer