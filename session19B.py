"""
myTuple = ()
myTuple = tuple()

myList = []
myList = list[]

mySet = set()

myDict = {}
myDict = dict()

"""

# Explore dictonary / map / json


myData = {
    101 : "john",
    102 : "johnny",
    103 : "iaa",
    104 : "anaa",
    105 : "assmin",
    106 : "anianials",
}

print("my data: ", myData)

print(len(myData))
print(min(myData))
print(max(myData))
print(sum(myData))

print(myData[106])
print(myData.get(106))
myData.pop(104)

# del myData(104)
myData[105] = "jass"
print(myData)

# myData = {
#     "jo" : "john",
#     "joh" : "johnny",
#     "mi" : "iaa",
#     "la" : "anaa",
#     "ja" : "assmin",
#     "da" : "anianials",
# }
# print(len(myData))
# print(min(myData))
# print(max(myData))
# print(sum(myData)) works only for int key

attendance = ["june", "july", "july", "august"]

collageAttendance = {}.fromkeys(attendance, 100)
collageAttendance["august"] = 70
print(collageAttendance)

items = list(myData.items())
values =  list(myData.values())

print(items)
print(values)

for items in myData.items():
    print(items)

    
for items in myData.values():
    print(items)