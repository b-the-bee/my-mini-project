"""The starting code for the mini project"""

import sys
import time
import products
import orders
import couriers
def products_master_program():
    """Manages products module"""
    stay_products = "y"
    while stay_products == "y":
        returned_value_p = int(products.products_decision_tree())
        if returned_value_p == 0:
            stay_products = input("Would you like to stay on the products program? y/n: ").lower()
        else:
            stay_products = "n"

def orders_master_program():
    """Manages orders module"""
    stay_orders = "y"
    while stay_orders == "y":
        returned_value_o = int(orders.orders_decision_tree())
        if returned_value_o == 0:
            stay_orders = input("Would you like to stay on the orders program? y/n: ").lower()
        else:
            stay_orders = "n"

def couriers_master_program():
    """Manages couriers module"""
    stay_couriers = "y"
    while stay_couriers == "y":
        returned_value_c = int(couriers.couriers_decision_tree())
        if returned_value_c == 0:
            stay_couriers = input("Would you like to stay on the courier management program? y/n: ").lower()
        else:
            stay_couriers = "n"

def main():
    """The main code"""
    x = "y"
    while x != "n":
        try:
            function_choice = input("Please choose whether to access products (p) or access ordering function (o) or courier function (c) or exit(n): ").lower()
            while function_choice not in ["o", "p", "c", "n"]:
                print("That is not a valid choice.")
                function_choice = input("Please choose whether to access products (p) or access ordering function (o) or exit(n): ").lower()
            if function_choice == "p":
                products_master_program()
            elif function_choice == "o":
                orders_master_program()
            elif function_choice == "c":
                couriers_master_program()
            else:
                break
        except ValueError:
            time.sleep(4)
            print("You have inputted the wrong data type, running the program again...")
            time.sleep(3)
            continue

        x = input("Continue? Return to main menu (y) or exit (n).\n").lower()
        while x not in ["y", "n"]:
            print("Please enter a valid input, y/n")
            x = input("Return to main menu? (y) or exit (n)\n").lower()

if __name__ == "__main__":
    main()

print("Goodbye =)")
sys.exit()
