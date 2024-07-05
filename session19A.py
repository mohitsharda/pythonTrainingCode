# Explore Set
# Unique

johnFollower = {"fiona", "johny", "joe", "kia"}
print(johnFollower, id(johnFollower), type(johnFollower))

numbers = list(range(10,101,10))
numbers1 = set(numbers)
print(numbers)
print(numbers1)

numbers1.add(101)
numbers1.add(22222)

print(numbers1)
# numbers1.pop()
# print(numbers1)

numbers1.remove(22222)
numbers1.remove(101)   # remove also available for set
numbers1.discard(100)
print(numbers1)

johnFollower = {"fiona", "johny", "joe", "kia"}
siaFollower = {"fiona", "helo", "kia"}
kiaFollower = {"fiona", "yo"}





A = {1,2,3,4,5}
B = {6,7,8,9,10}

# C = A + B
# print(C)

D = A - B
print("D",D)

E = A ^ B
print("E",E)

F = A | B
print("F",F)

A.clear()
print(A)

#create an empty set

mySet = set()
mylist = []
mydict = {}