"""

    ZOMATO : 20% off :
    :min value : 300

    BINGO 50% off
    min value : 500
    max discount: 100

INDENTATION -> PEP = python enhancement proposal

if and else ->they are meant to create workflows
"""

promoCode = input("ENTER PROMOCODE:")
amount = float(input("ENTER AMOUNT: "))


if promoCode == "ZOMATO":
    print("ZOMATO can be appllied...")

    if amount > 300:
        discount = 0.20 * amount

        print("ZOMATO applied successfull. you got discount of : ", discount)
        print("you will pay: \u20b9", amount-discount)
    
    else:
        print("Amount is less.. Please add items worth ", (300-amount), "more")



elif promoCode == "BINGO":
        if amount > 500:
            discount = 0.50 * amount

            print("BINGO applied successfull. you got discount of : ", discount)
            print("you will pay: \u20b9..", amount-discount) #\u20b9 is a unicode
    
        else:
            print("Amount is less.. Please add items worth ", (500-amount), "more")
   

        print("BINGO can be applied...")


else:
    print("INVALID PROMOCODE")

# H.W ->> write ur name is hindi/punjabi or whatever the language you are interested using unicode
