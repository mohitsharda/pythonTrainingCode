number = list(range(10,101,10))

reverse = []

data = [10, 20, 30, 40, 50]

# for i in range(len(data)-1, -1, -1):
#     reverse.append(data[i])

# print(reverse)

idx = data.index(30)
print("idx is: ", idx)

result = data.count(30)
print("result is:", result)

c = 0
for i in range(len(data)):
    if data[i] == 30:
        c += 1

print("c is :", c)

names = ["mohit", "anshit", "shivam", "chinar"]

data.sort()
print(data)

names.sort()
print(names)

print(min(names), max(names))


names.remove("chinar")
data.remove(30)

print(data)
print(names)

num = [10,20,30,40,50]
num.pop()
num.pop(0)
num.clear()

print(num)

num = [10,20,30,40,50]
num.append(99)
num.insert(2, 44)
num.insert(-1, 76)

print(num)

num1 = tuple(range(10,101,10))
print("tuple :",num1)

idx = num1.index(30)
print("idx is: ", idx)

result = num1.count(30)
print("result is:", result)

num1.pop()
num1.pop(0)
num1.clear()

print("pop, pop, clear: ", num1)

num1.append(99)
num1.insert(2, 44)
num1.insert(-1, 76)

print("append, insert, insert: ", num1)
