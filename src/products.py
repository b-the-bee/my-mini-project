"""The products management module"""
import pymysql
from database_handler import insert_new_item, read_all_items, get_correct_product_ids, update_item, delete_item

def products_get_user_choice():
    """Gets the user's choice and returns the value to be cached later."""
    user_choice = input("Please pick an operation:\nReturn to main menu (0).\
                        \nPrint product list (1).\
                        \nAdd Product to list (2).\nUpdate existing product (3).\
                        \nDelete Product(4). \n")

    while user_choice not in ["0", "1", "2", "3", "4"]:
        print("Please pick a valid number.")
        user_choice = input("Please pick an operation:\nReturn to main menu (0)."
                            "\nPrint product list (1).\
                            \nAdd Product to list (2).\nUpdate existing product (3).\
                            \nDelete Product(4). \n")
    return int(user_choice)

def products_decision_tree():
    """The decision tree for the products program goes through to provide different end user functions"""
    user_choice_cache = products_get_user_choice()
    if user_choice_cache == 0:
        print("Returning to the main menu.\n\n\n\n\n\n")
        return 1
    elif user_choice_cache == 1:
        read_all_items()
        return 0
    elif user_choice_cache == 2:
        product_name = input("What is the name of the item do you wish to add to the list?\n")
        product_price = float(input("What is the price of the product?\n"))
        insert_new_item(item= product_name, price= product_price)
        read_all_items()
        return 0
    elif user_choice_cache == 3:
        try:
            valid_product_ids = get_correct_product_ids()
        except pymysql.err.OperationalError:
            print("There are no products, returning to the menu")
            return 0
        read_all_items()
        user_change = str(input("Which item ID do you wish to change?\n").upper())
        while user_change not in valid_product_ids:
            print("That is not a valid input")
            user_change = str(input("Which item ID do you wish to change?\n").upper())
        change_name = str(input("What do you wish to change the name of the product to?\nOr hit enter to skip\n"))
        change_price = float(input("What do you wish to change the price of the product to?\nOr hit enter to skip\n"))
        update_item(item_id = user_change, item_name = change_name, item_price = change_price)
        read_all_items()
        return 0
    elif user_choice_cache == 4:
        try:
            valid_product_ids = get_correct_product_ids()
        except pymysql.err.OperationalError:
            print("There are no products, returning to the menu")
            return 0
        read_all_items()
        which_item = str(input("Which item ID do you wish to delete?\nOr leave blank to skip\n").upper())
        while which_item not in valid_product_ids and which_item:
            print("That is not a valid item ID")
            which_item = str(input("Which item ID do you wish to delete?\nOr leave blank to skip\n").upper())
        if which_item:
            delete_item(which_item)
            read_all_items()
            print("Returning to the menu, item deleted successfully.")
        else:
            print("Operation skipped, returning to the menu.")
        return 0
