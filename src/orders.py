"""Adds functionality for inputting new orders, functionality needs to be added to select an item for the order, maybe that would require something else but gonna keep em separate for now."""
import pymysql
from database_handler import get_correct_product_ids, read_all_items, read_all_orders, insert_new_order, get_correct_order_ids
from database_handler import update_customer_details, update_order_status, read_customer_details, read_orders, read_order_items
from database_handler import get_available_item_ids_on_orders, insert_new_items, delete_order, update_order_items
from database_handler import read_all_couriers, get_correct_courier_ids, update_courier_order, update_courier_details
def orders_get_user_choice():
    """Get's the user's choice and returns the value to be cached later."""
    user_choice = input("Please pick an operation:\nReturn to main menu (0).\
                        \nPrint order list (1).\
                        \nAdd Order to list (2).\nUpdate existing order (3).\
                        \nDelete Order(4). \
                        \nAssign courier to an order(5)\n")

    while user_choice not in ["0", "1", "2", "3", "4", "5"]:
        print("Please pick a valid number.")
        user_choice = input("Please pick an operation:\nReturn to main menu (0).\
                        \nPrint order list (1).\
                        \nAdd Order to list (2).\nUpdate existing order (3).\
                        \nDelete Order(4). \
                        \nAssign courier to an order(5)\n")
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
            i +=1
            chosen_product = str(input(f"What is the  have #{i} item they selected? (or type ls for product list)\n").upper())
            if chosen_product == "LS":
                read_all_items()
                chosen_product = str(input(f"What is the  have #{i} item they selected?\n").upper())
            while chosen_product not in correct_product_ids:
                print("That is not a valid product")
                chosen_product = str(input(f"What is the  have #{i} item they selected?\n").upper())
            chosen_product_list.append(chosen_product)
            keep_choosing_products = input("Would you like to keep adding items to their order y/n?: ")
        statuses = ["paid", "preparing", "en-route", "completed"]
        status_length = len(statuses) - 1
        for (i, item) in enumerate(statuses, start = 0):
            print(i, item)
        chosen_status_ind = int(input(f"Please pick a status 0-{status_length}: "))
        chosen_status = statuses[chosen_status_ind]
        this_order_id = insert_new_order(chosen_status, customer_name, customer_address, customer_phone, chosen_product_list)
        assign_courier_now = str(input("Do you wish to assign a courier to this order now? y/n\n").lower())
        if assign_courier_now != "y":
            read_all_orders()
            print("Returning to main menu.")
            return 0
        try:
            valid_couriers = get_correct_courier_ids()
        except pymysql.err.OperationalError:
            print("There are no current couriers, returning to the main menu.")
            return 1
        read_all_couriers()
        which_courier = str(input("Which courier ID do you wish to assign?\n").upper())
        while which_courier not in valid_couriers:
            print("That courier doesn't exist")
            which_courier = str(input("Which courier ID do you wish to assign?\n").upper())
        which_order = this_order_id
        update_courier_order(order_id=which_order, courier_id=which_courier)
        update_courier_details(courier_status="assigned", courier_id=which_courier, courier_name="", courier_phone="")
        read_all_couriers()
        return 0
    elif user_choice_cache == 3:
        read_all_orders()
        try:
            correct_order_ids = get_correct_order_ids()
        except pymysql.err.OperationalError:
            print("There are no current orders, returning to the menu\n")
            return 0
        user_change = str(input("Which order would you like to change, please select the order id: ").upper())
        while user_change not in correct_order_ids:
            print("That is not a valid order id")
            user_change = str(input("Which order would you like to change, please select the order id?: "))
        which_order_table = str(input("Which table would you like to change 'status', 'details' or 'items'?: ").lower())
        while which_order_table not in ["status", "items", "details"]:
            print("Please select items or details")
            which_order_table = str(input("Which table would you like to change 'status', 'details' or 'items'").lower())
        if which_order_table == "details":
            read_customer_details()
            changed_customer_name = str(input("What do you wish to change the customer name to? or hit enter to leave the same:\n"))
            changed_customer_phone = str(input("What do you wish to change the customer phone number to? or hit enter to leave the same:\n"))
            changed_customer_address = str(input("What do you wish to change the customer address to? or hit enter to leave the same:\n"))
            update_customer_details(user_change, changed_customer_name, changed_customer_phone, changed_customer_address)
        elif which_order_table == "status":
            read_orders()
            statuses = ["paid", "preparing", "en-route", "completed"]
            status_length = len(statuses) - 1
            for (i, item) in enumerate(statuses, start = 0):
                print(i, item)
            chosen_status_ind = int(input(f"Please pick a status 0-{status_length}: "))
            changed_status = statuses[chosen_status_ind]
            update_order_status(user_change, changed_status)
        elif which_order_table == "items":
            correct_product_ids = get_correct_product_ids()
            add_new_items_to_order = str(input("Would you like to add new items to this order y/n?\n"))
            if add_new_items_to_order == "n":
                print("Continuing...\n")
            elif add_new_items_to_order == "y":
                keep_choosing_products = "y"
                correct_product_ids = get_correct_product_ids()
                i = 0
                chosen_product_list = []
                while keep_choosing_products == "y":
                    i +=1
                    chosen_product = input(f"What is the  have #{i} item they selected? (or type ls for product list)\n")
                    while chosen_product == "ls":
                        read_all_items()
                        chosen_product = input(f"What is the  have #{i} they selected? (or type ls for product list)\n")
                    while chosen_product not in correct_product_ids:
                        print("That is not a valid product")
                        chosen_product = input(f"What is the  have #{i} item they selected? (or type ls for product list)\n")
                    chosen_product_list.append(chosen_product)
                    keep_choosing_products = input("Would you like to keep adding items to their order y/n?: ")
                insert_new_items(user_change, chosen_product_list)
            read_order_items()
            available_to_change = get_available_item_ids_on_orders(user_change)
            item_to_change_from = str(input("Which item code of this order would you like to change? or hit enter to go to the menu\n"))
            if not item_to_change_from:
                return 0
            while item_to_change_from not in available_to_change:
                print("That is not a valid item to change")
            item_to_change_to = str(input("Please enter the item ID you would like to change the item to? or type ls for a list of products\n"))
            while item_to_change_to == "ls":
                read_all_items()
                item_to_change_to = input("Please enter the item ID you would like to change the item to? (or type ls for product list)\n") 
            while item_to_change_to not in correct_product_ids:
                print("That is not a valid product")
                item_to_change_to = input("Please enter the item ID you would like to change the item to? (or type ls for product list)\n")
            update_order_items(user_change, item_to_change_to, item_to_change_from)
            read_order_items()
        return 0
    elif user_choice_cache == 4:
        read_all_orders()
        try:
            correct_order_ids = get_correct_order_ids()
        except pymysql.err.OperationalError:
            print("There are no current orders, returning to the menu\n")
            return 0
        user_change = str(input("Which order ID would you like to delete?\nOr leave blank to skip the operation\n").upper())
        while user_change not in correct_order_ids and user_change:
            print("That is not a valid order id")
            user_change = str(input("Which order ID would you like to delete?\nOr leave blank to skip the operation\n").upper())
        if user_change:
            delete_order(user_change)
            read_all_orders()
            print("Order removed successfully, returning to the menu")
        else:
            print("Operation skipped, returning to the menu.")
        return 0
    elif user_choice_cache == 5:
        try:
            valid_couriers = get_correct_courier_ids()
            valid_orders = get_correct_order_ids()
        except pymysql.err.OperationalError:
            print("There are no current couriers, returning to the main menu.")
            return 1
        read_all_couriers()
        which_courier = str(input("Which courier ID do you wish to assign?\n").upper())
        while which_courier not in valid_couriers:
            print("That courier doesn't exist")
            which_courier = str(input("Which courier ID do you wish to assign?\n").upper())
        read_all_orders()
        which_order = str(input("Which order ID do you wish to assign?\n").upper())
        while which_order not in valid_orders:
            print("That order doesn't exist")
            which_order = str(input("Which order ID do you wish to assign?\n").upper())
        update_courier_order(order_id=which_order, courier_id=which_courier)
        update_courier_details(courier_status="assigned", courier_id=which_courier, courier_name="", courier_phone="")
        return 0
    else:
        print("An error has occurred, returning to the main menu (else has been hit)")
        return 1
