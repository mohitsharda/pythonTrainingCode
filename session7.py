def printNumber(number):
    print(number)

    if number < 10:
        printNumber(number + 1) #function call itself again and again

printNumber(1)