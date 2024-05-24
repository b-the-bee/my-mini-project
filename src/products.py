"""Adds functionality for adding, displaying updating and deleting products. Keeping them persistent in JSON"""
import os

try:
    with open("data/product_list.txt", "r+", encoding="UTF-8") as my_file:
        product_list = my_file.read()
except FileNotFoundError as fnfe:
    print(f"Unable to open file {fnfe}")

print(product_list)
def products_get_user_choice():
    """Get's the user's choice and returns the value to be cached later."""
    user_choice = input("\n\n\n\n\n\nPlease pick an operation:\nReturn to main menu (0).\
                        \nPrint product list (1).\
                        \nAdd Product to list (2).\nUpdate existing product (3).\
                        \nDelete Product(4). \n")

    while user_choice not in ["0", "1", "2", "3", "4"]:
        print("Please pick a valid number.")
        user_choice = input("Please pick an operation:\nReturn to main menu (0)."
                            "\nPrint product list (1).\
                            \nAdd Product to list (2).\nUpdate existing product (3).\
                            \nDelete Product(4). \n")
    user_choice = int(user_choice)
    return user_choice

def show_products():
    """Generates an indexed list of products."""
    print("Here is the list of the products:")
    for (i, item) in enumerate(product_list, start = 0):
        print(i, item)


def products_decision_tree():
    """The decision tree for the products program goes through to provide different end user functions"""
    user_choice_cache = products_get_user_choice()
    if user_choice_cache == 0:
        print("Returning to the main menu.\n\n\n\n\n\n")
        return 1
    elif user_choice_cache == 1:
        product_list_length = len(product_list)
        show_products()
        return 0
    elif user_choice_cache == 2:
        user_addition = str(input("What item do you wish to add to the list?\n"))
        product_list.append(user_addition)
        show_products()
        my_file.write(product_list)
        return 0
    elif user_choice_cache == 3:
        product_list_length = len(product_list) - 1
        show_products()
        user_change = int(input(f"Which item do you wish to change? 0-{product_list_length}: "))
        while user_change < 0 or user_change > product_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to change? 0-{product_list_length}: "))
        item_change = str(input("What do you wish to change it to?\n"))
        product_list[user_change] = item_change
        show_products()
        my_file.write(product_list)
        return 0
    elif user_choice_cache == 4:
        product_list_length = len(product_list) - 1
        show_products()
        user_change = int(input(f"Which item do you wish to delete? 0-{product_list_length}: "))
        while user_change < 0 or user_change > product_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to change? 0-{product_list_length}: "))
        product_list.pop(user_change)
        show_products()
        my_file.write(product_list)
        return 0
