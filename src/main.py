"""The starting code for the mini project"""

import sys
import os
import time
import products
import orders
def products_master_program():
    stay_products = "y"
    while stay_products == "y":
        returned_value_p = products.products_decision_tree()
        if returned_value_p == 0:
            stay_products = input("Would you like to stay on the products program? y/n: ").lower()
        else:
            stay_products = "n"

def orders_master_program():
    stay_orders = "y"
    while stay_orders == "y":
        returned_value_o = orders.orders_decision_tree()
    if returned_value_o == 0:
        stay_orders = input("Would you like to stay on the orders program? y/n: ").lower()
    else:
        stay_orders = "n"
    
def main():
    """The main code"""
    X = "y"
    while X != "n":
        try:
            function_choice = input("Please choose whether to access products (p) or access ordering function (o) or courier function (c): ").lower()
            while function_choice not in ["o", "p", "c"]:
                print("That is not a valid choice.")
                function_choice = input("Please choose whether to access products (p) or access ordering function (o): ").lower()
            if function_choice == "p":
                products_master_program()
            elif function_choice == "o":
                orders_master_program()
            elif function_choice == "c":
                pass

        except ValueError:
            time.sleep(4)
            print("You have inputted the wrong data type, running the program again...")
            time.sleep(3)
            continue

        X = input("Continue? Return to main menu (y) or exit (n).\n").lower()
        while X not in ["y", "n"]:
            print("Please enter a valid input, y/n")
            X = input("Return to main menu? (y) or exit (n)\n").lower()

if __name__ == "__main__":
    main()

print("Goodbye =)")
sys.exit()
