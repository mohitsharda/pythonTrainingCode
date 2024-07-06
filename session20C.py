passWord = " hello "
print(passWord, len(passWord))

p1 = passWord.strip()
print(p1, len(p1))

data = "00000045340"
print(data.strip("0"))
print(data)

amount = 35.93000
newAmount = float(str(amount).strip("0"))
print(newAmount, type(newAmount))


quote = "SEARCH THE CANDEL RATHER THAN CUSRING THE DARKNESS: "
quote.replace("the", "k")
new = quote.replace("THE", "k")
print(quote)
print(new)

message = "no internet connection:"
print(message)
print(message.center(50))
print(message.ljust(50))
print(message.rjust(50))


amount = 545
data = str(amount).zfill(8)
print("data is:", data)

quote = "SEARCH THE CANDEL RATHER THAN CUSRING THE DARKNESS: "
idx1 = quote.find("THE")
idx2 = quote.find("DARK")
print(idx1)
print(idx2)

print(quote[idx1:idx1+4])
print(quote[idx2:])

idx3 = quote.rfind("THE")
print(idx3)
print(quote[idx3:])
