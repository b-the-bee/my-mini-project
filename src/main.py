"""The starting code for the mini project"""

import sys

product_list = ["White Americano","Black Americano", "Cappuccino", "Mocha", "Latte",
                "Cortado", "Macchiato", "Iced Americano", "Iced Cappuccino", "Iced Mocha",
                "Iced Latte", "Iced Cortado", "Iced Macchiato"]
customers_orders = []
order_number = 0


def products_get_user_choice():
    """Get's the user's choice and returns the value to be cached later."""
    user_choice = input("\n\n\n\n\n\nPlease pick an operation:\nReturn to main menu (0).\
                        \nPrint product list (1).\
                        \nAdd Product to list (2).\nUpdate existing product (3).\
                        \nDelete Product(4).\\n")

    while user_choice not in ["0", "1", "2", "3", "4"]:
        print("Please pick a valid number.")
        user_choice = input("Please pick an operation:\nReturn to main menu (0)."
                            "\nPrint product list (1).\
                            \nAdd Product to list (2).\nUpdate existing product (3).\
                            \nDelete Product(4).")
    user_choice = int(user_choice)
    return user_choice

def show_products():
    """Generates an indexed list of products."""
    print("Here is the list of the products:")
    for (i, item) in enumerate(product_list, start = 0):
        print(i, item)




def products_decision_tree():
    """The decision tree the program goes through to provide functionality"""
    user_choice_cache = products_get_user_choice()
    if user_choice_cache == 0:
        print("Returning to the main menu.\n\n\n\n\n\n")
    elif user_choice_cache == 1:
        product_list_length = len(product_list)
        show_products()
    elif user_choice_cache == 2:
        user_addition = str(input("What item do you wish to add to the list?\n"))
        product_list.append(user_addition)
        show_products()
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
    elif user_choice_cache == 4:
        product_list_length = len(product_list) - 1
        show_products()
        user_change = int(input(f"Which item do you wish to delete? 0-{product_list_length}: "))
        while user_change < 0 or user_change > product_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to change? 0-{product_list_length}: "))
        product_list.pop(user_change)
        show_products()




def orders_get_user_choice():
    """Get's the user's choice and returns the value to be cached later."""
    user_choice = input("\n\n\n\n\n\nPlease pick an operation:\nReturn to main menu (0).\
                        \nPrint order list (1).\
                        \nAdd Order to list (2).\nUpdate existing order (3).\
                        \nDelete Order(4).\\n")

    while user_choice not in ["0", "1", "2", "3", "4", "5"]:
        print("Please pick a valid number.")
        user_choice = input("\n\n\n\n\n\nPlease pick an operation:\nReturn to main menu (0).\
                        \nPrint order list (1).\
                        \nAdd Order to list (2).\nUpdate existing order (3).\
                        \nDelete Order(4).\\n")
    user_choice = int(user_choice)
    return user_choice

def show_orders():
    """Shows a list of saved orders, formatted in dictionaries"""
    print("Here is the list of the products:")
    for (i, item) in enumerate(customers_orders, start = 0):
        print(i, item)



def orders_decision_tree():
    """Decision tree if user chooses o"""
    user_choice_cache = orders_get_user_choice()
    if user_choice_cache == 0:
        print("Returning to the main menu.\n\n\n\n\n\n")
    elif user_choice_cache == 1:
        order_list_length = len(product_list)
        show_orders()
    elif user_choice_cache == 2:
        customer_name = str(input("What is your name?\n"))
        customer_address = str(input("What is your address?\n"))
        customer_phone = str(input("What is your phone numbers?\n"))
        customers_orders[order_number] = {
            "Customer Name": {customer_name},
            "Customer Address": {customer_address},
            "Customer Phone": {customer_phone},
            "Status": "preparing"
        }
        show_orders()
    elif user_choice_cache == 3:
        order_list_length = len(customers_orders) - 1
        show_orders()
        user_change = int(input(f"Which order do you wish to change? 0-{order_list_length}: "))
        while user_change < 0 or user_change > order_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to change? 0-{order_list_length}: "))
        item_change = str(input("What do you wish to change it to?\n"))
        product_list[user_change] = item_change
        show_orders()
    elif user_choice_cache == 4:
        product_list_length = len(product_list) - 1
        show_orders()
        user_change = int(input(f"Which order do you wish to delete? 0-{order_list_length}: "))
        while user_change < 0 or user_change > product_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to change? 0-{order_list_length}: "))
        customers_orders.pop(user_change)
        show_orders()
if __name__ == "__main__":
    X = "y"
    while X != "n":
        try:
            function_choice = str(input("Please choose whether to access products (p)\
                or access ordering function (o): ").lower())
            while function_choice not in ["o", "p"]:
                print("That is not a valid choice.")
                function_choice = str(input("Please choose whether to access products (p)\
                    or access ordering function (o): ").lower())
            if function_choice == "p":
                products_decision_tree()
            elif function_choice == "o":
                orders_decision_tree()
        except ValueError:
            print("You have inputted the wrong data type, running the program again...")
            continue
        X = str(input("Continue? (y/n)\n").lower())
        while X not in ["y", "n"]:
            print("Please enter a valid input, y/n")
            X = str(input("Continue? (y/n)\n").lower())

print("Goodbye =)")
sys.exit()
