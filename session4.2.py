#Dictionary 
#the most powerfull and most important and mostly used 

friends = {0: "mohit", 1: "anshit", 2:"prashant", 3:"saurav"}
print(friends, type(friends), id(friends))

print(friends[0])

zomato = {
    "nikkuDabbhaPMCode" : {"zomato100", "zomato200", "welcome100"},
    "rishiPMCode" : {"zomato50", "zomato150", "welcome100"}

}

print(zomato["nikkuDabbhaPMCode"])
print(zomato["rishiPMCode"])

mutualPromoCode = zomato["nikkuDabbhaPMCode"] & zomato["rishiPMCode"]

print(mutualPromoCode)

#homeWork draw a ram diagram of dictionary