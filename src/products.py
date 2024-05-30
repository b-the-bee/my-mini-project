"""The products management module"""
import json

def read_product_list():
    """Reads product list and returns it"""
    try:
        with open("data/products.json", "r", encoding="UTF-8") as my_file:
            product_list = json.load(my_file)
    except FileNotFoundError as fnfe:
        print(f"Unable to open file: {fnfe}")
        product_list = []
    except json.JSONDecodeError as jde:
        print(f"Error decoding JSON: {jde}")
        product_list = []
    return product_list

def write_product_list(product_list):
    """Function for persisting product list"""
    try:
        with open("data/products.json", "w", encoding="UTF-8") as my_file:
            json.dump(product_list, my_file, indent=4)  # Write the list of dictionaries to the file
    except FileNotFoundError as fnfe:
        print(f"Error writing to file: {fnfe}")

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

def show_products(product_list):
    """Generates an indexed list of products."""
    print("Here is the list of the products:")
    for (i, item) in enumerate(product_list):
        print(f"""\n{i}
              Product: {item["item"]}
              Price: £{item["price"]}""")

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
        product_name = input("What is the name of the item do you wish to add to the list?\n")
        product_price = float(input("What is the price of the product?"))
        temp_dict = {
            "Item": product_name,
            "Price": product_price
        }
        product_list.append(temp_dict)
        show_products(product_list)
        write_product_list(product_list)
        return 0
    elif user_choice_cache == 3 and product_list:
        show_products(product_list)
        product_list_length = len(product_list) - 1
        user_change = int(input(f"Which item do you wish to change? 0-{product_list_length}: "))
        while user_change < 0 or user_change > product_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to change? 0-{product_list_length}: "))
        item_change = input("What do you wish to change it to?\n")
        valid_keys = ["item", "price",]
        key_change = str(input(f"What about the product would you like to update? {valid_keys}\n").lower())
        while key_change not in valid_keys:
            print("That is not a valid input.")
            key_change = str(input(f"What about the courier would you like to update? {valid_keys}\n").lower())
        details_change = str(input("What do you wish to change it to?\n"))
        product_list[item_change][key_change] = details_change
        write_product_list(product_list)
        show_products(product_list)
        write_product_list(product_list)
        return 0
    elif user_choice_cache == 4 and product_list:
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
