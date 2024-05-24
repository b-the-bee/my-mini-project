"""The starting code for the mini project"""

import sys
import os
import time
import products
import orders

if __name__ == "__main__":
    X = "y"
    while X != "n":
        try:
            function_choice = str(input("Please choose whether to access products (p) or access ordering function (o) or courier function (c): ").lower())
            while function_choice not in ["o", "p", "c"]:
                print("That is not a valid choice.")
                function_choice = str(input("Please choose whether to access products (p) or access ordering function (o): ").lower())
            if function_choice == "p":
                stay_products = "y"
                while stay_products == "y":
                    products.products_decision_tree()
                    stay_products = str(input("Would you like to stay on the products program? y/n: ").lower())
            elif function_choice == "o":
                stay_orders = "y"
                while stay_orders == "y":
                    orders.orders_decision_tree()
                    stay_orders = str(input("Would you like to stay on the orders program? y/n: ").lower())
            elif function_choice == "c":
                stay_couriers = "y"
                while stay_orders == "y":
                    orders.orders_decision_tree()
                    stay_orders = str(input("Would you like to stay on the orders program? y/n: ").lower())
        except ValueError:
            time.sleep(4)
            print("You have inputted the wrong data type, running the program again...")
            time.sleep(3)
            continue
        X = str(input("Continue? Return to main menu (y) or exit (n).\n").lower())
        while X not in ["y", "n"]:
            print("Please enter a valid input, y/n")
            X = str(input("Return to main menu? (y) or exit (n)\n").lower())

print("Goodbye =)")
sys.exit()
