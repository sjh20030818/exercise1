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


# Define the validate_name function to check for first and last name with alphabets only
def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

# Define the validate_email function to check for the presence of '@'
def validate_email(email):
    return '@' in email

# Define the display_categories function to show the available categories
def display_categories(products):
    for index, category in enumerate(products.keys(), 1):
        print(f"{index}. {category}")

# Define the display_products function to show products in a category
def display(products_list):
    for index, (product, price) in enumerate(products_list, 1):
        print(f"{index}. {product} - ${price:.2f}")

# Define the display_sorted_products function to sort and show products a category
def display_sorted_products(products_list, sort_order):
    if sort_order == 'price':
        sorted_products = sorted(products_list, key=lambda x: x[1])
    else:  # Default to sorting by name
        sorted_products = sorted(products_list, key=lambda x: x[0])
    return sorted_products

# Define the add_to_cart function to add products to the cart
def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

# Define the display_cart function to show the contents of the cart
def display_cart(cart):
    print("Your Cart:")
    for item, quantity in cart:
        print(f"{item} x {quantity}")

# Define the generate_receipt function to print a receipt
def generate_receipt(name, email, cart, total_cost, address):
    print(f"Receipt for {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print("Items Purchased:")
    for item, quantity in cart:
        print(f"{item} x {quantity}")
    print(f"Total Cost: ${total_cost:.2f}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

# Define the main function
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

    # Get and validate's name
    while True:
        name = input("Enter your name (First Last): ")
        if validate_name(name):
            break
        print("Invalid name. Please enter both first and last names using alphabets only.")

    # Get and validate user's email
    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            break
        print("Invalid email. Please enter a valid email address.")

    # Display categories and handle user's choice
    while True:
        display_categories(products)
        choice = input("Enter the number of the category you want to browse, or 0 to finish shopping: ")
        if choice == '0':
            break
        if not choice.isdigit() or not 1 <= int(choice) <= len(products):
            print("Invalid choice. Please enter a valid category number.")
            continue
        category_index = int(choice) - 1
        category_name = list(products.keys())[category_index]
        products_list = products[category_name]

        action_choice = input("Choose an action: 1. Display products 2. Sort products by price 3. Go back: ")
        if action_choice == '1':
            print(f"Products in {category_name}:")
            display_products(products_list)
        elif action_choice == '2':
            print(f"Sorted products in {category_name} by price:")
            sorted_products = display_sorted_products(products_list, 'price')
            display_products(sorted_products

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
