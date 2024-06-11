productPrices = [1200, 400, 200, 210, 2144, 700]
salaries = [100000, 230000, 211400, 234000, 2300]
teamPoints = [12,3,4,5,1]


# goal find max number out of these three
 
def findMax(data):
    max = data[0]

    for i in range(1, len(data)):
        if data[i] > max:
            max = data[i]

    print("max is :", max)

findMax(productPrices)
findMax(salaries)
findMax(teamPoints)
