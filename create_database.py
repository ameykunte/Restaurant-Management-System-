import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='username', password='password',
                              host='localhost',
                              database='restaurant')

# Create a cursor to execute SQL commands
cursor = cnx.cursor()

# Create the menu table
menu_table = '''
CREATE TABLE menu (
  item_id INT AUTO_INCREMENT PRIMARY KEY,
  item_name VARCHAR(50) NOT NULL,
  item_description TEXT,
  item_price DECIMAL(5,2) NOT NULL
)
'''
cursor.execute(menu_table)

# Create the orders table
orders_table = '''
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(50) NOT NULL,
  order_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
'''
cursor.execute(orders_table)

# Create the order details table
order_details_table = '''
CREATE TABLE order_details (
  order_id INT NOT NULL,
  item_id INT NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (order_id, item_id),
  FOREIGN KEY (order_id)
    REFERENCES orders(order_id)
    ON DELETE CASCADE,
  FOREIGN KEY (item_id)
    REFERENCES menu(item_id)
    ON DELETE CASCADE
)
'''
cursor.execute(order_details_table)

# Close the cursor and database connection
cursor.close()
cnx.close()
