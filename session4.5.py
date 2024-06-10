#Operators
#Arithmetic Operators
# +,-,*,**,/,//,%

productPrice = 200
gstTax = 0.18

priceToPay = productPrice + gstTax*productPrice

print(priceToPay, id(priceToPay), type(priceToPay))

number = 10
#result = number / 3
result = number // 3 #it gives integral divison

print("result is: ", result)

base = 2
#result = base * 2
result = base ** 2 #it gives base to the power

print("result is : ", result)

#remainder operator
bucketSize = 7
hashCode = 120 % bucketSize

print("hasshcode of 120 is : ", hashCode)

#Assignment operator
# =, +=, -=, *=, **=,/=,//= %=

#A refrence variable age , will be created in stack
#A container 20 will be  created in heap
# hashcode of 20 will be stored in age

#hence , age is a reference variable :)
age = 20

#uppdate operation
# age = age + 10
age += 10 #shorthand operator add and assign

print("age is : ", age)

age %= 3 # age = age % 3
age -= 1

print("age is: ", age)

#increment and decrement 
qty = 1
qty += 1 
qty -= 1
qty += 5
qty -= 1
qty **= 2

print("quantity is : ", qty)