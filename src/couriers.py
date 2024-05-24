import json

# Initialise couriers
couriers = []

def read_courier_list():
    try:
        with open("data/couriers.json", "r", encoding="UTF-8") as my_file:
            courier_list = json.load(my_file)
    except FileNotFoundError as fnfe:
        print(f"Unable to open file: {fnfe}")
        courier_list = []
    except json.JSONDecodeError as jde:
        print(f"Error decoding JSON: {jde}")
        courier_list = []
    return courier_list

def write_courier_list(courier_list):
    try:
        with open("data/couriers.json", "w", encoding="UTF-8") as my_file:
            json.dump(courier_list, my_file, indent=4)  # Write the list of dictionaries to the file
    except FileNotFoundError as fnfe:
        print(f"Error writing to file: {fnfe}")

def couriers_get_user_choice():
    """Get's the user's choice and returns the value to be cached later."""
    user_choice = input("\nPlease pick an operation:\nReturn to main menu (0).\
                        \nPrint courier list (1).\
                        \nAdd courier to list (2).\nUpdate existing courier (3).\
                        \nDelete courier(4). \n")

    while user_choice not in ["0", "1", "2", "3", "4"]:
        print("Please pick a valid number.")
        user_choice = input("Please pick an operation:\nReturn to main menu (0).\
                        \nPrint courier list (1).\
                        \nAdd courier to list (2).\nUpdate existing courier (3).\
                        \nDelete courier(4). \n")
    user_choice = int(user_choice)
    return user_choice

def show_couriers():
    """Shows a list of saved couriers, formatted in dictionaries"""
    print("Here is the list of the couriers:")
    for (i, item) in enumerate(couriers, start=0):
        print(f"""Courier Number: {i}. 
              \nCourier Name: {item['courier-name']}
              \nTarget Address: {item['target-address']}
              \nCourier Phone #: {item['courier-phone']}
              \nOrder Status: {item['status']} """)

def couriers_decision_tree():
    """Decision tree if user chooses an option"""
    global couriers
    user_choice_cache = couriers_get_user_choice()
    if user_choice_cache == 0:
        print("Returning to the main menu, please select the appropriate inputs.\n\n\n\n\n\n")
        return 1
    elif user_choice_cache == 1:
        show_couriers()
        return 0
    elif user_choice_cache == 2:
        courier_name = str(input("What is the courier's name?\n"))
        target_address = str(input("What is the courier's target address?\n"))
        courier_phone = str(input("What is their phone number?\n"))
        statuses = ["stand-by", "en-route", "delayed", "completed"]
        for (i, item) in enumerate(statuses, start=0):
            print(i, item)
        chosen_status_ind = int(input(f"Please pick a status 0-{len(statuses) - 1}: "))
        chosen_status = statuses[chosen_status_ind]
        temp_dict = {
            "courier-name": courier_name,
            "target-address": target_address,
            "courier-phone": courier_phone,
            "status": chosen_status,
        }
        couriers.append(temp_dict)
        write_courier_list(couriers)  # Write to file after adding
        show_couriers()
        return 0
    elif user_choice_cache == 3 and couriers:
        show_couriers()
        user_change = int(input(f"Which courier do you wish to change? 0-{len(couriers) - 1}: "))
        while user_change < 0 or user_change >= len(couriers):
            print("That is not a valid input")
            user_change = int(input(f"Which courier do you wish to change? 0-{len(couriers) - 1}: "))
        valid_keys = ["courier-name", "target-address", "courier-phone", "status"]
        key_change = str(input(f"What about the courier would you like to update? {valid_keys}\n").lower())
        while key_change not in valid_keys:
            print("That is not a valid input.")
            key_change = str(input(f"What about the courier would you like to update? {valid_keys}\n").lower())
        details_change = str(input("What do you wish to change it to?\n"))
        couriers[user_change][key_change] = details_change
        write_courier_list(couriers)  # Write to file after updating
        show_couriers()
        return 0
    elif user_choice_cache == 4 and couriers:
        show_couriers()
        user_change = int(input(f"Which courier do you wish to delete? 0-{len(couriers) - 1}: "))
        while user_change < 0 or user_change >= len(couriers):
            print("That is not a valid input")
            user_change = int(input(f"Which courier do you wish to delete? 0-{len(couriers) - 1}: "))
        couriers.pop(user_change)
        write_courier_list(couriers)  # Write to file after deleting
        show_couriers()
        return 0
    else:
        print("No current couriers")
        return 0

# Read initial couriers from the file
couriers = read_courier_list()