#Condition1 : you can apply promocode if and only if min amount is greater than 499

promoCode = "GET200"
amount = float(input("Enter your amount : "))

minAmount = 500

if amount > minAmount :
    print("you can apply promoCode :", promoCode)
    amount -= 200
    print("promoCode applied successfully. please pay:", amount)
else :
    print("you cannot apply the promoCode :", promoCode)
    print("Add items worth", (minAmount - amount), "more..")
