import json
from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

host_name = os.environ.get("mysql_host")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")
database_name = os.environ.get("mysql_db")

def read_data_from_file():
    """Read the data from the JSON file, if it exists. Otherwise, return a default structure."""
    try:
        with open("data\ids.json", 'r', encoding="UTF-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'courier_id': 0, 'item_id': 0, 'order_id': 0}
    except json.JSONDecodeError:
        data = {'courier_id': 0, 'item_id': 0, 'order_id': 0}
    return data

def save_data_to_file(data):
    """Save the data to the JSON file."""
    with open("data\ids.json", 'w', encoding="UTF-8") as file:
        json.dump(data, file, indent=4)

def increment_and_save_id(id_type):
    """Read the current IDs from the file, increment the specified ID, and save it back to the file."""
    data = read_data_from_file()
    
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
    
    save_data_to_file(data)
    return new_id


# Generate new IDs
new_courier_id = increment_and_save_id('courier')
new_item_id = increment_and_save_id('item')
new_order_id = increment_and_save_id('order')

def insert_new_item(item, price):
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            insert_sql = """
            INSERT INTO items (customer_name, customer_phone, customer_address, items, order_status)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (item["customer-name"], item["customer-phone"], item["customer-address"], item["items"], item["status"])
            cursor.execute(insert_sql, values)
            connection.commit()

