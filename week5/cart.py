import colorama
from colorama import Fore, Style
colorama.init()

# vars
items = []
item = ""
num = 1
menu_entry = 0

# clear screen
print('\033[2J')

# initial promt
print("Welcome to the Shopping Cart Program!")

# loop until exit
while menu_entry != "5":

    # menu
    menu_entry = input(f"""{Fore.CYAN}
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
{Style.RESET_ALL}  
Please enter an action:  """)

    # OUT OF RANGE
    if menu_entry not in ("1","2","3","4","5"):
        print(f"{Fore.RED}WARNING: \"{menu_entry}\" is invalid{Style.RESET_ALL}")

    # ADD ITEM
    if menu_entry == "1":
        item = input("What item would you like to add?: ")
        items.append(item)
        print(f"'{Fore.GREEN}{item}' has been added to the cart.{Style.RESET_ALL}")

    # VIEW ITEMS
    elif menu_entry == "2":
        print(f"{Fore.YELLOW}The contents of the shopping cart are: ")
        for item in items:
            print(f"{num}. {item}")
            num += 1
        print(Style.RESET_ALL)   

    # REMOVE ITEM

    # COMPUTE TOTAL

# QUIT
else:
    print("Thank you. Goodbye.\n")
