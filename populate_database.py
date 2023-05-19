import mysql.connector
from faker import Faker
import random

# Connect to the database
cnx = mysql.connector.connect(user='username', password='password',
                              host='localhost',
                              database='restaurant')
cursor = cnx.cursor()

# Generate sample menu items
menu_items = [
    ('Cheeseburger', 'Juicy beef patty with melted cheese', 9.99),
    ('Margherita Pizza', 'Classic pizza with tomato sauce and fresh mozzarella', 11.99),
    ('Caesar Salad', 'Crisp romaine lettuce with Parmesan cheese and croutons', 7.99),
    ('Spaghetti Bolognese', 'Hearty meat sauce served over al dente spaghetti', 12.99),
    ('Grilled Salmon', 'Fresh Atlantic salmon grilled to perfection', 18.99)
]

# Insert menu items into the database
for item in menu_items:
    add_item = """
    INSERT INTO menu (item_name, item_description, item_price)
    VALUES (%s, %s, %s)
    """
    cursor.execute(add_item, item)

# Generate sample orders
fake = Faker()
for i in range(20):
    # Generate a random order with 1-3 items
    num_items = random.randint(1, 3)
    items = random.sample(menu_items, num_items)
    order_items = []
    for item in items:
        order_items.append((item[0], random.randint(1, 5)))
    total_price = sum([item[1] * item[0][2] for item in zip(order_items, items)])
    customer_name = fake.name()
    # Insert the order and order details into the database
    add_order = """
    INSERT INTO orders (customer_name)
    VALUES (%s)
    """
    cursor.execute(add_order, (customer_name,))
    order_id = cursor.lastrowid
    for item in order_items:
        add_order_detail = """
        INSERT INTO order_details (order_id, item_id, quantity)
        VALUES (%s, (SELECT item_id FROM menu WHERE item_name=%s), %s)
        """
        cursor.execute(add_order_detail, (order_id, item[0], item[1]))
    cnx.commit()

# Close the cursor and database connection
cursor.close()
cnx.close()
