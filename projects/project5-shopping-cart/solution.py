# Project 5 — Mini Shopping Cart
# Author: Seid Mamuti

menu = {
    1: ("Apple",  0.50),
    2: ("Banana", 0.30),
    3: ("Milk",   1.20),
    4: ("Bread",  2.00),
}

cart  = {}   # { item_name: quantity }
total = 0.0

# TODO: display the menu
# print("--- Shop Menu ---")
# for number, (name, price) in menu.items():
#     print(f"{number}. {name:<10} ${price:.2f}")
# print("5. Done")

# TODO: shopping loop
# while True:
#     choice = int(input("\nChoose an item (1-5): "))
#     if choice == 5:
#         break
#     if choice in menu:
#         ...add to cart, update total...
#     else:
#         print("Invalid choice, try again.")

# TODO: print the receipt
# print("\n--- Receipt ---")
# for item, qty in cart.items():
#     ...
# print(f"Total: ${total:.2f}")
# print("Thank you!")

# Project 5 - Mini Shopping Cart
# Author: Seid Mamuti
menu = {
1: ("Apple", 0.50),
2: ("Banana", 0.30),
3: ("Milk", 1.20),
4: ("Bread", 2.00),
}
cart = {}
total = 0.0
while True:
print("\n--- Shop Menu ---")
print("1. Apple $0.50")
print("2. Banana $0.30")
print("3. Milk $1.20")
print("4. Bread $2.00")
print("5. Done")
choice = int(input("Choose an item (1-5): "))
if choice == 5:
break
elif choice in menu:
item_name, price = menu[choice]
if item_name in cart:
cart[item_name] += 1
else:
cart[item_name] = 1
total += price
print(f"Added {item_name}. Total: ${total:.2f}")
else:
print("Invalid choice. Please choose a number from 1 to 5.")
print("\n--- Receipt ---")
for item_name, quantity in cart.items():
price = 0.0
for item in menu.values():
if item[0] == item_name:
price = item[1]
break
print(f"{item_name:<8} x{quantity} ${price * quantity:.2f}")
print("---------------------")
print(f"Total: ${total:.2f}")
print("Thank you!")
