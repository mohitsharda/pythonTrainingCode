class FOOD :

    def __init__(self):
        # for restaurant object
        self.nameOfRestaurant = "RISHI VEGETARIAN"
        self.overview = "RESTAURANT OVERVIEW"
        self.order = "ORDER OPTION"
        self.photos = "PHOTOES OF RESTAURANT"
        self.menu = "MENU OF RESTAURANT"
        self.review = "REVIEW OF RESTAURANT"
        self.ratingOfRestaurant = 4

        #for menu object
        self.menuOfdishes = "INFORMATION OF ALL DISHES"
        self.buy = "DISHES THAT YOU WANT TO BUY"
        self.totalItemsInMenu = 20
        self.categoryOfDishes = "All FOOD ITEMS CATEGORY"
        self.vegOrNonVeg = "\U0001F7E2 -> VEG & \U0001F534 -> NON-VEG"
 
        # for dish object
        self.nameOfDish = "DAL MAKHANI"
        self.quantityOfDish = "HALF"
        self.rateOfDish = 150
        self.ratingOfDish = "\u2606 \u2606 \u2606 \u2606"
        self.combo =  "Dal MAKHANI, RAITA, CHAPPATI, SALAD, RICE"

    # for restaurant
    def show(self):
        print("-----------------------------------------")
        print("Resyaurant :, {},{},{},{},{},{},{}".format(self.nameOfRestaurant, self.overview, self.order, self.photos, self.menu,self.review, self.ratingOfRestaurant))
        print("-----------------------------------------")



    # for menu
    # def showMenuInfo(self):
    #     print(self.menuOfdishes)
    #     print(self.buy )
    #     print(self.totalItemsInMenu)
    #     print(self.categoryOfDishes)
    #     print(self.vegOrNonVeg)

    def show(self):
        print("-----------------------------------------")
        print("Resyaurant :, {},{},{},{},{}".format(self.menuOfdishes, self.buy, self.totalItemsInMenu, self.categoryOfDishes, self.vegOrNonVeg))
        print("-----------------------------------------")



    # for dishes
    # def showDishesInfo(self):
    #     print(self.nameOfDish)
    #     print(self.quantityOfDish )
    #     print(self.rateOfDish)
    #     print(self.ratingOfDish)
    #     print(self.combo)

    def show(self):
        print("-----------------------------------------")
        print("Dishes :, {},{},{},{},{}".format(self.nameOfDish, self.quantityOfDish, self.rateOfDish, self.ratingOfDish, self.combo))
        print("-----------------------------------------")


restaurant = FOOD()
print("RESTAURANT INFO: ")
print("----------------------------")
restaurant.show()
print("----------------------------\n")

print("MENU INFO: ")
print("----------------------------")
restaurant.show()
print("----------------------------\n")

print("DISHES INFO: ")
print("----------------------------")
restaurant.show()
print("----------------------------\n")
