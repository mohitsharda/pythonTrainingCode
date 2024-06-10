#promocode is ZOMATO
#Condition1 : you can apply  more than 249
#Condition1 : 50% off upto 150

amount = float(input("enter amount: "))
promoCode = input("enter promoCode: ")

if promoCode == "ZOMATO" :
    print("promoCode exists:")

    if amount > 249 :
        print("promoCode ZOMATO applied...")

        discount = 0.50 * amount

        if discount >= 150:
            discount = 150
            
        amount -= discount
        print("discount : ", discount)
        print("please pay : ", amount)

    else :
        print("AMOUNT IS LOW...")

else:
    print("promoCode Invalid :")

    