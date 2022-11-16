import csv 
def main():
    PRODUCT_NUMBER = 0
    ITEM_NAME = 1
    PRICE_OF_PRODUCT = 2
    REQUESTED_PROD_NUM = 0
    QUANTITY = 1

    products_dict = read_dict('products.csv', PRODUCT_NUMBER)

    print()
    print('Inkom Emporium')
    print() 
    with open('request.csv', 'rt') as request_file:
        second_read = csv.reader(request_file)
        next(second_read)
        total_items = 0
        for list in second_read:
            request_prod = list[REQUESTED_PROD_NUM]
            prod_quantity = list[QUANTITY]
            total_items += int(prod_quantity)
            prod_name = products_dict[request_prod][ITEM_NAME]
            prod_price = products_dict[request_prod][PRICE_OF_PRODUCT]
            print(f'{prod_name}: {prod_quantity} @ {prod_price}')
            print()
    print(f'The number of items: {total_items}')




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

main()