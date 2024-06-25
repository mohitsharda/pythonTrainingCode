# num  = [23,34,23,12]
# for i in range(len(num)-1):
#     for j in range(i+1, len(num)):

#         if (num[j] < num[i]):
#             # temp = num[i]
#             num[i], num[j] = num[j], num[i]
#             # num[j] = temp


# print(num)

# Above without function
#  Below with Function

def bubbleSort(data):

    for i in range(0, len(data) - 1):
        print("i is:", i)
        for j in range(i+1, len(data)):
            print(j, end= " ")
            if data[i] > data[j]:
                print("Swapping {} with {}".format(data[i], data[j]))
                data[i],data[j] = data[j],data[i]    
    
    
numbers = [50,10,20,30,40]
print("unsorted data:")
print(numbers)

print("sorted data:")
bubbleSort(numbers)
print(numbers)