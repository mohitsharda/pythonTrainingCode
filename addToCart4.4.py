#this is a basic code for add to cart using List and Dictionary

cart = []
price = []
quantity = []

shop = {
    "tshirt" : 100,
    "shoes" : 500,
    "perfumes" : 200,
    "watch" : 800,
    "jeans" : 400
}

print("Welcome to shopping platform")
print("*********************")
print("shopping menu:")
print("*********************")
print(shop)
print("*********************")

while True:
    item = input("Enter the item you want to purchase or 0 for exit : ")

    if item == "0":
        break

    qty = int(input("Enter quantity of an item you want to buy : "))
    quantity.append(qty)

    cart.append(item)
    price.append(shop[item]*qty)

print("Item is : ", cart)
print("price is : ", price)
print("total quantity of item is :", quantity)
print("total item in cart is : ", len(cart))
print("Amount toPay : ", sum(price))
