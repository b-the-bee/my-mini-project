import os
import random
import string
import json
import pymysql
from dotenv import load_dotenv

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
        new_id = f"P{data['item_id']:03d}"
    elif id_type == 'order':
        data['order_id'] += 1
        new_id = f"O{data['order_id']:04d}"
    else:
        raise ValueError("Invalid id_type. Must be 'courier', 'item', or 'order'.")
    
    save_data_to_file(file_path, data)
    return new_id

# Path to the file where the data will be saved
default_file_path = 'data/ids.json'

# ----------------------
# Items/Products Functions
# ----------------------

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
            data = cursor.fetchall()
    return data

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

def get_item_names():
    with pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT item_id, item FROM items")
            item_name_tuple_list = cursor.fetchall()
            # Create a dictionary mapping item_id to item_name
            item_name_dict = {item_id: item for item_id, item in item_name_tuple_list}
    return item_name_dict

def update_item(item_id, item_name, item_price):
    if item_name:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
        ) as connection:
            with connection.cursor() as cursor:
                update_sql = """
                UPDATE items
                SET item = %s
                WHERE item_id = %s
                """
                values = (item_name, item_id)
                cursor.execute(update_sql, values)
                connection.commit()       
    if item_price:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
        ) as connection:
            with connection.cursor() as cursor:
                update_sql = """
                UPDATE items
                SET price = %s
                WHERE item_id = %s
                """
                values = (item_price, item_id)
                cursor.execute(update_sql, values)
                connection.commit()

def delete_item(item_id):
    try:
        with pymysql.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_name
        ) as connection:
            with connection.cursor() as cursor:
                delete_order_items_sql = "DELETE FROM order_items WHERE item_id = %s;"

                cursor.execute(delete_order_items_sql, (item_id,))

            connection.commit()
    except pymysql.err.OperationalError:
        print("There are no orders to remove this item from, continuing..")
    finally:
        with pymysql.connect(
                host=host_name,
                user=user_name,
                password=user_password,
                database=database_name
        ) as connection:
            with connection.cursor() as cursor:
                delete_item_sql = "DELETE FROM items WHERE item_id = %s;"   
                cursor.execute(delete_item_sql, (item_id,))
            connection.commit()
# ----------------------
# Orders Functions
# ----------------------

def insert_new_order(orders_status, customers_name, customers_address, customers_phone, chosens_products):
    new_order_id = increment_and_save_id(file_path=default_file_path, id_type='order')
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
    return this_order_id
    
def read_orders():
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM orders")
            data = cursor.fetchall()
    return data       
        

def read_customer_details():
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT ocd.*, oi.item_ordered FROM order_customer_details ocd INNER JOIN order_items oi ON ocd.order_id=oi.order_id")
            data = cursor.fetchall()
            
    return data
        
def read_order_items():
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM order_items")
            data = cursor.fetchall()
        return data
    
import pymysql

def read_one_order(order_id):
    connection = pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name,
    )
    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM orders WHERE order_id = %s"
                cursor.execute(sql, (order_id,))
                data = cursor.fetchone()
                if data:
                    # Fetch column names from cursor description
                    columns = [desc[0] for desc in cursor.description]
                    # Combine columns and data into a dictionary
                    result = dict(zip(columns, data))
                    return result
                else:
                    return None
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        return None


        
def just_order_items():
    with pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT item_ordered FROM order_items")
            info_list = cursor.fetchall()
            
            # Extract items from tuples and clean them
            cleaned_list = []
            for item_tuple in info_list:
                item = item_tuple[0]  # Extract the string from the tuple
                cleaned_item = item.replace("(", "").replace(")", "").replace(",", "")
                cleaned_list.append(cleaned_item)
    return cleaned_list

def read_orders_by_status(status):
    with pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name,
    ) as connection:
        with connection.cursor() as cursor:
            select_sql = "SELECT order_id, order_status FROM orders WHERE order_status = %s"
            cursor.execute(select_sql, (status,))
            rows = cursor.fetchall()
            
            # Create a PrettyTable for orders
            order_table = PrettyTable()
            order_table.field_names = ["order_id", "order_status"]
            
            # List to hold order IDs
            order_ids = []

            # Add rows to the order table and collect order IDs
            for row in rows:
                order_table.add_row(row)
                order_ids.append(row[0])  # Append the order_id to the list
            
            # Print the order table
            print(order_table)
            
            # Create a PrettyTable for customer details
            customer_details_table = PrettyTable()
            customer_details_table.field_names = ["order_id", "customer_name", "customer_phone", "customer_address"]
            
            # Fetch and display customer details for each order ID
            for order_id in order_ids:
                select_customer_sql = """
                SELECT order_id, customer_name, customer_phone, customer_address
                FROM order_customer_details
                WHERE order_id = %s
                """
                cursor.execute(select_customer_sql, (order_id,))
                customer_details = cursor.fetchall()
                
                for detail in customer_details:
                    customer_details_table.add_row(detail)
            order_details_table = PrettyTable()
            order_details_table.field_names = ["row_id", "order_id", "item_ordered"]
            for order_id in order_ids:
                select_customer_sql = """
                SELECT row_id, order_id, item_ordered
                FROM order_items
                WHERE order_id = %s
                """
                cursor.execute(select_customer_sql, (order_id,))
                items_ordered = cursor.fetchall()
                
                for item in items_ordered:
                    order_details_table.add_row(item)
        return customer_details_table,

def read_all_orders():
    read_orders()
    read_customer_details()
    read_order_items()

def get_correct_order_ids():
    with pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT order_id FROM orders")
            order_id_list = cursor.fetchall()
            # Extract item_ids from the fetched rows
            order_id_list = [row[0] for row in order_id_list]
    return order_id_list

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


def update_order_status(order_id, status):
    if status:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
        ) as connection:
            with connection.cursor() as cursor:
                update_sql = """
                UPDATE orders
                SET order_status = %s
                WHERE order_id = %s
                """
                values = (status, order_id)
                cursor.execute(update_sql, values)
                connection.commit()

def update_order_items(order_id, item_change_to, item_change_from):
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            update_sql = """
            UPDATE order_items
            SET item_ordered = %s
            WHERE order_id = %s AND item_ordered = %s
            """
            values = (item_change_to, order_id, item_change_from)
            cursor.execute(update_sql, values)
            connection.commit()

def insert_new_items(this_order_id, chosens_products):
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
                
def get_available_item_ids_on_orders(order_id):
    with pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name
    ) as connection:
        with connection.cursor() as cursor:
            sql_read ="""
            SELECT item_ordered from order_items WHERE order_id = %s
            """
            value = order_id
            cursor.execute(sql_read, value)
            product_id_list = cursor.fetchall()
            # Extract item_ids from the fetched rows
            product_id_list = [row[0] for row in product_id_list]
    return product_id_list



def delete_order(order_id):
    with pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name
    ) as connection:
        with connection.cursor() as cursor:
            delete_order_courier_details_sql = "DELETE FROM courier_delivery_details WHERE order_id = %s";
            delete_order_customer_details_sql = "DELETE FROM order_customer_details WHERE order_id = %s;"
            delete_order_items_sql = "DELETE FROM order_items WHERE order_id = %s;"
            delete_order_sql = "DELETE FROM orders WHERE order_id = %s;"
            
            cursor.execute(delete_order_courier_details_sql , (order_id))
            cursor.execute(delete_order_customer_details_sql, (order_id,))
            cursor.execute(delete_order_items_sql, (order_id,))
            cursor.execute(delete_order_sql, (order_id,))
            
        connection.commit()
            

# ----------------------
# Couriers Functions
# ----------------------

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
            
def read_couriers():
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM couriers")
            data = cursor.fetchall()

    return data
    

def read_couriers_delivery():
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM courier_delivery_details")
            data = cursor.fetchall()
    return data

def read_couriers_by_status(status):
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            select_sql = ("SELECT * FROM couriers WHERE courier_status = %s")
            value = status
            cursor.execute(select_sql, value)
            rows = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["courier_id", "courier_name", "courier_phone", "courier_status"]

        # Add rows to the table
        for row in rows:
            table.add_row(row)
        
        # Print the table
        print(table)

def get_correct_courier_ids():
    with pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT courier_id FROM couriers")
            order_id_list = cursor.fetchall()
            # Extract item_ids from the fetched rows
            order_id_list = [row[0] for row in order_id_list]
    return order_id_list

def update_courier_details(courier_id, courier_name, courier_phone, courier_status):
    if courier_name:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
        ) as connection:
            with connection.cursor() as cursor:
                update_sql = """
                UPDATE couriers
                SET courier_name = %s
                WHERE courier_id = %s
                """
                values = (courier_name, courier_id)
                cursor.execute(update_sql, values)
                connection.commit()       
    if courier_phone:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
        ) as connection:
            with connection.cursor() as cursor:
                update_sql = """
                UPDATE couriers
                SET courier_phone = %s
                WHERE courier_id = %s
                """
                values = (courier_phone, courier_id)
                cursor.execute(update_sql, values)
                connection.commit()   
    if courier_status:
        with pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
        ) as connection:
            with connection.cursor() as cursor:
                update_sql = """
                UPDATE couriers
                SET courier_status = %s
                WHERE courier_id = %s
                """
                values = (courier_status, courier_id)
                cursor.execute(update_sql, values)
                connection.commit()

def update_courier_order(courier_id, order_id):
    if order_id:
        with pymysql.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_name,
        ) as connection:
            with connection.cursor() as cursor:
                update_sql = """
                INSERT INTO courier_delivery_details (courier_id, order_id)
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE order_id = VALUES(order_id)
                """
                values = (courier_id, order_id)
                cursor.execute(update_sql, values)
                connection.commit()

def delete_courier(courier_id):
    with pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name
    ) as connection:
        with connection.cursor() as cursor:
            delete_couriers_sql = "DELETE FROM couriers WHERE courier_id = %s;"
            delete_courier_delivery_sql = "DELETE FROM courier_delivery_details WHERE courier_id = %s;"

            cursor.execute(delete_couriers_sql, (courier_id,))
            cursor.execute(delete_courier_delivery_sql, (courier_id,))

        connection.commit()

def get_valid_courier_order_ids():
    with pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT order_id FROM courier_delivery_details")
            order_id_list = cursor.fetchall()
            # Extract item_ids from the fetched rows
            order_id_list = [row[0] for row in order_id_list]
    return order_id_list