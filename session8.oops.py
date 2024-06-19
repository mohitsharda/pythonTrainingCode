"""
Principal of OOPS:
1. Think of an object

LibraryObject: purchasegames , gamesName, play ,numberOfGames , unistall , install

"""

# 2. Create class of object 
# Below class represent the object. It is description of object

class LibraryObject:
    pass

# 3. create the real object from class in memory
# Below is object construction statement

game1 = LibraryObject()

game2 = LibraryObject()

#COPY REFERENCE VARIABLE
game3 = game1


# game 1 is an reference variable, libraryObjec() = represent the object construction
# print(game1)
# print(id(game1))
# print(hex(id(game1)))

# operation on object
# 1. write operation
game1.purchaseGames = "All Purchased Games"
game1.gamesName = "GTA 5, ASSASSIN's CREED.. etc"
game1.play = "Play Button"
game1.numberOfGames = 200
game1.uninstall = "uninstall Button"
game1.install  = "install Button"

game2.purchaseGames = "All Purchased Games"
game2.gamesName = "RED DEAD REDEMPTION 2, ASSASSIN's CREED.. etc"
game2.play = "Play Button"
game2.numberOfGames = 200
game2.uninstall = "uninstall Button"
game2.insta = "install Button"
game2.grid = 50

# 2. update operation
game1.numberOfGames = 90

# 3. Read operation
print("Library Information:")
print(vars(game1))
print("All games - ", game1.gamesName)
print("-----------------------------------")


print("Library Information:")
print(vars(game2))
print("All games - ", game2.gamesName)
print("-----------------------------------")


#4. delete operation
del game1.purchaseGames
print("AFTER DELETING PRUCHASE GAME:")
print(vars(game1))


del game1

print("Library Information:")
print(vars(game3))
print("All games - ", game2.gamesName)
print("---------------END-----------------")
