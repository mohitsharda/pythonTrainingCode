def add(num1, num2, num3):
    result = num1 + num2 + num3

    print("result is: {}".format(result))

# add(10,20,30)
add(num1 = 10, num2 = 20, num3 = 30)


# default argument and inputs
def squar(num = 5):
    result = num * num
    print("result is: {}".format(result))


squar()
squar(3)
squar(num = 9)


# def subtract(num1 = 10, num2): # error
def subtract(num1, num2 = 20):
    result = num1 - num2 
    print("result is: {}".format(result))


subtract(10)
subtract(num1 = 20)