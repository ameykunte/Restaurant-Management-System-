import pymysql

# Connect to the MySQL database
db = pymysql.connect(host='localhost',
                     user='your_username',
                     password='your_password',
                     database='restaurant')

# Create a cursor object to execute SQL commands
cursor = db.cursor()

# Define a function to display the menu
def display_menu():
    # Retrieve the menu items from the Items table
    cursor.execute("SELECT * FROM Items")
    menu_items = cursor.fetchall()
    
    # Display the menu items
    print("Menu:")
    for item in menu_items:
        print(f"{item[1]} - {item[2]} - ${item[3]}")

# Define a function to create a new order
def create_order():
    # Prompt the user for the customer ID
    customer_id = input("Enter customer ID: ")
    
    # Prompt the user for the table ID
    table_id = input("Enter table ID: ")
    
    # Prompt the user for the item IDs and quantities
    order_items = []
    while True:
        item_id = input("Enter item ID (or 'done' to finish): ")
        if item_id == 'done':
            break
        quantity = input("Enter quantity: ")
        order_items.append((item_id, quantity))
    
    # Insert the order into the Orders table
    cursor.execute(f"INSERT INTO Orders (customer_id, table_id) VALUES ({customer_id}, {table_id})")
    order_id = cursor.lastrowid
    
    # Insert the order items into the Order_Items table
    for item in order_items:
        cursor.execute(f"INSERT INTO Order_Items (order_id, item_id, quantity) VALUES ({order_id}, {item[0]}, {item[1]})")
    
    # Commit the changes to the database
    db.commit()
    print("Order created successfully.")

# Define a function to display the list of orders
def display_orders():
    # Retrieve the orders from the Orders table
    cursor.execute("SELECT * FROM Orders")
    orders = cursor.fetchall()
    
    # Display the orders
    print("Orders:")
    for order in orders:
        print(f"Order {order[0]} - Customer {order[1]} - Table {order[6]}")

# Define a function to display the details of a specific order
def display_order_details():
    # Prompt the user for the order ID
    order_id = input("Enter order ID: ")
    
    # Retrieve the order details from the Orders and Order_Items tables
    cursor.execute(f"SELECT * FROM Orders WHERE order_id={order_id}")
    order = cursor.fetchone()
    cursor.execute(f"SELECT * FROM Order_Items WHERE order_id={order_id}")
    order_items = cursor.fetchall()
    
    # Display the order details
    print(f"Order {order[0]} - Customer {order[1]} - Table {order[6]}")
    print("Items:")
    for item in order_items:
        cursor.execute(f"SELECT * FROM Items WHERE item_id={item[2]}")
        item_details = cursor.fetchone()
        print(f"{item_details[1]} - Quantity: {item[3]} - ${item_details[3]}")

# Define the main function to display the main menu and handle user input
def main():
    while True:
        print("\nRestaurant Management System")
        print("1. Display menu")
        print("2. Create order")
        print("3. Display orders")
        print("4. Display order details")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_menu()
        elif choice == '2':
            create_order()
        elif choice == '3':
            display_orders()
        elif choice == '4':
            display_order_details()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
    
    # Close the database connection
    db.close()

if __name__ == '__main__':
    main()
