promoCode = "zomato100"
print(promoCode, type(promoCode), id(promoCode))

#reference copy statment 
promoCode2 = promoCode

print(promoCode2, type(promoCode2), id(promoCode2))

del promoCode

print(promoCode2, type(promoCode2), id(promoCode2))
