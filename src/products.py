import csv

def read_product_list():
    try:
        with open("data/product_list.csv", "r", encoding="UTF-8") as my_file:
            reader = csv.reader(my_file, delimiter=",")
            product_list = next(reader)  # Read the first row as a list of products
    except FileNotFoundError as fnfe:
        print(f"Unable to open file: {fnfe}")
        product_list = []
    return product_list

def write_product_list(product_list):
    try:
        with open("data/product_list.csv", "w", encoding="UTF-8") as my_file:
            writer = csv.writer(my_file)
            writer.writerow(product_list)  # Write the list as a single row
    except Exception as e:
        print(f"Error writing to file: {e}")

def products_get_user_choice():
    """Gets the user's choice and returns the value to be cached later."""
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
    return int(user_choice)

def show_products(product_list):
    """Generates an indexed list of products."""
    print("Here is the list of the products:")
    for i, item in enumerate(product_list):
        print(f"{i}: {item}")

def products_decision_tree():
    """The decision tree for the products program goes through to provide different end user functions"""
    product_list = read_product_list()
    user_choice_cache = products_get_user_choice()

    if user_choice_cache == 0:
        print("Returning to the main menu.\n\n\n\n\n\n")
        return 1
    elif user_choice_cache == 1:
        show_products(product_list)
        return 0
    elif user_choice_cache == 2:
        user_addition = input("What item do you wish to add to the list?\n")
        product_list.append(user_addition)
        show_products(product_list)
        write_product_list(product_list)
        return 0
    elif user_choice_cache == 3:
        show_products(product_list)
        product_list_length = len(product_list) - 1
        user_change = int(input(f"Which item do you wish to change? 0-{product_list_length}: "))
        while user_change < 0 or user_change > product_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to change? 0-{product_list_length}: "))
        item_change = input("What do you wish to change it to?\n")
        product_list[user_change] = item_change
        show_products(product_list)
        write_product_list(product_list)
        return 0
    elif user_choice_cache == 4:
        show_products(product_list)
        product_list_length = len(product_list) - 1
        user_change = int(input(f"Which item do you wish to delete? 0-{product_list_length}: "))
        while user_change < 0 or user_change > product_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to delete? 0-{product_list_length}: "))
        product_list.pop(user_change)
        show_products(product_list)
        write_product_list(product_list)
        return 0