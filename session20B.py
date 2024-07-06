# STRINGS ARE IMMUTABLE -> thy cannot be changed

quote = "be exceptional"
print("HASHCODE OF QUOTE IS:", id(quote))

s1 = quote.upper()

print("1: quote is: ", quote)
print("HASHCODE OF QUOTE IS:", id(quote))


s2 = quote.lower()
print("2: quote is: ", quote)
print("HASHCODE OF QUOTE IS:", id(quote))

print("s1 is :", s1)
print("s1 is :", s1)

s3 = quote.capitalize()
print("s3 is: ", s3)


s4 = quote.title()
print("s4 is: ", s4)

quote = "Be Exceptional"
s5 = quote.swapcase()
print("s5 is: ", s5)

