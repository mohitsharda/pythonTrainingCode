class LibraryObject:
    
    # DeFault constructor in python
    # self is reference variable, which will hold the hascode of any current object
    def __init__(self):
        print("self -", self)
        self.purchaseGames = "All Purchased Games"
        self.gamesName = "GTA 5, ASSASSIN's CREED.. etc"
        self.play = "Play Button"
        self.numberOfGames = 200
        self.uninstall = "uninstall Button"
        self.install  = "install Button"

     # PARAMETERISED CONSTRUCTOR
    # def __init__(self, purchaseGames, gamesName, play, numberOfGames, uninstall, install):
    #     print("self -", self)
    #     self.purchaseGames = purchaseGames
    #     self.gamesName = gamesName
    #     self.play = play
    #     self.numberOfGames = numberOfGames
    #     self.uninstall = uninstall
    #     self.install  = install

    # def show(self):
    #     print("info")
    #     print(self.gamesName)

game1 = LibraryObject()
print("game1: ", game1)
print("Library Data - ")
print(vars(game1))
print("----------------------------------")
# game1.show()


game2 = LibraryObject()
print("game1: ", game2)
print("Library Data - ")
print(vars(game2))
print("----------------------------------")

# h.w -> (restaurant , menu and dish ) code this three objects