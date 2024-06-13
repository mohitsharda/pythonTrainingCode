def square(num):
    print(" 1. number is:", num, id(num))
    num *= num # num = num * num
    print(" 2. num is :", num, id(num))

# proof function exists in memory
# print("square is:", square)

number = 10
print("A. number is :", number,  id(number))
square(number)
print("B. number is :", number, id(number))
