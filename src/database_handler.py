import os
import random
import string
import json
import pymysql
from dotenv import load_dotenv
from prettytable import PrettyTable

load_dotenv()

host_name = os.environ.get("mysql_host")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")
database_name = os.environ.get("mysql_db")

def read_data_from_file(file_path):
    """Read the data from the JSON file, if it exists. Otherwise, return a default structure."""
    try:
        with open(file_path, 'r', encoding="UTF-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'courier_id': 0, 'item_id': 0, 'order_id': 0}
    except json.JSONDecodeError:
        data = {'courier_id': 0, 'item_id': 0, 'order_id': 0}
    return data

def save_data_to_file(file_path, data):
    """Save the data to the JSON file."""
    with open(file_path, 'w', encoding="UTF-8") as file:
        json.dump(data, file, indent=4)

def increment_and_save_id(file_path, id_type):
    """Read the current IDs from the file, increment the specified ID, and save it back to the file."""
    data = read_data_from_file(file_path)
    
    if id_type == 'courier':
        data['courier_id'] += 1
        new_id = f"C{data['courier_id']:04d}"
    elif id_type == 'item':
        data['item_id'] += 1
        new_id = f"I{data['item_id']:03d}"
    elif id_type == 'order':
        data['order_id'] += 1
        new_id = f"O{data['order_id']:04d}"
    else:
        raise ValueError("Invalid id_type. Must be 'courier', 'item', or 'order'.")
    
    save_data_to_file(file_path, data)
    return new_id

# Path to the file where the data will be saved
default_file_path = 'ids.json'

# Items/Products Functions

def insert_new_item(item, price):
    new_item_id = increment_and_save_id(file_path=default_file_path, id_type='item')
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            insert_sql = """
            INSERT INTO items (item_id, item, price)
            VALUES (%s, %s, %s)
            """
            values = (new_item_id, item, price)
            cursor.execute(insert_sql, values)
            connection.commit()
            
def read_all_items():
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM items")
            rows = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["item_id", "item", "price"]

        # Add rows to the table
        for row in rows:
            table.add_row(row)
        
        # Print the table
        print(table)

def get_correct_product_ids():
    with pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT item_id FROM items")
            product_id_list = cursor.fetchall()
            # Extract item_ids from the fetched rows
            product_id_list = [row[0] for row in product_id_list]
    return product_id_list

# Orders Functions
def insert_new_order(orders_status, customers_name, customers_address, customers_phone, chosens_products):
    new_order_id = increment_and_save_id(file_path=default_file_path, id_type='courier')
    modifier1 = str(random.randint(10, 99))
    modifier2 = ''.join(random.choices(string.ascii_uppercase, k=2))
    this_order_id = str(new_order_id + modifier1 + modifier2)
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            insert_sql = """
            INSERT INTO orders (order_id, order_status)
            VALUES (%s, %s)
            """
            values = (this_order_id, orders_status)
            cursor.execute(insert_sql, values)
            connection.commit()
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            insert_sql = """
            INSERT INTO order_customer_details (order_id, customer_name, customer_phone, customer_address)
            VALUES (%s, %s, %s, %s)
            """
            values = (this_order_id, customers_name, customers_phone, customers_address)
            cursor.execute(insert_sql, values)
            connection.commit()
    for item in chosens_products:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
        ) as connection:
            with connection.cursor() as cursor:
                insert_sql = """
                INSERT INTO order_items (order_id, item_ordered)
                VALUES (%s, %s)
                """
                values = (this_order_id, item)
                cursor.execute(insert_sql, values)
                connection.commit()        
def read_orders():
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM orders")
            rows = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["order_id", "order_status"]

        # Add rows to the table
        for row in rows:
            table.add_row(row)
        
        # Print the table
        print(table)
def read_customer_details():
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM order_customer_details")
            rows = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["order_id", "customer_name", "customer_phone", "customer_address"]

        # Add rows to the table
        for row in rows:
            table.add_row(row)
        # Print the table
        print(table)
        
def read_order_items():
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM order_items")
            rows = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["order_id", "item_ordered"]

        # Add rows to the table
        for row in rows:
            table.add_row(row)
        
        # Print the table
        print(table)
def update_customer_details(order_id, customer_name, customer_phone, customer_address):
    if customer_name:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
        ) as connection:
            with connection.cursor() as cursor:
                update_sql = """
                UPDATE order_customer_details
                SET customer_name = %s
                WHERE order_id = %s
                """
                values = (customer_name, order_id)
                cursor.execute(update_sql, values)
                connection.commit()       
    if customer_phone:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
        ) as connection:
            with connection.cursor() as cursor:
                update_sql = """
                UPDATE order_customer_details
                SET customer_phone = %s
                WHERE order_id = %s
                """
                values = (customer_phone, order_id)
                cursor.execute(update_sql, values)
                connection.commit()   
    if customer_address:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
        ) as connection:
            with connection.cursor() as cursor:
                update_sql = """
                UPDATE order_customer_details
                SET customer_address = %s
                WHERE order_id = %s
                """
                values = (customer_address, order_id)
                cursor.execute(update_sql, values)
                connection.commit()   


def get_correct_order_ids():
    with pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT order_id FROM items")
            order_id_list = cursor.fetchall()
            # Extract item_ids from the fetched rows
            order_id_list = [row[0] for row in order_id_list]
    return order_id_list

# Couriers Functions
def insert_new_courier(courier_name, courier_phone, courier_status):
    new_courier_id = increment_and_save_id(file_path=default_file_path, id_type='courier')
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            insert_sql = """
            INSERT INTO couriers (courier_id, courier_name, courier_phone, courier_status)
            VALUES (%s, %s, %s, %s)
            """
            values = (new_courier_id, courier_name, courier_phone, courier_status)
            cursor.execute(insert_sql, values)
            connection.commit()
            
def read_all_couriers():
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM couriers")
            rows = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["courier_id", "courier_name", "courier_phone", "courier_status"]

        # Add rows to the table
        for row in rows:
            table.add_row(row)
        
        # Print the table
        print(table)
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM courier_delivery_details")
            rows = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["courier_id", "order_id",]

        # Add rows to the table
        for row in rows:
            table.add_row(row)
        
        # Print the table
        print(table)