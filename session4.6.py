#conditional operator
# ==, !=, >, <, >=, <=

cabFare = 500
#eWallet = 200
eWallet = 500

result = eWallet >= cabFare

print("can i book the cab :", result)
print((type(result)))

#logical operator
#and , or


email = input("Enter email: ")
passWord = input("Enter passWord: ")

print("if login success : ")
result = (email == "mohit@gmail.com") and (passWord == "mohit123")

print(result)

otp = 1234
userOtp = int(input("enter opt receive: "))
print("is otp correct ?? ", (otp == userOtp))

# Membership Testing
# is, is not

a = 10
b = 10
print(a == b)
print(a is b)
print(a is not b)

# homeWork : find difference between  == and is

# homeWork find 5 apptitude problem and solve them using operator
