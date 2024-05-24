customers_orders = []


def orders_get_user_choice():
    """Get's the user's choice and returns the value to be cached later."""
    user_choice = input("\n\n\n\n\n\nPlease pick an operation:\nReturn to main menu (0).\
                        \nPrint order list (1).\
                        \nAdd Order to list (2).\nUpdate existing order (3).\
                        \nDelete Order(4). \n")

    while user_choice not in ["0", "1", "2", "3", "4"]:
        print("Please pick a valid number.")
        user_choice = input("\n\n\n\n\n\nPlease pick an operation:\nReturn to main menu (0).\
                        \nPrint order list (1).\
                        \nAdd Order to list (2).\nUpdate existing order (3).\
                        \nDelete Order(4). \n")
    user_choice = int(user_choice)
    return user_choice

def show_orders():
    """Shows a list of saved orders, formatted in dictionaries"""
    print("Here is the list of the orders:")
    for (i, item) in enumerate(customers_orders, start = 0):
        print(f"""Order: \n{i}. 
              \nCustomer Name:{[item['customer-name']]}
              \nCustomer Address:{[item['customer-address']]}
              \nCustomer Phone #:{[item['customer-phone']]}
              \nStatus:{[item['status']]} """)
        
def orders_decision_tree():
    """Decision tree if user chooses o"""
    user_choice_cache = orders_get_user_choice()
    if user_choice_cache == 0:
        print("Returning to the main menu, please select the appropriate inputs.\n\n\n\n\n\n")
    elif user_choice_cache == 1:
        order_list_length = len(customers_orders) - 1
        show_orders()
    elif user_choice_cache == 2:
        customer_name = str(input("What is your name?\n"))
        customer_address = str(input("What is your address?\n"))
        customer_phone = str(input("What is your phone number?\n"))
        statuses = ["preparing", "paid", "completed"]
        status_length = len(statuses) - 1
        for (i, item) in enumerate(statuses, start = 0):
            print(i, item)
        chosen_status_ind = int(input(f"Please pick a status 0-{status_length}: "))
        chosen_status = statuses[chosen_status_ind]
        temp_dict = {
            "customer-name": customer_name,
            "customer-address": customer_address,
            "customer-phone": customer_phone,
            "status": chosen_status,
        }
        customers_orders.append(temp_dict)
        print(customers_orders)
        show_orders()
    elif user_choice_cache == 3 and customers_orders:
        order_list_length = len(customers_orders) - 1
        show_orders()
        user_change = int(input(f"Which order do you wish to change? 0-{order_list_length}: "))
        while user_change < 0 or user_change > order_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to change? 0-{order_list_length}: "))
        valid_keys = ["customer-name", "customer-address", "customer-phone", "status"]
        key_change = str(input(f"What about the order would you like to update? {valid_keys}\n").lower())
        while key_change not in valid_keys:
            print("That is not a valid input.")
            key_change = str(input(f"What about the order would you like to update? {valid_keys}\n").lower())
        details_change = str(input("What do you wish to change it to?\n"))
        customers_orders[user_change][key_change] = details_change
        show_orders()
    elif user_choice_cache == 4 and customers_orders:
        order_list_length = len(customers_orders) - 1
        show_orders()
        user_change = int(input(f"Which order do you wish to delete? 0-{order_list_length}: "))
        while user_change < 0 or user_change > order_list_length:
            print("That is not a valid input")
            user_change = int(input(f"Which item do you wish to change? 0-{order_list_length}: "))
        customers_orders.pop(user_change)
        show_orders()
    else:
        print("No current orders")