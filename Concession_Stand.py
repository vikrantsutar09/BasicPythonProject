
menu = {"Pizza": 99,
        "Ice cream": 49,
        "Water": 10,
        "Soda": 20,
        "Tea": 15,
        "Coffee": 30
}

cart = []
total = 0

print("--------MENU-------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")
print("--------MENU-------")

while True:
    food = input("Select an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------Your Order-------")
for food in cart:
    total += menu.get(food)
    print(f"Your order is : {food}")

print()
print(f"Total is : ${total:.2f}")