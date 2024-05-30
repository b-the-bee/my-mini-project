"""Adds functionality for inputting new orders, functionality needs to be added to select an item for the order, maybe that would require something else but gonna keep em separate for now."""
import json
import products
order_list = []

def read_order_list():
    """Reads product list and returns it"""
    try:
        with open("data/orders.json", "r", encoding="UTF-8") as my_file:
            orders_list = json.load(my_file)
    except FileNotFoundError as fnfe:
        print(f"Unable to open file: {fnfe}")
        orders_list = []
    except json.JSONDecodeError as jde:
        print(f"Error decoding JSON: {jde}")
        orders_list = []
    return orders_list

def write_order_list(orders_list):
    """Function for persisting product list"""
    try:
        with open("data/orders.json", "w", encoding="UTF-8") as my_file:
            json.dump(orders_list, my_file, indent=4)  # Write the list of dictionaries to the file
    except FileNotFoundError as fnfe:
        print(f"Error writing to file: {fnfe}")

def orders_get_user_choice():
    """Get's the user's choice and returns the value to be cached later."""
    user_choice = input("Please pick an operation:\nReturn to main menu (0).\
                        \nPrint order list (1).\
                        \nAdd Order to list (2).\nUpdate existing order (3).\
                        \nDelete Order(4). \n")

    while user_choice not in ["0", "1", "2", "3", "4"]:
        print("Please pick a valid number.")
        user_choice = input("Please pick an operation:\nReturn to main menu (0).\
                        \nPrint order list (1).\
                        \nAdd Order to list (2).\nUpdate existing order (3).\
                        \nDelete Order(4). \n")
    user_choice = int(user_choice)
    return user_choice

def show_orders(orders_list):
    """Shows a list of saved orders, formatted in dictionaries"""
    print("Here is the list of the orders:")
    for (i, item) in enumerate(orders_list, start = 0):
        print(f"""Order: \n{i}.
              \nCustomer Name:{[item['customer-name']]}
              \nCustomer Address:{[item['customer-address']]}
              \nCustomer Phone #:{[item['customer-phone']]}
              \nCustomer Items :{[item['items']]}
              \nStatus:{[item['status']]}\n\n """)

def orders_decision_tree():
    """Decision tree if user chooses o"""
    order_list = read_order_list()
    user_choice_cache = orders_get_user_choice()
    if user_choice_cache == 0:
        print("Returning to the main menu...\n\n\n\n\n\n")
        return 1
    elif user_choice_cache == 1:
        order_list_length = len(order_list) - 1
        show_orders(order_list)
        return 0
    elif user_choice_cache == 2:
        customer_name = str(input("What is their name?\n"))
        customer_address = str(input("What is their address?\n"))
        customer_phone = str(input("What is their phone number?\n"))
        chosen_products = input("What products have they selected? (or type ls for product list)\n")
        while chosen_products == "ls":
            product_list = products.read_product_list()
            products.show_products(product_list)
            chosen_products = input("What products have they selected? (or type ls for product list)\n")
        statuses = ["paid", "preparing", "en-route", "completed"]
        status_length = len(statuses) - 1
        for (i, item) in enumerate(statuses, start = 0):
            print(i, item)
        chosen_status_ind = int(input(f"Please pick a status 0-{status_length}: "))
        chosen_status = statuses[chosen_status_ind]
        temp_dict = {
            "customer-name": customer_name,
            "customer-address": customer_address,
            "customer-phone": customer_phone,
            "items": chosen_products,
            "status": chosen_status,
        }
        order_list.append(temp_dict)
        show_orders(order_list)
        write_order_list(order_list)
        return 0
    elif user_choice_cache == 3 and order_list:
        order_list_length = len(order_list) - 1
        show_orders(order_list)
        user_change = int(input(f"Which order do you wish to change? 0-{order_list_length}: "))
        while user_change < 0 or user_change > order_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to change? 0-{order_list_length}: "))
        valid_keys = ["customer-name", "customer-address", "customer-phone", "status"]
        key_change = str(input(f"What about the order would you like to update? {valid_keys}\n").lower())
        while key_change not in valid_keys:
            print("That is not a valid input.")
            key_change = str(input(f"What about the order would you like to update? {valid_keys}\n").lower())
        if key_change == "status":
            status_length = len(statuses) - 1
            for (i, item) in enumerate(statuses, start = 0):
                print(i, item)
            chosen_status_ind = int(input(f"Please pick a status 0-{status_length}: "))
            chosen_status = statuses[chosen_status_ind]
        else:
            details_change = str(input("What do you wish to change it to?\n"))
        order_list[user_change][key_change] = details_change
        show_orders(order_list)
        write_order_list(order_list)
        return 0
    elif user_choice_cache == 4 and order_list:
        order_list_length = len(order_list) - 1
        show_orders(order_list)
        user_change = int(input(f"Which order do you wish to delete? 0-{order_list_length}: "))
        while user_change < 0 or user_change > order_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to change? 0-{order_list_length}: "))
        order_list.pop(user_change)
        show_orders(order_list)
        write_order_list(order_list)
        return 0
    else:
        print("No current orders")
        return 0
