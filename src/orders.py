"""Adds functionality for inputting new orders, functionality needs to be added to select an item for the order, maybe that would require something else but gonna keep em separate for now."""
import json
import products
from database_handler import get_correct_product_ids, read_all_items, read_all_orders, insert_new_order, get_correct_order_ids
from database_handler import update_customer_details
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
    

def orders_decision_tree():
    """Decision tree if user chooses o"""
    user_choice_cache = orders_get_user_choice()
    if user_choice_cache == 0:
        print("Returning to the main menu...\n\n\n\n\n\n")
        return 1
    elif user_choice_cache == 1:
        read_all_orders()
        return 0
    elif user_choice_cache == 2:
        customer_name = str(input("What is their name?\n"))
        customer_address = str(input("What is their address?\n"))
        customer_phone = str(input("What is their phone number?\n"))
        keep_choosing_products = "y"
        correct_product_ids = get_correct_product_ids()
        i = 0
        chosen_product_list = []
        while keep_choosing_products == "y":
            # Need to make a list then for item in list add at the end with everything else for atomicity
            chosen_product = input(f"What is the  have #{i} they selected? (or type ls for product list)\n")
            while chosen_product not in correct_product_ids or chosen_product != "ls":
                print("That is not a valid product")
            while chosen_product == "ls":
                read_all_items()
            chosen_product_list.append(chosen_product)
            i +=1
        statuses = ["paid", "preparing", "en-route", "completed"]
        status_length = len(statuses) - 1
        for (i, item) in enumerate(statuses, start = 0):
            print(i, item)
        chosen_status_ind = int(input(f"Please pick a status 0-{status_length}: "))
        chosen_status = statuses[chosen_status_ind]
        insert_new_order(chosen_status, customer_name, customer_address, customer_phone, chosen_product_list)
        read_all_orders()
        return 0
    elif user_choice_cache == 3:
        read_all_orders()
        correct_order_ids = get_correct_order_ids()
        user_change = str(input("Which order would you like to change, please select the order id"))
        while user_change not in correct_order_ids:
            print("That is not a valid order id")
            user_change = str(input("Which order would you like to change, please select the order id"))
        which_order_table = str(input("Which table would you like to change 'status', 'details' or 'items'").lower())
        while which_order_table not in ["status", "items", "details"]:
            print("Please select items or details")
            which_order_table = str(input("Which table would you like to change 'status', 'details' or 'items'").lower())
        if which_order_table == "details":
            changed_customer_name = str(input("What do you wish to change the customer name to? or hit enter to leave the same:\n"))
            changed_customer_phone = str(input("What do you wish to change the customer phone number to? or hit enter to leave the same:\n"))
            changed_customer_address = str(input("What do you wish to change the customer address to? or hit enter to leave the same:\n"))
            update_customer_details(user_change, changed_customer_name, changed_customer_phone, changed_customer_address)
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
