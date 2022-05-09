import colorama
from colorama import Fore
colorama.init()

# vars
items = []
prices = []
item = ""
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
{Fore.RESET}  
Please enter an action:  """)

    # OUT OF BOUNDS
    if menu_entry not in ("1","2","3","4","5"):
        print(f"{Fore.RED}WARNING: \"{menu_entry}\" is invalid{Fore.RESET}")

    # ADD ITEM
    if menu_entry == "1":
        item = input("What item would you like to add?: ")
        price = float(input(f"What is the price of '{item}'?: "))
        items.append(item)
        prices.append(price)
        print(f"'{Fore.GREEN}{item}' has been added to the cart.{Fore.RESET}")

    # VIEW ITEMS
    elif menu_entry == "2":
        num = 1
        if len(items) == 0:
            print(f"{Fore.YELLOW}The shopping cart is empty.{Fore.RESET}")
        # if the cart contains at least 1 item
        else:
            print(f"{Fore.YELLOW}The contents of the shopping cart are: ")
            for item in items:
                # cart items printed with their prices [indexes are taken from the items]
                print(f"{num}. {item} - ${prices[items.index(item)]:.2f}")
                num += 1              
            print(Fore.RESET)   

    # REMOVE ITEM
    elif menu_entry == "3":
        item_remove = int(input("Which item would you like to remove?: "))
        # out of bounds message
        if item_remove <= 0 or item_remove > len(items):
            print(f"{Fore.RED}Sorry, that is not a valid item number.{Fore.RESET}")
        else:
            del items[item_remove-1]
            del prices[item_remove-1]
            print(f"{Fore.MAGENTA}Item removed.{Fore.RESET}")

    # COMPUTE TOTAL
    elif menu_entry == "4":
        total = sum(prices)
        print(f"{Fore.YELLOW}The total price of the items in the shopping cart is ${total:.2f}{Fore.RESET}")
# QUIT
else:
    print(f"{Fore.CYAN}Thank you. Goodbye.\n{Fore.RESET}")
