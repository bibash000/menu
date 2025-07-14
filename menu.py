# Gorkha Kitchen Restaurant Menu Program

menu = {
    1: {"name": "Momo (Buff)", "price": 150},
    2: {"name": "Momo (Chicken)", "price": 180},
    3: {"name": "Chowmein (Veg)", "price": 120},
    4: {"name": "Chowmein (Chicken)", "price": 160},
    5: {"name": "Fried Rice (Veg)", "price": 130},
    6: {"name": "Thakali Set (Veg)", "price": 200},
    7: {"name": "Thakali Set (Chicken)", "price": 250},
    8: {"name": "Sekuwa (Buff)", "price": 220},
    9: {"name": "Cold Drink", "price": 60},
    10: {"name": "Milk Tea", "price": 30}
}

order = {}

def display_menu():
    print("\n🍽️ Welcome to Gorkha Kitchen 🍽️")
    print("--------- MENU ---------")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - Rs. {item['price']}")
    print("-------------------------")

def take_order():
    while True:
        try:
            choice = int(input("Enter item number to order (0 to finish): "))
            if choice == 0:
                break
            elif choice in menu:
                quantity = int(input(f"Enter quantity for {menu[choice]['name']}: "))
                if choice in order:
                    order[choice]['quantity'] += quantity
                else:
                    order[choice] = {"name": menu[choice]["name"], "price": menu[choice]["price"], "quantity": quantity}
            else:
                print("❌ Invalid item number.")
        except ValueError:
            print("⚠️ Please enter valid numbers.")

def print_bill():
    print("\n🧾 Order Summary:")
    print("-----------------------------")
    total = 0
    for item in order.values():
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"{item['name']} x {item['quantity']} = Rs. {item_total}")
    print("-----------------------------")
    print(f"Total Amount: Rs. {total}")
    print("🙏 Thank you for visiting Gorkha Kitchen!")

# Run the restaurant ordering system
display_menu()
take_order()
print_bill()
#This is AI Generated!