"""
   Multivalue Container

   Sequences:
      Tuple
      List
      String

    Properties
    1. Indexing
    2. Negative Indexing
    3. Slicing 
    4. Concatenation
    5. Multiplicity
    6. Membereship Testing

"""

# 1D List 
# Indexing 
#         0   1   2
#         -3  -2  -1


myData = [10, 20, 30]

# 2D List (List of Lists)

numbers = [
         [10, 20,  30], #0  -3
         [30, 40, 50],  #1  -2
         [60, 70, 80]  #2  -1
]

largeNumbers = [
        [
            [10, 20,  30], #0  -3
            [30, 40, 50],  #1  -2       0 -2
            [60, 70, 80]  #2  -1
        ],
        [
            [100, 200,  300], #0  -3
            [300, 400, 500],  #1  -2    1 -1
            [600, 700, 800]  #2  -1
        ],
]

print(myData[0])
print(myData[-1])
print(len(myData))

print(numbers[0])
print(numbers[-1])
print(len(numbers))

print(largeNumbers[0])
print(largeNumbers[-1])
print(len(largeNumbers))

print(largeNumbers[1][0][0])
print(largeNumbers[1][-3][-3])

name = "John's Cafe"
name = 'John\'s Cafe'
name = """Johns Cafe
Welcome to CaFe
Todays Menu:
coffee
Burger 
Cookie"""


print(name)
print(name[0])
print(name[-1])
print(name[-2])

#3. Slicing 
data = list(range(10, 101, 10))
print("data is: ")
print(data)  

print("data[0:3]", data[0:3])
print("data[3:7]", data[3:7])  #3 inclusive and less than 7
print("data[5:]", data[5:])

print("data[:-5]", data[:-5])
print("data[-5:-2]", data[-5:-2])

email = "john@example.com"
print("email[-1, -4] : ", email[-4:])
print("email[-1, -4] : ", email[12:])

# Concatenation

data1 = [10,20,30]
data2 = [40,50,60]

data3 = data1 + data2
print(data3)

# 5. Multiplicity
data4 = data1 * 2
print(data4)

prices = [100,200,300,400,500]
prices1 = prices * 2
print(prices1)

# 6. Membership Testing
print(10 in prices) #False
print(10 not in prices)   #True

quote = "search the candle rather than searching the dark"
print(quote[6])


student = {
    "rollNo": 1,
    "name": "John",
    "age": 20,
    "gender" : "male"
}

print("student[rollno]: ", student["rollNo"])

#Membership testing workss with dictionary
print(1 in student)
print("name" in student)

