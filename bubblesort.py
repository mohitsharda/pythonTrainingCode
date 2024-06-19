num  = [23,34,23,12]
for i in range(len(num)-1):
    for j in range(i+1, len(num)):

        if (num[j] < num[i]):
            # temp = num[i]
            num[i], num[j] = num[j], num[i]
            # num[j] = temp


print(num)