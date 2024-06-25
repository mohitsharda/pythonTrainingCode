file = open("CUSTOMERS.csv", "r") # r ->> read
# data  = file.read()

lines = file.readlines()

print("FILE DATA: ")
print(lines)

for i in range(len(lines)):
    print(lines[i])