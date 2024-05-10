"""The starting code for the mini project"""
product_list = ["White Americano","Black Americano", "Cappuccino", "Mocha", "Latte",
                "Cortado", "Macchiato", "Iced Americano", "Iced Cappuccino", "Iced Mocha",
                "Iced Latte", "Iced Cortado", "Iced Macchiato"]
user_choice = int(input("Please pick an operation:\nReturn to main menu (0).\n"
                        "Print product list (1)."
                        "\nAdd Product to list (2).\nUpdate existing product (3).\nDelete Product(4).\n"))

while user_choice not in [0, 1, 2, 3, 4]:
    print("Please pick a valid number.")
    user_choice = int(input("Please pick an operation:\nReturn to main menu (0).\n Print product list (1).\nAdd Product to list (2).\nUpdate existing product (3).\nDelete Product(4).\n"))
    
if user_choice == 0:
    print("Go to main menu")
elif user_choice == 1:
    product_list_length = len(product_list)
    print("Here is a list of products")
    for (i, item) in enumerate(product_list, start = 0):
        print(i, item)            
elif user_choice == 3:
    product_list_length = len(product_list)
    print("Here is a list of products:")
    for (i, item) in enumerate(product_list, start = 0):
        print(i, item)
    user_change = int(input(f"Which item do you wish to change? 0-{product_list_length}"))
    item_change = str(input("What do you wish to change it to?"))
    product_list[user_change] = item_change
elif user_choice == 4:
    print("Here is a list of products:")
    for (i, item) in enumerate(product_list, start = 0):
        print(i, item)
    user_change = int(input(f"Which item do you wish to delete? 0-{product_list_length}"))
    product_list -= [user_change]
    




if __name__ == "__main__":
    next