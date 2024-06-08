numbers = {10, 20, 11, 22, 55, 57}
myFriends = {"avneetKaur", "ronaldo", "carryminati", "zayn"}
otherFriends = {"prashant", "ravi", "saurav", "anshit"}

print(numbers, type(numbers), id(numbers))
print(myFriends, type(myFriends), id(myFriends))
print(otherFriends, type(otherFriends), id(otherFriends))

mutualFriends = myFriends & otherFriends

print(mutualFriends)

#Set doesnt support indexing it works on hashing hence we cannot get the data from the set by using indexing