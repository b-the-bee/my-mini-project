"""Couriers management system"""
import pymysql
from database_handler import read_all_couriers, insert_new_courier, get_correct_courier_ids, update_courier_details, update_courier_order, delete_courier, read_couriers_by_status
from database_handler import read_orders, get_correct_order_ids, get_valid_courier_order_ids, read_all_orders
def couriers_get_user_choice():
    """Get's the user's choice and returns the value to be cached later."""
    user_choice = input("\nPlease pick an operation:\nReturn to main menu (0).\
                        \nPrint courier list (1).\
                        \nAdd courier to list (2).\nUpdate existing courier (3).\
                        \nDelete courier(4). \
                        \nAssign courier to an order(5)\n")

    while user_choice not in ["0", "1", "2", "3", "4", "5"]:
        print("Please pick a valid number.")
        user_choice = input("Please pick an operation:\nReturn to main menu (0).\
                        \nPrint courier list (1).\
                        \nAdd courier to list (2).\nUpdate existing courier (3).\
                        \nDelete courier(4). \
                        \nAssign courier to an order(5)\n")
    user_choice = int(user_choice)
    return user_choice

def couriers_decision_tree():
    """Decision tree if user chooses an option"""
    user_choice_cache = couriers_get_user_choice()
    if user_choice_cache == 0:
        print("Returning to the main menu, please select the appropriate inputs.\n\n\n\n\n\n")
        return 1
    elif user_choice_cache == 1:
        order_by_status = str(input("Do you wish to filter the couriers by status? (y/n)\n").lower())
        while order_by_status not in ["y", "n"]:
            print("That is not a valid input.")
            order_by_status = str(input("Do you wish to filter the couriers by status? (y/n)\n").lower())
        if order_by_status == "n":
            read_all_couriers()
            return 0
        try:
            valid_courier_ids = get_correct_courier_ids()
        except pymysql.err.OperationalError:
            print("There are no current couriers, returning to the menu\n")
            return 0
        statuses = ["stand-by", "assigned", "en-route", "delayed", "completed"]
        for (i, item) in enumerate(statuses, start=0):
            print(i, item)
        chosen_status_ind = int(input(f"Please pick a status 0-{len(statuses) - 1}: "))
        chosen_status = statuses[chosen_status_ind]
        try:
            read_couriers_by_status(chosen_status)
            return 0
        except pymysql.err.OperationalError:
            print("There are no couriers with that status.\nPrinting all couriers")
            read_all_couriers()
            return 0
    elif user_choice_cache == 2:
        courier_name = str(input("What is the courier's name?\n"))
        courier_phone = str(input("What is their phone number?\n"))
        statuses = ["stand-by", "assigned", "en-route", "delayed", "completed"]
        for (i, item) in enumerate(statuses, start=0):
            print(i, item)
        chosen_status_ind = int(input(f"Please pick a status (it is recommended to insert as stand-by when adding new courier) 0-{len(statuses) - 1}: "))
        chosen_status = statuses[chosen_status_ind]
        insert_new_courier(courier_name=courier_name, courier_phone=courier_phone, courier_status=chosen_status)
        return 0
    elif user_choice_cache == 3:
        try:
            valid_courier_ids = get_correct_courier_ids()
        except pymysql.err.OperationalError:
            print("There are no current couriers, returning to the menu\n")
            return 0
        read_all_couriers()
        statuses = ["stand-by", "assigned", "en-route", "delayed", "completed"]
        user_change = str(input("Which courier ID do you wish to change?\n").upper())
        while user_change not in valid_courier_ids:
            print("That is not a valid input")
            user_change = user_change = str(input("Which courier do you wish to change?").upper())
        correct_courier_order_ids = get_valid_courier_order_ids()
        if not correct_courier_order_ids:
            print("There are no current orders, so the order ID for the courier cannot be changed")
        else:
            read_orders()
            valid_orders = get_correct_order_ids()
            change_order = str(input("What do you wish to change the order ID of the courier to? or hit enter to leave the same\n").upper())
            while change_order not in valid_orders and change_order:
                print("That is not a valid order ID")
                change_order = str(input("What do you wish to change the order ID of the courier to? or hit enter to leave the same\n").upper())
            update_courier_order(user_change, change_order)
        change_courier_details = str(input("Do you wish to change the couriers details? y/n\n").lower())
        if change_courier_details != "y":
            read_all_couriers()
            return 0
        changed_courier_name = str(input("What do you wish to change the courier name to? or hit enter to leave the same:\n"))
        changed_courier_phone = str(input("What do you wish to change the courier phone number to? or hit enter to leave the same:\n"))
        changed_courier_status = str(input(f"What do you wish to change the courier status to ({statuses})? or hit enter to leave the same:\n").lower())
        while changed_courier_status not in statuses and changed_courier_status:
            print("That is not a valid status")
            changed_courier_status = str(input(f"What do you wish to change the courier status to ({statuses})? or hit enter to leave the same:\n"))  
        update_courier_details(user_change, changed_courier_name, changed_courier_phone, changed_courier_status)
        read_all_couriers()
        return 0
    elif user_choice_cache == 4:
        try:
            valid_courier_ids = get_correct_courier_ids()
        except pymysql.err.OperationalError:
            print("There are no current couriers, returning to the menu\n")
            return 0
        read_all_couriers()
        user_change = str(input("Which courier do you wish to delete?\nOr leave blank to skip\n").upper())
        while user_change not in valid_courier_ids and user_change:
            print("That is not a valid courier ID")
            user_change = str(input("Which courier do you wish to delete?\nOr leave blank to skip\n").upper())
        if user_change:
            delete_courier(user_change)
            read_all_couriers()
            print("Courier removed successfully, returning to the menu")
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
