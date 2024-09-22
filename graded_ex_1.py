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
def display_products(products_list):
    for index, (product, price) in enumerate(products_list, 1):
        print(f"{index}. {product} - ${price:.2f}")

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
   (f"Address: {address}")
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

    # Get and validate user's name
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
    display_categories(products)
    while True:
        choice = input("Enter the number of the category you want to browse, or 4 to finish shopping: ")
        if choice == '4':
            break
        if not choice.isdigit() or not 1 <= int(choice) <= len(products):
            print("Invalid choice. Please enter a valid category number.")
            continue
        category_index = int(choice) - 1
        category_name = list(products.keys())[category_index]
        products_list = products[category_name]
        display_products(products_list)

        # Add products to cart
       _choice = input("Enter the number of the product you want to add to the cart, or 0 to go back: ")
        if product_choice == '0':
            continue
        if not product_choice.isdigit() or not 1 <= int(product_choice) <= len(products_list):
            print("Invalid choice. Please enter a valid product number.")
            continue
        product_index = int(product_choice) - 1
        product = products_list[product_index][0]
        quantity = int(input("Enter the quantity: "))
        add_to_cart(cart, product, quantity)

    # Check if the cart is empty
    if not cart:
        print("You have not added any products to your cart.")
    else:
        # Display cart and generate receipt
        display_cart(cart)
        total_cost = sum(price * quantity for _, quantity in cart for product, price in products.values() if product[0] == _[

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
