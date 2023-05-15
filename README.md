

# Restaurant Management System

This is a Python application that manages orders for a restaurant. The application uses a SQL database to store information about the menu, orders, and order details.

## Installation

1. Install Python 3.x from the official website: https://www.python.org/downloads/
2. Install a SQL database management system such as MySQL or PostgreSQL.
3. Install the necessary Python packages: `mysql-connector-python` and `tabulate`. You can install these packages using pip with the following commands:

    ```
    pip install mysql-connector-python
    pip install tabulate
    ```

4. Clone this repository:

    ```
    git clone https://github.com/your_username/restaurant-management.git
    ```

## Usage

1. Open a terminal or command prompt and navigate to the cloned repository directory.
2. Create the database and tables by running the `create_database.py` script:

    ```
    python create_database.py
    ```

3. Populate the database with sample data by running the `populate_database.py` script:

    ```
    python populate_database.py
    ```

4. Run the main application by running the `main.py` script:

    ```
    python main.py
    ```

5. Follow the prompts in the application to manage orders.

## Features

The Restaurant Management System application provides the following features:

- Display menu: Displays the menu items with their descriptions and prices.
- Create order: Prompts the user to create an order by selecting menu items and specifying the quantity.
- Display orders: Displays all orders with their order IDs, customer names, and order timestamps.
- Display order details: Displays the details of an order by specifying the order ID.

## Schema
![Schema for DB](https://github.com/ameykunte/DB_Project/assets/70936188/3436dd1e-23a6-4988-8cef-ea2ba41d54b5)


## Contributing

Contributions to this project are welcome! Here are some ways you can contribute:

- Report bugs or issues.
- Suggest new features or improvements.
- Fork the repository and make your own changes. Submit a pull request to merge your changes back into the main branch.



