# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == 'price':
        sorted_products = sorted(products_list, key=lambda x: x[1])
    else:  # Default to sorting by name
        sorted_products = sorted(products_list, key=lambda x: x[0])
    return sorted_products

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, 1):
        print(f"{index}. {product} - ${price:.2f}")

def display_categories(products):
    categories = list(products.keys())
    for index, category in enumerate(categories, 1):
        print(f"{index}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

def display_cart(cart):
    print("Your Cart:")
    for item, quantity in cart:
        print(f"{item} x {quantity}")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Receipt for {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
   ("Items Purchased:")
    for item, quantity in cart:
        print(f"{item} x {quantity}")
    print(f"Total Cost: ${total_cost:.2f}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return '@' in email

def main():
    products = {
        "IT Products": [
            ("Laptop", 1000), ("Smartphone", 600), ("Headphones", 150),
            ("Keyboard", 50), ("Monitor", 300), ("Mouse", 25),
            ("Printer", 120), ("USB Drive", 15)
        ],
        "Electronics": [
            ("Smart TV", 800), ("Bluetooth Speaker", 120), ("Camera", 500),
            ("Smartwatch", 200), ("Home Theater", 700), ("Gaming Console", 450)
        ],
        "Groceries": [
            ("Milk", 2), ("Bread", 1.5), ("Eggs", 3), ("Rice", 10),
            ("Chicken", 12), ("Fruits", 6), ("Vegetables", 5), ("Snacks", 8)
        ]
    }
    cart = []

    while True:
        name = input("Enter your name: ")
        if not validate_name(name):
            print("Invalid name. Please enter both first and last names using alphabets only.")
            continue
        break

    while True:
        email = input("Enter your email: ")
        if not validate_email(email):
            print("Invalid email. Please enter a valid email address.")
            continue
        break

    display_categories(products)
    while True:
        category_choice = int(input("Select a category by number: "))
        selected_category = list(products.keys())[category_choice - 1]
        selected_products = products[selected_category]

        action_choice = input("Choose an action: 1. Display products 2. Sort products by price 3. Go back: ")
        if action_choice == '1':
            print(f"Products in {selected_category}:")
            display_products(selected_products)
        elif action_choice == '2':
            print(f"Sorted products in {selected_category} by price:")
            sorted_products = display_sorted_products(selected_products, 'price')
            display_products(sorted_products)
        elif action_choice == '3':
            continue
        else:
            print("Invalid. Please enter 1, 2, or 3.")
            continue

        product_choice = int(input("Select a product to buy by number: "))
        selected_product = selected_products[product_choice - 1]
        quantity = int(input("Enter quantity: "))
        add_to_cart(cart, selected_product, quantity)

        finish_shopping = input("Do you want to finish shopping? (yes/no): ")
        if finish_shopping.lower() == 'yes':
            break

    address = input("Enter your shipping address: ")

    total_cost = sum(price * quantity for _, quantity in cart for product, price in products.values() if product[0] == _[0])
    generate_receipt(name, email, cart, total_cost, address)

    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
