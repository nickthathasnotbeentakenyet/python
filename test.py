# TODO:
# HACK:
# NOTE:
# FIXME:
# BUG:
# REVIEW:
# COMMENT:
# WARNING:
# PERF:

menu = ["Add item", "View cart", "Remove item", "Compute total","Quit"]
items = []
prices = []
selling_price = None
product = None
menu_entry = "0"

# Menu display
print(f"Welcome to the Shopping Cart Program!")
for i in menu:
    # notice "+1" for the index. We want to start list from 1, not 0  
    print(f"{menu.index(i)+1}.  {i}")

# keep looping until user enters 5, which is 'quit'
while menu_entry != "5":

    # ask user to enter number that represents desired action
    menu_entry = input("Please enter an action. 1 to add, 2 to view, 3 to remove, 4 for total or 5 to quit: ")

    # if user enters 1, which is 'add item'
    if menu_entry == "1":
        product = input("What item would you like to add?: ")
        selling_price = float(input(f"What is the price of '{product}'?: "))
        items.append(product)
        prices.append(selling_price)
        print(f"{product} has been added to the cart.")

    # if user enters 2, which is 'view cart'
    elif menu_entry == "2":
        print("The contents of the shopping cart are:")
        for i in items:
            # printing list number, product, price of the product based on the index of that product
            # notice "+1" for the index. We want to start list from 1, not 0  
            print(f"{items.index(i)+1}. {i} {prices[items.index(i)]}")
    
    # if user enters 3, which is 'remove a product'
    # elif menu_entry == "3":
        
    # if user enters 4, which is 'compute total'        
    # elif menu_entry == "4":

# if user enters 5, which is 'quit'
else:
    print(f"Thank you. Goodbye.")