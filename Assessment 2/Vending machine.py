import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_items(items, category):
    print(f"{category.capitalize()}:")
    for item in items:
        print(f"Code: {item['Code']}\tName: {item['Name']}\t\tPrice: ${item['Price']}")

def suggest_shoes(selected_shoe_code, shoe_list):
    print("Suggested Shoes:")
    for shoe in shoe_list:
        print(f"Code: {shoe['Code']}\tName: {shoe['Name']}\t\tPrice: ${shoe['Price']}")

cart = []
total_price = 0

# H&M Shoes
HMshoes = [
    {'Code': '1A', 'Name': 'Running Shoes', 'Price': 60},
    {'Code': '1B', 'Name': 'Casual Sneakers', 'Price': 70},
    {'Code': '1C', 'Name': 'Formal Shoes', 'Price': 80}
]

# UNIQLO Shoes
UNIQLOshoes = [
    {'Code': '2A', 'Name': 'Slip-Ons', 'Price': 50},
    {'Code': '2B', 'Name': 'Loafers', 'Price': 55},
    {'Code': '2C', 'Name': 'Sandals', 'Price': 45}
]

# ZARA Shoes
ZARAshoes = [
    {'Code': '3A', 'Name': 'Boots', 'Price': 90},
    {'Code': '3B', 'Name': 'Oxfords', 'Price': 100},
    {'Code': '3C', 'Name': 'Derby Shoes', 'Price': 110}
]

# Start
money = int(input('Insert Money any amount to start the vending machine: '))
print('Current Balance:', money, '$')
print('Please Select A Brand Code:')
brand = {
    '1A': 'H&M',  
    '1B': 'Uniqlo', 
    '1C': 'Zara'
}

print('___________')
for key, value in brand.items():
    print(f'| Code: {key}\tBrand: {value}\t\t|')
print('***********')
brand1 = input('Select Brand Code: ')

while brand1 not in brand:
    print('Invalid Brand Code')
    brand1 = input("Please enter valid brand code or [Q] to quit:")
    if brand1.upper() == 'Q':
        print("Thank you, have a great day.")
        print(f"Please get your remaining balance of {money}$ from the 'change box!'")
        break

if brand1 in brand:
    clear_screen()
    print('You have selected:', brand[brand1])

    if brand1 == '1A':
        print('Shoes')
        display_items(HMshoes, 'Shoes')
    elif brand1 == '1B':
        print('Shoes')
        display_items(UNIQLOshoes, 'Shoes')
    elif brand1 == '1C':
        print('Shoes')
        display_items(ZARAshoes, 'Shoes')

    # CART
    while True:
        tempcart = input("Enter Shoe code (or 'Q' to finish): ")
        if tempcart.upper() == 'Q':
            break

        item_found = False

        for item in HMshoes + UNIQLOshoes + ZARAshoes:
            if tempcart == item['Code']:
                cart.append(item)
                total_price += item['Price']
                print(f"Item {tempcart} added to the cart.")
                item_found = True
                break

        if not item_found:
            print("Invalid item code. Please enter a valid code.")

    # Receipt generation
    print("\nFinal Shopping Cart:")
    for item in cart:
        print(f"Code: {item['Code']}, Name: {item['Name']}, Price: ${item['Price']}")

    print(f"Total Price: ${total_price}")

    # Handling payment
    while True:
        try:
            payment = int(input("We added your initial money to your funds. Enter the amount paid: $"))
            if payment + money >= total_price:
                break
            else:
                print("Still not enough but we added your input to your funds")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    money1 = payment + money
    change = money1 - total_price
    print(f"Change: ${change}")

    # Suggestions for shoes based on selected brand
    if brand1 == '1A':
        suggest_shoes(cart[-1]['Code'], HMshoes)
    elif brand1 == '1B':
        suggest_shoes(cart[-1]['Code'], UNIQLOshoes)
    elif brand1 == '1C':
        suggest_shoes(cart[-1]['Code'], ZARAshoes)
