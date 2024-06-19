def add(num1, num2):
    result = num1 + num2

    print("result is : {}".format(result))

print(hex(id(add)))
print("add is :", add) # add is a function and u will see the hashcode of function
add(10,20)

#reference copy operation
hello = add

hello(11,22)

# if u redefine the same function the previous function will be remoove from the memory 
# new definition will exist
def add(num1, num2, num3):
    result = num1 + num2 + num3 + 10

    print("result is:", result)

print(hex(id(add)))
print("add is :", add)

add(10, 20, 30)

