
def getMax(data, length):
    #data , length : getMax frames
    if length == 1:
        return data[0]
    else:
        previous = getMax(data, length-1)
        current = data[length-1]
        
        if previous > current:
            return previous
        else:
            return current

number = [1, 5, 3 ]

result = getMax(number, len(number))
print("Max value is: ", result)



# below is the  code without using recursion

# max = number[0]

# for i in range(1, len(number)):
#     if number[i] > max:
#         max = number[i]

# print("max is:", max)


