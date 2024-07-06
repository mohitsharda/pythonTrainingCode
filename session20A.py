# properties
"""
   Indexing
   negative indexing
   slicing
   concatenation
   multiplicity
   membership testing
"""

quote = "search the candle rather than searching the darkness"
print(id(quote))

print(quote[1])
print(quote[-8:])

quote = quote + "\n" + "Be Exceptional\n"
print(quote)
print(id(quote))

data = quote * 3
print("-----------------------------")
print(data)
print("-----------------------------")

print("the" in quote)

# email = input("ENTER THE EMAIL:")

# if "@" in email and "." in email:

#     print("email is wellformed:", email)

# else:
#     print("not wellformed:")

contacts = ["mohit", "shivam", "anshit"]
search = input("ENTER SEACRH KEYWORD: ")

for contact in contacts:
    if search  in contact:
        print(contact)