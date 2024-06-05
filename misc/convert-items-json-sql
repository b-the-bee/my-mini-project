# if to be ran again needs to be ran from src for some reason
import json
from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

# Read JSON file
try:
    with open("data/products.json", "r", encoding="UTF-8") as my_file:
        product_list = json.load(my_file)
except FileNotFoundError as fnfe:
    print(f"Unable to open file: {fnfe}")
    product_list = []
except json.JSONDecodeError as jde:
    print(f"Error decoding JSON: {jde}")
    product_list = []


host_name = os.environ.get("mysql_host")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")
database_name = os.environ.get("mysql_db")

for item in product_list:
    with pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database_name,
    ) as connection:
        with connection.cursor() as cursor:
            insert_sql = """
            INSERT INTO couriers (item, price)
            VALUES (%s, %s)
            """
            values = (item["item"], item["price"])
            cursor.execute(insert_sql, values)
            connection.commit()