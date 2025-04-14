# Exercise 2 shopping cart program

item = input("what item you like to buy?; ")
price = float(input("What is the price?; "))
quantity = int(input("how many would you like?; "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"you total is {total}")