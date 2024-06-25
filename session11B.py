quote1  = "SEARCHING THE CANDLE RATHER THAN CURSING THE DARKNESS \n"
quote2  = "BE EXCEPTIONAL\n"

# file = open("quotes.txt", "w")in w if you write another data it will overright the previous data
file = open("quotes.txt", "a") #here if you write another data the previous data will not erase it will add another data with previous

file.write(quote1)
file.write(quote2)

file.close() # FREE MEMORY RESOURCES ONCE YOU HAVE USED FILES



print("DATA WRITTEN: ")