#multi value container
#tuple cannot be changed once created

#MVC LIST
#Tuple is immutable and list is mutable
freinds = ["Avneet Kaur", "Andrew Tate", "Rehman BHai",111]
print(freinds, type(freinds), id(freinds))

print(freinds[0], type(freinds[0]), id(freinds[0]))
print(freinds[1], type(freinds[1]), id(freinds[1]))

#lets change..
#you will get an error
freinds[0] = "jonny"
print(freinds, type(freinds), id(freinds))

#in list we can change the value but in tuple we cant

