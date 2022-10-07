import csv
from datetime import datetime

class colors:
    LIGHTCYAN = '\033[36m'
    GREEN = '\033[38;5;86m'
    CYAN = '\033[94m'
    YELLOW = '\033[38;5;214m'
    RED = '\033[91m'
    LINK = '\033[38;5;225m'
    UNDERLINEON = '\033[4m'
    UNDERLINEOFF = '\033[24m'
    ENDC = '\033[0m'

PATH = 'products.csv'
REQUEST = 'request.csv'
PRODUCT_CODE = 0
PRODUCT_NAME = 1
PRODUCT_PRICE = 2
REQUEST_CODE = 0
REQUEST_QUANTITY = 1
TAX_RATE = .06

def main():
    try:
        products_dict = read_dict(PATH, PRODUCT_CODE)
        decor()
        print(f"{colors.CYAN}Inkom Emporium\n{colors.ENDC}")

        with open(REQUEST,'rt') as file:
            reader = csv.reader(file)
            next(reader)
            items, subtotal = 0, 0

            for line in reader:
                product_code = line[REQUEST_CODE]
                product_quantity = line[REQUEST_QUANTITY]
                product_name = products_dict[product_code][PRODUCT_NAME]
                items += int(product_quantity)
                subtotal += float(products_dict[product_code][PRODUCT_PRICE]) * int(product_quantity)
                tax = subtotal * TAX_RATE
                total = subtotal + tax
                print(f"{colors.GREEN}{product_name}: {product_quantity} @ {products_dict[product_code][PRODUCT_PRICE]}")
          
        print(f"\n{colors.YELLOW}\
Number of Items: {items}\n\
Subtotal: {subtotal:.2f}\n\
Sales Tax: {tax:.2f}\n\
Total: {total:.2f}")
        print(f"\n{colors.CYAN}Thank you for shopping at the Inkom Emporium.")
        print(f"{datetime.now():%c}{colors.ENDC}")
        print("\nWould you like to take a short online survey? [y/n]")
        answer = input("> ").lower()
        if answer in ['y', 'yes', 'sure', '+']:
            print(f"{colors.LINK}{colors.UNDERLINEON}https://forms.gle/Wj7sfoc4L29GQn1b7" + colors.UNDERLINEOFF + colors.ENDC)
        else:
            print("OK...Goodbye...")
        decor()

    # BUG: найти лучшее место, чтобы вывод сверху не печатался
    except KeyError as keyerr:
        print()
        print(f"{colors.RED}Error: unknown product ID in the request.csv file")
        print(keyerr,f"{colors.ENDC}")
        decor()

    except FileNotFoundError as file_not_found:
        print()
        print(f"{colors.RED}Error: missing file")
        print(file_not_found,f"{colors.ENDC}")
        decor()

    except PermissionError as perm_err:
        print(f"{colors.RED}Error: {perm_err}{colors.ENDC}")
        decor()


def decor():
    """Prints a decoration line to separate elements in terminal window
    
    Parameters: None
    Return: None
    """
    print(f"{colors.LIGHTCYAN}="*50 + colors.ENDC)

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    product_dict = {}
    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            key = line[key_column_index]
            product_dict[key] = line
    return product_dict

if __name__ == '__main__':
    main()

