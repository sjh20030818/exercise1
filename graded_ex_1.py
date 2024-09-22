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


# Products available in the store by category
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

# Function to validate the name
def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

# Function to validate the email
def validate_email(email):
    return '@' in email and '.' in email.split('@')[-1]

# Function to display categories
def display_categories():
    for index, category in enumerate(products.keys(), 1):
        print(f"{index}. {category}")

# Function to display
def display_products(category):
    for index, (product, price) in enumerate(products[category], 1):
        print(f"{index}. {product} - ${price:.2f}")

# Function to add products to the cart
def add_to_cart(cart, product, quantity):
    for item in cart:
        if item[0] == product:
            item[1] += quantity
            return
    cart.append([product, quantity])

# Function to display the cart
def display_cart(cart):
    print("Your Cart:")
    for product, quantity in cart:
        print(f"{product} x {quantity}")

# Function to generate a receipt
def generate_receipt(name, email, cart, address):
    print(f"Receipt for {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print("Items Purchased:")
    total_cost = 0
    for product, quantity in cart:
        price = next(price for cat, pros in products.items() for prod, price in pros if prod == product)
        print(f"{product} x {quantity}")
        total_cost += price * quantity
    print(f"Total Cost: ${total_cost:.2f}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

# Main function
def main():
    cart = []
    name = input("Enter your name (First Last): ")
    while not validate_name(name):
        name = input("Invalid name. Please enter both first and last names using alphabets only: ")
    
    email = input("Enter your email: ")
    while not validate_email(email):
        email = input("Invalid email. Please enter a valid email address: ")
    
    display_categories()
    while True:
        choice = input("Enter the number of the category you want to browse, or 0 to finish shopping: ")
        if choice == '0':
            break
        if not choice.isdigit() or not 1 <= int(choice) <= len(products):
            print("Invalid choice. Please enter a valid category number.")
            continue
        category = list(products.keys())[int(choice) - 1]
        display_products(category)
        
        product_choice = input("Enter the number of the product you want to add to the cart, or 0 to go back: ")
        if product_choice == '0':
            continue
        if not product_choice.isdigit() or not 1 <= int(product_choice) <= len(products[category]):
            print("Invalid choice. Please enter a valid product number.")
            continue
        product = list(products[category])[int(product_choice) - 1][0]
        quantity = input("Enter the quantity: ")
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid quantity. Please enter a positive number.")
            continue
        add_to_cart(cart, product, int(quantity))
    
    if cart:
        address = input("Enter your shipping address: ")
        generate_receipt(name, email, cart, address)
    else:
        print("You have not added any products to your cart.")

if __name__ == "__main__":
   
